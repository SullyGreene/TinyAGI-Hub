# TinyAGI/plugins/generate_references.py

import logging
from .base_plugin import BasePlugin

logger = logging.getLogger(__name__)

class GenerateReferences(BasePlugin):
    def __init__(self, config):
        super().__init__(config)
        # Initialize any additional configurations if necessary

    def execute(self, agent, tool, input_data, options, stream=False):
        """
        Extract references from the provided text.

        :param agent: Instance of a model agent.
        :param tool: Instance of a tool (if any).
        :param input_data: Dictionary containing the text.
        :param options: Dictionary containing additional options.
        :param stream: Boolean indicating whether to handle streaming responses.
        :return: List of references.
        """
        text = input_data.get('text', '')
        if not text:
            logger.error("No text provided for extracting references.")
            return []

        # Example logic: Extract references based on a pattern (e.g., numbered list)
        references = []
        try:
            lines = text.split('\n')
            for line in lines:
                if line.strip().startswith(tuple(str(i) + '.' for i in range(1, 100))):
                    parts = line.split('.', 1)
                    if len(parts) == 2:
                        ref_id = parts[0].strip()
                        ref_source = parts[1].strip()
                        references.append({"id": ref_id, "source": ref_source})
            logger.info("Extracted references using GenerateReferences plugin.")
            return references
        except Exception as e:
            logger.error(f"Error extracting references: {e}")
            return []
