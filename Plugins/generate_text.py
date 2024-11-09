# TinyAGI/plugins/generate_text.py

import logging
from .base_plugin import BasePlugin

logger = logging.getLogger(__name__)

class GenerateText(BasePlugin):
    def __init__(self, config):
        super().__init__(config)
        self.prompt_template = self.config.get('prompt_template', "{prompt}")

    def execute(self, agent, tool, input_data, options, stream=False):
        """
        Generate text based on the provided prompt, optionally using a tool.

        :param agent: Instance of a model agent.
        :param tool: Instance of a tool (e.g., WikipediaTool).
        :param input_data: Dictionary containing the prompt.
        :param options: Dictionary containing additional options.
        :param stream: Boolean indicating whether to handle streaming responses.
        :return: Generated text.
        """
        prompt = self.prompt_template.format(prompt=input_data.get('prompt', ''))
        
        if not prompt.strip():
            logger.error("No prompt provided for GenerateText plugin.")
            return "No prompt provided."

        # Optionally use the tool to enhance the prompt or fetch additional data
        if tool:
            additional_info = tool.get_page_summary(prompt)
            if additional_info:
                prompt += f"\n\nAdditional Information:\n{additional_info}"

        response = agent.generate_text(prompt, stream=stream)
        logger.info("Generated text using GenerateText plugin.")
        return response
