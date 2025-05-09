import requests
from tools.ui import console

PROXY_SOURCES = [
    # HTTP/HTTPS proxy lists
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt"
]

def scrape_proxies():
    proxies = set()

    console.print("\n[bold yellow]Scraping proxies from public sources...[/bold yellow]")

    for url in PROXY_SOURCES:
        try:
            response = requests.get(url, timeout=10)
            new_proxies = response.text.strip().splitlines()
            proxies.update([p.strip() for p in new_proxies if p.strip()])
            console.print(f"[green]✔ Retrieved {len(new_proxies)} proxies from {url}[/green]")
        except Exception as e:
            console.print(f"[red]✖ Failed to fetch from {url} — {e}[/red]")

    proxies = sorted(proxies)

    if not proxies:
        console.print("[red]No proxies scraped. All sources failed.[/red]")
        return

    with open("data/proxies.txt", "w") as f:
        for proxy in proxies:
            f.write(proxy + "\n")

    console.print(f"\n[bold green]{len(proxies)} proxies saved to data/proxies.txt[/bold green]\n")