import random

class WebSearchTool:
    """
    WebSearchTool: Dummy web search integration
    In practice, this can call Google Search API or another search API
    """
    def search(self, query: str, top_k: int = 1):
        """
        Returns a dummy search result
        """
        dummy_results = [
            f"Top result for '{query}' - Example.com",
            f"Secondary result for '{query}' - Example.org"
        ]
        return random.sample(dummy_results, min(top_k, len(dummy_results)))
