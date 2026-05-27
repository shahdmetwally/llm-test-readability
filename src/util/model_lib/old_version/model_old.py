from __future__ import annotations
from enum import Enum
from os import PathLike
import copy

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BatchEncoding,
    PreTrainedTokenizer,
    PreTrainedTokenizerFast,
    PreTrainedModel,
    MistralForCausalLM,
    MixtralForCausalLM,
    LlamaForCausalLM
    #,Conversation   has been removed from transformers 
)




import torch
from typing import Final

from .model_old import *

class TokenError(Exception):
    """Base class for exceptions related to token errors in the model."""
    pass

class NegativeTokenCountError(TokenError):
    """Exception raised when the token count becomes negative.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Negative token count: context window exceeded."):
        self.message = message
        super().__init__(self.message)

class InsufficientAllowedTokensError(TokenError):
    """Exception raised when there are insufficient tokens allowed for response generation.

    Attributes:
        allowed_tokens -- the number of allowed tokens
        message -- explanation of the error
    """
    def __init__(self, allowed_tokens: int, message: str = "Insufficient allowed tokens. Minimum required is 1000."):
        self.allowed_tokens = allowed_tokens
        self.message = f"{message} Allowed tokens: {allowed_tokens}."
        super().__init__(self.message)


class ModelLoadingException(Exception):
    def __init__(self, model_name_or_path: str | PathLike, *args):
        super().__init__(f"{model_name_or_path} is being loaded.", *args)


class UnsupportedModelException(Exception):
    def __init__(self, model_type: str, *args: object) -> None:
        super().__init__(f"{model_type} is not supported right now.", *args)


class _ModelType(Enum):
    MISTRAL: dict = {
        "inst": ("[INST]", "[/INST]"),
        "bos": "<s>",
        "eos": "</s>"
    }
    LLAMA: dict = {
        "inst": ("user", "assistant"),
        "bos": "",
        "eos": ""
    }
    


class Model:
    def __init__(
        self,
        tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast = None,
        model: PreTrainedModel = None,
        max_new_tokens: int = 2048,  # Default value for max_new_tokens
        context_window: int = 4096,  # Default value for context_window
        temperature: float = 0.1  # Default value for temperature
    ):
        

        self.tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast = tokenizer
        self.model: PreTrainedModel = model
        self.max_new_tokens: int = max_new_tokens
        self._context_window: int = context_window
        self.temperature: float = temperature
        
        # Set the type of the model
        self.type: _ModelType
        if isinstance(model, (MistralForCausalLM, MixtralForCausalLM)):
            self.type = _ModelType.MISTRAL
        elif isinstance(model, LlamaForCausalLM):
            self.type = _ModelType.LLAMA
        # Pass the placeholder
        elif tokenizer is None and model is None:
            pass
        else:
            raise UnsupportedModelException(type(model).__name__)

        _MODELS: Final[dict[str | PathLike, Model]] = {}

    _PLACEHOLDER: Model = None

    # System prompt used for REST-at
    _SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

    # Placeholder for loaded models
    _MODELS: Final[dict[str | PathLike, Model]] = {}

    _PLACEHOLDER: Model = None

    # System prompt used for REST-at
    _SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

    @staticmethod
    def _get_placeholder() -> Model:
        """
        Retrieves the placeholder for loading models.

        Returns:
        --------
        `Model` - An empty placeholder model.
        """
        if not Model._PLACEHOLDER:
            # Initialize placeholder with default values
            Model._PLACEHOLDER = Model()
        return Model._PLACEHOLDER

    @staticmethod
    def _get(model_name_or_path: str | PathLike) -> Model | None:
        """
        Gets a model if loaded, else `None`

        Parameters:
        -----------
        model_name_or_path: str | PathLike - The model to get. Can be either a model name from Hugging Face Hub or a path to a local model.

        Returns:
        --------
        `Model | None` The tokenizer and the model itself if loaded, else None.
        """
        return Model._MODELS.get(model_name_or_path, None)

    @staticmethod
    def get(
        model_name_or_path: str | PathLike,
        max_new_tokens: int = None,
        context_window: int = 4096,
        temperature: float = 0.1,
    ) -> Model | None:
        m: Model = Model._get(model_name_or_path)

        # Return None if the loading placeholder is present
        if m is Model._get_placeholder():
            return None

        # Return model if already loaded
        if m:
            return m
        
        if max_new_tokens is None:
            raise ValueError("Cannot load model without max_new_tokens.")
        
        # Add a placeholder in the dict to prevent additional loads
        Model._MODELS[model_name_or_path] = Model._get_placeholder()

        # Load the model and its tokenizer
        tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast = AutoTokenizer.from_pretrained(model_name_or_path)

        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        # Ensure that the model is in evaluation mode
        model.eval()


        Model._MODELS[model_name_or_path] = m = Model(tokenizer, model, max_new_tokens, context_window, temperature)

        return m

    
    def _apply_chat_template_llama(self, messages: list[dict[str, str]]) -> BatchEncoding:
        """
        Applies a pre-defined Llama chat template to a message history and tokenizes it.

        Parameters:
        -----------
        messages: list[dict[str, str]] - The message history.

        Returns:
        --------
        `BatchEncoding` - The encoded input.

        Raises:
        -------
        `ValueError` if `message["content"]` is empty or consists of only whitespace characters for any message.
        """

        # Remove leading and trailing whitespace
        for message in messages:
            message["content"] = message["content"].strip()

            if not message["content"]:
                raise ValueError("Messages can't be empty!")

        # The LLaMA tokeniser supports system prompts
        return self.tokenizer(
            self.tokenizer.apply_chat_template(messages, tokenize=False),
            return_tensors="pt",
            return_attention_mask=True
        )
    
    def _apply_chat_template_mistral(self, messages: list[dict[str, str]]) -> BatchEncoding:
        """
        Applies a pre-defined Mistral/Mixtral chat template to a message history and tokenizes it.

        Parameters:
        -----------
        messages: list[dict[str, str]] - The message history.

        Returns:
        --------
        `BatchEncoding` - The encoded input.

        Raises:
        -------
        `ValueError` if `message["content"]` is empty or consists of only whitespace characters for any message.
        """
        chat: str = self.tokenizer.bos_token

        # Apply template

        # Check for system message in the message history
        # Use the default one in there is no system message
        sys_message: str = Model._SYSTEM_PROMPT
        if messages[0]["role"] == "system":
            sys_message = messages[0]["content"]
            messages = messages[1:]

        for i, message in enumerate(messages):
            # The message history MUST lead with a user message
            # and then alternate between user and assistant
            if (message["role"] == "user") != (i % 2 == 0):
                raise Exception("Conversation roles must alternate user/assistant/user/assistant/...")

            # Remove any leading or trailing whitespace characters
            message["content"] = message["content"].strip()

            # Check for empty messages
            if not message["content"]:
                raise ValueError("Messages can't be empty!")

            # Format the message history into a single string
            if message["role"] == "user":
                chat += "[INST]\n" \
                        + (f"<system>\n{sys_message}\n</system>\n\n" if sys_message else "") \
                        + f"{message['content']}\n[/INST]"
            elif message["role"] == "assistant":
                chat += f"{message['content']}{self.tokenizer.eos_token}"
            elif message["role"] == "system":
                raise Exception("System messages must be the first entry in the history.")
            else:
                raise Exception("Only system, user, and assistant roles are supported!")

        return self.tokenizer(chat, return_tensors="pt", return_attention_mask=True)

    def _apply_chat_template(self, messages: list[dict[str, str]]) -> BatchEncoding:
        match (self.type):
            case _ModelType.MISTRAL:
                return self._apply_chat_template_mistral(messages)
            case _ModelType.LLAMA:
                return self._apply_chat_template_llama(messages)
    
    def generate_response_fixed_max_tokens(
            self,
            history: list[dict[str, str]] ,
            prompt: str,
        ) -> str:
        history.append({"role": "user", "content": prompt})
        input_ids: BatchEncoding = self._apply_chat_template(history).to("cuda")

        outputs = self.model.generate(
            **input_ids,
            max_new_tokens=self.max_new_tokens,
            do_sample=True,
            temperature=self.temperature
        )

        raw_res: str = self.tokenizer.decode(outputs[0])

        # 1 at inst in the instruction suffix
        inst_suffix: str = self.type.value["inst"][1]
        inst_suffix_len: int = len(inst_suffix)
        # Cut out the instruction section of the output
        res: str = raw_res[
            (raw_res.rfind(inst_suffix) + inst_suffix_len):raw_res.rfind(self.tokenizer.eos_token)
        ].strip()

        # Append response to history
        history.append({"role": "assistant", "content": res})
        return res
    
    def generate_response_dynamic_max_tokens(
        self,
        history: list[dict[str, str]],
        prompt: str,
    ) -> str:
        # Append the user prompt to the history
        history.append({"role": "user", "content": prompt})

        # Calculate the number of tokens used by the history and the system prompt
        input_ids: BatchEncoding = self._apply_chat_template(history).to("cuda")
        total_input_tokens = input_ids.input_ids.size(1)  # Count the number of input tokens

        # Calculate the maximum new tokens dynamically
        #print("context_window", self.context_window)
        
        print("\nFrom Model: printing input tokens:", total_input_tokens)
   
        
        max_allowed_tokens = self.context_window - total_input_tokens - 100  # Buffer to ensure we don't hit the limit of the context window
        
        print("From Model: printing max allowed tokens set to:")
        print(max_allowed_tokens)
        print("\n")


        # Raise exceptions for token errors
        if max_allowed_tokens < 0:
            raise NegativeTokenCountError("Negative token count: context window exceeded.")
        elif max_allowed_tokens < 700:
            raise InsufficientAllowedTokensError(max_allowed_tokens)

        # Ensure we don't set a negative max_new_tokens value
        dynamic_max_new_tokens = max(0, max_allowed_tokens)

        # Generate the model's response
        outputs = self.model.generate(
            **input_ids,
            max_new_tokens=dynamic_max_new_tokens,
            do_sample=True,
            temperature=self.temperature
        )

        raw_res: str = self.tokenizer.decode(outputs[0])

        # Extract the response after the instruction suffix
        inst_suffix: str = self.type.value["inst"][1]
        inst_suffix_len: int = len(inst_suffix)
        res: str = raw_res[
            (raw_res.rfind(inst_suffix) + inst_suffix_len):raw_res.rfind(self.tokenizer.eos_token)
        ].strip()

        # Append the assistant's response to the history
        history.append({"role": "assistant", "content": res})

        return res
    
    def count_tokens(
        self,
        history: list[dict[str, str]],
        prompt: str,
    ) -> int:
        # Make a copy of the history to avoid modifying the original list
        history_copy = copy.deepcopy(history)

        # Append the user prompt to the history copy
        history_copy.append({"role": "user", "content": prompt})

        # Apply the chat template, which formats the messages with role markers and special tokens
        tokenized_input = self._apply_chat_template(history_copy)

        # Count the number of tokens in the input
        # tokenized_input.input_ids is a tensor, and size(1) gives the length of the token sequence
        return tokenized_input.input_ids.size(1)
    
    @property
    def max_new_tokens(self) -> int:
        """
        Getter for max_new_tokens.
        
        Returns:
        --------
        int - The maximum number of new tokens the model can generate.
        """
        return self._max_new_tokens

    @max_new_tokens.setter
    def max_new_tokens(self, value: int) -> None:
        """
        Setter for max_new_tokens. Ensures that the value is positive.

        Parameters:
        -----------
        value: int - The new value for max_new_tokens.

        Raises:
        -------
        ValueError - If value is not positive.
        """
        if value <= 0:
            raise ValueError("max_new_tokens must be positive.")
        self._max_new_tokens = value
    
    @property
    def context_window(self) -> int:
        return self._context_window

    @context_window.setter
    def context_window(self, value: int) -> None:
        if value <= 0:
            raise ValueError("context_window must be a positive integer.")
        self._context_window = value


class Session:
    def __init__(
            self,
            name: str,
            model_name_or_path: str | PathLike,
            max_new_tokens: int,
            system_prompt: str,
            temperature: float = 0.1
        ):
        self.name: str = name
        self.temperature: float = temperature
        self.model: Model = Model.get(model_name_or_path, max_new_tokens,temperature=self.temperature)

        # Don't instantiate if model is loading
        if not self.model:
            raise ModelLoadingException(model_name_or_path)

        self._system_prompt: str = system_prompt
        self._history: list[dict[str, str]] = [{"role": "system", "content": system_prompt}]

    _SESSIONS: dict[str, Session] = {}

    @staticmethod
    def create(
        name: str,
        model_name_or_path: str | PathLike,
        max_new_tokens: int,
        system_prompt: str = Model._SYSTEM_PROMPT,
        temperature: float = 0.1
    ) -> Session:
        session: Session = Session.get(name)

        if session:
            return session

        session = Session(name, model_name_or_path, max_new_tokens, system_prompt, temperature)
    
        Session._SESSIONS[name] = session
        return session

    @staticmethod
    def get(name: str) -> Session | None:
        return Session._SESSIONS.get(name, None)
    
    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, system_prompt: str) -> None:
        if not system_prompt:
            system_prompt = Model._SYSTEM_PROMPT
        self._system_prompt = system_prompt
        self._history[0] = {"role": "system", "content": self._system_prompt}
    
    def prompt(self, prompt: str) -> str:
        res: str = self.model.generate_response_dynamic_max_tokens(self._history, prompt)

    # Popping the last two entries from the history (user and assistant)
        self._history.pop()  # Removes the assistant's response
        self._history.pop()  # Removes the user's prompt
        return res
    
    def prompt_with_history(self, prompt: str) -> str:
        res: str = self.model.generate_response_dynamic_max_tokens(self._history, prompt)
        
        return res

    def clear(self) -> None:
        self._history = [{"role": "system", "content": self._system_prompt}]

    @property
    def history(self) -> list[dict[str, str]]:
        return copy.deepcopy(self._history)

    def delete(self) -> None:
        del Session._SESSIONS[self.name]