# TinyAGI/plugins/generate_summary.py

import logging
from .base_plugin import BasePlugin

logger = logging.getLogger(__name__)

class GenerateSummary(BasePlugin):
    def __init__(self, config):
        super().__init__(config)
        self.prompt_template = self.config.get('prompt_template', "Provide a concise summary of the following text:\n{text}")

    def execute(self, agent, tool, input_data, options, stream=False):
        text = input_data.get('text', '')
        prompt = self.prompt_template.format(text=text)
        response = agent.generate_text(prompt, stream=stream)
        logger.info("Generated summary using GenerateSummary plugin.")
        return response
