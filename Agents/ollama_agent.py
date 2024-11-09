# TinyAGI/agents/ollama_agent.py

import logging
import ollama
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

class OllamaAgent(BaseAgent):
    def __init__(self, model_config, module_manager):
        super().__init__(model_config)
        self.model_name = self.model_config.get('name', 'llama3.2:1b')
        self.host = self.parameters.get('host', 'http://localhost:11434')
        self.client = ollama.Client(host=self.host)
        logger.info(f"OllamaAgent initialized with model: {self.model_name} at host: {self.host}")

    def generate_text(self, prompt, stream=False):
        try:
            if stream:
                response_stream = self.client.generate(
                    model=self.model_name,
                    prompt=prompt,
                    stream=True
                )
                return (chunk.get('response', '') for chunk in response_stream)
            else:
                response = self.client.generate(
                    model=self.model_name,
                    prompt=prompt
                )
                content = response.get('response', '')
                return content
        except ollama.ResponseError as e:
            logger.error(f"Ollama ResponseError: {e.error} (Status Code: {e.status_code})")
            return None

    def embed(self, input_data):
        logger.warning("Embedding is not implemented for OllamaAgent.")
        return []
