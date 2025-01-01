# MIT License
# Copyright (c) 2024 Sully Greene
# Repository: https://github.com/SullyGreene
# Profile: https://x.com/@SullyGreene

# TinyAGI/agents/meta_ai_agent.py

import logging
from meta_ai_api import MetaAI
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

class MetaAIAgent(BaseAgent):
    def __init__(self, model_config, module_manager=None):
        """
        Initialize the MetaAI Agent.
        
        :param model_config: Dictionary containing model configuration parameters.
        :param module_manager: Optional module manager for additional functionalities.
        """
        super().__init__(model_config)
        self.meta_ai = MetaAI()
        logger.info("MetaAIAgent initialized successfully.")

    def generate_text(self, prompt, stream=False):
        """
        Generate text using the MetaAI model.

        :param prompt: The prompt string to send to the model.
        :param stream: Boolean indicating whether to stream responses.
        :return: Generated text or a generator for streaming.
        """
        try:
            if stream:
                response_stream = self.meta_ai.prompt(message=prompt, stream=True)
                return (chunk.get('message', '') for chunk in response_stream)
            else:
                response = self.meta_ai.prompt(message=prompt)
                content = response.get('message', 'No response received.')
                return content
        except Exception as e:
            logger.error(f"Error in MetaAIAgent.generate_text: {e}")
            return None

    def embed(self, input_data):
        """
        Generate embeddings using the MetaAI model.

        :param input_data: String or list of strings to embed.
        :return: Embedding vector(s).
        """
        logger.warning("Embedding is not explicitly supported for MetaAI.")
        return []


# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
