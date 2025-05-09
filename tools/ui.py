from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_banner():
    banner = r"""
 ________  ________  ________     ___    ___ ___    ___ 
|\   __  \|\   __  \|\   __  \   |\  \  /  /|\  \  /  /|
\ \  \|\  \ \  \|\  \ \  \|\  \  \ \  \/  / | \  \/  / /
 \ \   ____\ \   _  _\ \  \\\  \  \ \    / / \ \    / / 
  \ \  \___|\ \  \\  \\ \  \\\  \  /     \/   \/  /  /  
   \ \__\    \ \__\\ _\\ \_______\/  /\   \ __/  / /    
    \|__|     \|__|\|__|\|_______/__/ /\ __\\___/ /     
                                 |__|/ \|__\|___|/      
    """
    console.print(Panel(banner, style="bold cyan", expand=False))


def print_menu():
    console.print("\n[bold magenta]Select an option:[/bold magenta]")
    console.print("[1] Scrape Proxies")
    console.print("[2] Check Proxies")
    console.print("[3] Quit")
    console.print("[4] Check Proxies From File (util/proxies.txt)\n")
