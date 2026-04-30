import time
from colorama import Fore
from .base_agent import BaseAgent

class SearchAgent(BaseAgent):
    def execute(self, query: str) -> str:
        print(f"\n{Fore.BLUE}[{self.name}] Fetching external context for: {query}...{Fore.RESET}")
        time.sleep(2)
        print(f"{Fore.BLUE}[{self.name}] Context retrieved: Found 3 relevant specifications.{Fore.RESET}")
        return "PostgreSQL v3 spec data"