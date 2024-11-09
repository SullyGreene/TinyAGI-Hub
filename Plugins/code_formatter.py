# TinyAGI/plugins/code_formatter.py

import logging
from .base_plugin import BasePlugin

logger = logging.getLogger(__name__)

class CodeFormatter(BasePlugin):
    def __init__(self, config):
        super().__init__(config)
        self.languages = self.config.get('languages', [])
        self.style = self.config.get('style', 'default')

    def execute(self, agent, tool, input_data, options, stream=False):
        code = input_data.get('code', '')
        language = input_data.get('language', 'python')
        formatted_code = self.format_code(code, language)
        logger.info("Formatted code using CodeFormatter plugin.")
        return formatted_code

    def format_code(self, code, language):
        if language.lower() == 'python':
            try:
                import black
                formatted_code = black.format_str(code, mode=black.FileMode())
                return formatted_code
            except ImportError:
                logger.warning("Black formatter is not installed.")
                return code
            except Exception as e:
                logger.error(f"Error formatting code: {e}")
                return code
        else:
            logger.warning(f"No formatter implemented for language: {language}")
            return code
