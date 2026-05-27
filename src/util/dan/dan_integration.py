import os
import shutil
import logging
from . import dan_evaluator
from .pdg_generator import PDGGenerator

# Configure logging
logger = logging.getLogger(__name__)

class DANIntegrator:
    def __init__(self, model_name="microsoft/codebert-base-mlm"):
        """
        Initialize DAN Integrator.
        Loads the model once to be reused across multiple test files.
        """
        self.model_name = model_name
        self.model, self.tokenizer, self.model_type = dan_evaluator.load_model(model_name)
        
        # Native PDG generator used instead of Joern
        self.joern_available = True 

    def _generate_pdg(self, file_path, output_dir):
        """
        Generates PDG for a single file using native PDGGenerator.
        Returns path to the generated DOT file(s) directory.
        """
        # Create a unique temp dir for this run to avoid collisions
        temp_pdg_dir = os.path.join(output_dir, "pdg_output")
        os.makedirs(temp_pdg_dir, exist_ok=True)
        
        try:
            with open(file_path, "r") as f:
                source_code = f.read()

            generator = PDGGenerator(source_code)
            # Returns dict: {func_name: nx.DiGraph}
            graphs = generator.build()
            
            if not graphs:
                logger.warning(f"No functions found in {file_path} to generate PDGs for.")
                return None
            
            # Save each graph to a separate DOT file
            ordered_filenames = []
            for func_name, graph in graphs.items():
                try:
                    # Sanitize func_name for filename
                    safe_name = "".join(c for c in func_name if c.isalnum() or c in ('_', '-'))
                    filename = f"{safe_name}.dot"
                    dot_path = os.path.join(temp_pdg_dir, filename)
                    generator.save_to_dot(graph, dot_path)
                    ordered_filenames.append(filename)
                except Exception as e:
                    logger.error(f"Failed to save DOT file for {func_name}: {e}")

            return temp_pdg_dir, ordered_filenames

        except Exception as e:
            logger.error(f"Error generating PDG: {e}")
            return None

    def compute_score(self, file_path, temp_output_base_dir="/tmp"):
        """
        Computes the DAN score for a Python file.
        Returns a DICTIONARY of scores: { "method_name": score, ... }
        """
        if not self.model:
            return None
            
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return None

        # Generate PDGs
        res = self._generate_pdg(file_path, temp_output_base_dir)
        if not res:
            return None
        pdg_dir, ordered_files = res
            
        # Score using dan_evaluator logic
        try:
            # scores is a dict: { "filename.dot": score }
            raw_scores = dan_evaluator.process_directory(
                pdg_dir, self.model, self.tokenizer, self.model_type, 
                ordered_files=ordered_files
            )
            
            if not raw_scores:
                return {}
            
            # Clean up keys: "test_method.dot" -> "test_method"
            final_scores = {}
            # If we have ordered_files, follow that order for final_scores keys
            if ordered_files:
                for filename in ordered_files:
                    if filename in raw_scores:
                        method_name = os.path.splitext(filename)[0]
                        final_scores[method_name] = raw_scores[filename]
            else:
                # Fallback to natural sorting if no ordered_files (shouldn't happen with updated _generate_pdg)
                sorted_keys = sorted(raw_scores.keys(), key=dan_evaluator.natural_sort_key)
                for filename in sorted_keys:
                    method_name = os.path.splitext(filename)[0]
                    final_scores[method_name] = raw_scores[filename]
                
            return final_scores
            
        finally:
            # Cleanup PDGs is optional, maybe keep it if debugging? 
            if pdg_dir and os.path.exists(pdg_dir):
                shutil.rmtree(pdg_dir, ignore_errors=True)

