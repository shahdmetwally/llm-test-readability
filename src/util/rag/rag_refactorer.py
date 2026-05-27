from .rag_pipeline import build_test_refactor_rag_chain, RetrievalConfig

class TestRefactorRAG:
    def __init__(self, llm, vectorstores, tokenizer, prompt_type="base"):
        self.llm = llm
        self.vectorstores = vectorstores
        self.tokenizer = tokenizer
        self.prompt_type = prompt_type
        
        # Default config; could be passed in
        # Reduced limits for performance and to avoid context overflow
        self.cfg = RetrievalConfig(
            k_code=4,
            k_docs=1,
            max_code_total=4,
            max_docs_total=1,
            max_chars_per_doc=2000,
        )
        
        self.chain = self._build_chain()

    def _build_chain(self):
        return build_test_refactor_rag_chain(
            llm=self.llm,
            vectorstores=self.vectorstores,
            tokenizer=self.tokenizer,
            cfg=self.cfg,
            model_max_input=16384,  # Adjust
            prompt_type=self.prompt_type
        )

    def refactor_raw(
        self,
        test_code: str,
        module_hint: str = "",
        extra_hint: str = "",
    ) -> str:
        # The chain expects a dict
        raw = self.chain.invoke({
            "test_code": test_code,
            "module_hint": module_hint,
            "extra_hint": extra_hint,
        })
        return raw

    def refactor(
        self,
        test_code: str,
        module_hint: str = "",
        extra_hint: str = "",
    ) -> str:
        raw = self.refactor_raw(test_code, module_hint, extra_hint)
        from .. import extractor
        return extractor.extract_response(raw)
