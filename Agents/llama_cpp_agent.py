# TinyAGI/agents/llama_cpp_agent.py

import logging
from llama_cpp import Llama
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

class LlamaCppAgent(BaseAgent):
    def __init__(self, model_config, module_manager=None):
        super().__init__(model_config)
        model_path = self.parameters.get('model_path', '')
        if not model_path:
            logger.error("Model path not provided for LlamaCppAgent.")
            raise ValueError("Model path is required for LlamaCppAgent.")
        self.model = Llama(model_path=model_path)
        logger.info(f"LlamaCppAgent initialized with model at: {model_path}")

    def generate_text(self, prompt, stream=False):
        try:
            output = self.model(prompt, max_tokens=self.parameters.get('max_tokens', 150), stream=stream)
            if stream:
                return (chunk['choices'][0]['text'] for chunk in output)
            else:
                text = output['choices'][0]['text']
                return text
        except Exception as e:
            logger.error(f"Error generating text with LlamaCpp: {e}")
            return None

    def embed(self, input_data):
        logger.warning("Embedding is not implemented for LlamaCppAgent.")
        return []
