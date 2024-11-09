# TinyAGI/agents/openai_agent.py

import logging
import openai
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class OpenAIAgent(BaseAgent):
    def __init__(self, model_config, module_manager=None):
        super().__init__(model_config)
        openai.api_key = os.getenv('OPENAI_API_KEY', '')
        if not openai.api_key:
            logger.error("OpenAI API key not provided.")
            raise ValueError("OpenAI API key is required.")
        self.model_name = self.model_config.get('name', 'gpt-3.5-turbo')
        self.model_type = self.model_config.get('type', 'chat')
        logger.info(f"OpenAIAgent initialized with model: {self.model_name}")

    def generate_text(self, prompt, stream=False):
        try:
            if self.model_type == 'chat':
                messages = [{"role": "user", "content": prompt}]
                response = openai.ChatCompletion.create(
                    model=self.model_name,
                    messages=messages,
                    temperature=self.parameters.get('temperature', 0.7),
                    max_tokens=self.parameters.get('max_tokens', 150),
                    stream=stream
                )
                if stream:
                    return (chunk.choices[0].delta.get('content', '') for chunk in response)
                else:
                    content = response.choices[0].message['content']
                    return content
            else:
                response = openai.Completion.create(
                    model=self.model_name,
                    prompt=prompt,
                    temperature=self.parameters.get('temperature', 0.7),
                    max_tokens=self.parameters.get('max_tokens', 150),
                    stream=stream
                )
                if stream:
                    return (chunk.choices[0].text for chunk in response)
                else:
                    text = response.choices[0].text
                    return text
        except Exception as e:
            logger.error(f"Error generating text with OpenAI: {e}")
            return None

    def embed(self, input_data):
        try:
            response = openai.Embedding.create(
                input=input_data,
                model=self.model_config.get('embedding_model', 'text-embedding-ada-002')
            )
            embeddings = [datum['embedding'] for datum in response['data']]
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings with OpenAI: {e}")
            return []
