import time
from colorama import init, Fore, Style
from core.orchestrator import Orchestrator
from agents.search_agent import SearchAgent
from agents.dev_agent import DevAgent
from agents.review_agent import ReviewAgent

# 初始化终端颜色
init(autoreset=True)

def run_demo():
    print(Fore.YELLOW + "="*60)
    print(Fore.YELLOW + " MimoAgent-Flow: Complex Task Simulation Initialize ")
    print(Fore.YELLOW + "="*60 + "\n")

    user_requirement = "Build a high-performance PostgreSQL reverse proxy middleware with Auth."
    print(f"{Fore.WHITE}[User Input] {user_requirement}\n")
    
    # 1. 任务拆解
    orchestrator = Orchestrator()
    tasks = orchestrator.decompose_task(user_requirement)
    
    # 2. 初始化 Agents
    searcher = SearchAgent("Knowledge-Searcher")
    developer = DevAgent("Code-Generator")
    reviewer = ReviewAgent("Security-Reviewer")
    
    print(f"\n{Fore.MAGENTA}>>> Multi-Agent Collaboration Chain Started <<<{Fore.RESET}")
    time.sleep(1)
    
    # 3. 链式执行
    context = searcher.execute("PostgreSQL Wire Protocol V3 and Auth standards")
    code_result = developer.execute("Proxy async loop logic based on context", context)
    passed = reviewer.execute(code_result)
    
    if passed:
        print(f"\n{Fore.GREEN}[Pipeline Success] Workflow finished. Artifacts ready for deployment.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}[Pipeline Failed] Iteration limit reached.{Style.RESET_ALL}")
    
    print("\n" + Fore.YELLOW + "="*60)

if __name__ == "__main__":
    run_demo()