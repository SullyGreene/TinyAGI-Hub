# TinyAGI/plugins/generate_tags.py

import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from .base_plugin import BasePlugin

logger = logging.getLogger(__name__)

class GenerateTags(BasePlugin):
    def __init__(self, config):
        super().__init__(config)
        self.stopwords = set(stopwords.words('english'))
        self.max_tags = self.config.get('max_tags', 10)

    def execute(self, agent, tool, input_data, options, stream=False):
        text = input_data.get('text', '')
        try:
            tokens = word_tokenize(text)
            filtered_tokens = [word.lower() for word in tokens if word.lower() not in self.stopwords and word.isalpha()]
            freq_dist = nltk.FreqDist(filtered_tokens)
            tags = [word for word, freq in freq_dist.most_common(self.max_tags)]
            logger.info("Generated tags using GenerateTags plugin.")
            return tags
        except Exception as e:
            logger.error(f"Error generating tags: {e}")
            return []
