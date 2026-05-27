from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage
from langchain_core.outputs import ChatGeneration, ChatResult


class LangChainModelAdapter(BaseChatModel):
    """
    Wraps the project's existing Model abstraction
    so it can be used inside LangChain chains.
    """

    def __init__(self, model):
        super().__init__()
        self._model = model

    @property
    def _llm_type(self) -> str:
        return "custom-project-model"

    def _generate(self, messages, stop=None, **kwargs) -> ChatResult:
        # Convert LangChain messages to the history format expected by Model
        # The Model expects a history list of dicts: [{"role": "...", "content": "..."}]
        # and a separate prompt string.
        
        # We'll treat the last message as the prompt and the rest as history.
        history = []
        prompt = ""
        
        if messages:
            for m in messages[:-1]:
                role = "user" if isinstance(m, HumanMessage) else "assistant"
                history.append({"role": role, "content": m.content})
            
            last_msg = messages[-1]
            if isinstance(last_msg, HumanMessage):
                prompt = last_msg.content
            else:
                # Fallback if the last message isn't human
                # (though LangChain usually ends with HumanMessage for generation)
                prompt = last_msg.content

        # Call the underlying model
        # Note: get_response modifies history in-place, but we passed a fresh list
        response_text = self._model.get_response(history, prompt)

        generation = ChatGeneration(
            message=HumanMessage(content=response_text)
        )
        return ChatResult(generations=[generation])
