# 📘 TinyAGI/tools/wikipediaapi.py
# 🚀 Wikipedia Tool - Access and retrieve data from Wikipedia using Python!

import logging  # 📝 Standard logging for tracking tool's operations and errors
import wikipediaapi  # 📚 Library to interact with Wikipedia API
from .base_tool import BaseTool  # 🔧 Base class for all tools, enabling easy extension

# 📋 Set up logger for logging information, warnings, and errors throughout the module
logger = logging.getLogger(__name__)

class WikipediaTool(BaseTool):
    def __init__(self, config):
        """
        🌐 Initialize the WikipediaTool with a configuration dictionary.
        
        :param config: Dictionary containing tool-specific configurations (e.g., language setting).
        """
        super().__init__(config)  # 👌 Initialize BaseTool with config
        self.language = self.config.get('language', 'en')  # 🌎 Default to English ('en') if not specified
        self.wiki = wikipediaapi.Wikipedia(self.language)  # 🎯 Set up Wikipedia instance with chosen language
        logger.info(f"WikipediaTool initialized with language: {self.language}")  # 🔍 Log tool's language

    def search(self, query, results=5):
        """
        🔍 Search Wikipedia for a specified query and return the top results.
        
        :param query: The search query string 🕵️‍♂️.
        :param results: Number of search results to return (default: 5) 📊.
        :return: List of page titles matching the query (limited by 'results').
        """
        try:
            logger.info(f"Searching Wikipedia for query: '{query}' with {results} results.")  # 🔍 Log the search
            search_results = self.wiki.search(query, results=results)  # 📚 Retrieve search results
            logger.info(f"Found {len(search_results)} results.")  # 📊 Log number of results found
            return search_results  # ✅ Return the list of page titles
        except Exception as e:
            logger.error(f"Error during Wikipedia search: {e}")  # ❗ Log any errors encountered
            return []  # 🛑 Return an empty list if there's an error

    def get_page_summary(self, title, sentences=3):
        """
        📜 Get a summary of a Wikipedia page by title. 
        If the exact page is missing, search and fetch the summary for the closest match.

        :param title: Title of the Wikipedia page 🏷️.
        :param sentences: Number of sentences for the summary (default: 3) 📝.
        :return: Summary string or error message if the page isn't found.
        """
        try:
            if not title.strip():
                logger.error("Empty title provided for fetching summary.")  # 🛑 Log error if title is empty
                return "No title provided for fetching summary."

            logger.info(f"Fetching summary for Wikipedia page: '{title}'.")  # 🔍 Log the title being fetched
            page = self.wiki.page(title)  # 🔗 Access page by title
            if page.exists():  # 🌟 Check if the page exists
                summary = page.summary  # 📝 Get page summary
                logger.info("Fetched summary successfully.")  # ✅ Log successful summary fetch
                return summary  # 📜 Return summary
            else:
                logger.warning(f"Page '{title}' does not exist. Performing a search.")  # ⚠️ Log if page not found
                search_results = self.search(title, results=1)  # 🔄 Search for similar page title
                if search_results:
                    first_result = search_results[0]  # 🥇 Get the first result from search
                    page = self.wiki.page(first_result)  # 🔗 Access page by the first search result
                    if page.exists():  # 🎉 Check if the fallback page exists
                        summary = page.summary  # 📝 Fetch its summary
                        logger.info(f"Fetched summary for '{first_result}' successfully.")  # ✅ Log successful fetch
                        return summary  # 📜 Return summary for the best match
                    else:
                        logger.error(f"Page '{first_result}' does not exist.")  # ❌ Log if page doesn't exist
                        return f"No Wikipedia page found for '{title}'."
                else:
                    logger.error(f"No search results found for query '{title}'.")  # ❌ Log lack of search results
                    return f"No Wikipedia page found for '{title}'."
        except Exception as e:
            logger.error(f"Unexpected error fetching page summary: {e}", exc_info=True)  # ⚠️ Log unexpected errors
            return ""  # 🛑 Return an empty string if an error occurs

