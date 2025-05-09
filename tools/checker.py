import asyncio
import aiohttp
import socket
import time
from tools.ui import console

def check_proxies():
    try:
        timeout = float(input("Timeout: ") or "7")
        concurrency = int(input("Threads: ") or "100")
        recheck = input("Recheck? (y/N): ").strip().lower() == "y"
    except ValueError:
        console.print("[red]Invalid input. Using default values.[/red]")
        timeout = 7
        concurrency = 100
        recheck = False

    proxy_file = "data/working_proxies.txt" if recheck else "data/proxies.txt"

    try:
        with open(proxy_file, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print(f"[red]File not found: {proxy_file}. Please run the scraper first.[/red]")
        return

    if not proxies:
        console.print("[red]No proxies found to check.[/red]")
        return

    console.print(f"\n[bold yellow]Checking {len(proxies)} proxies with {concurrency} threads and {timeout}s timeout...[/bold yellow]")

    start_time = time.time()
    asyncio.run(check_all_proxies(proxies, timeout, concurrency))
    duration = time.time() - start_time
    console.print(f"\n[bold green]Checked {len(proxies)} proxies in {duration:.2f} seconds.[/bold green]")

async def test_proxy(session, proxy, timeout):
    proxy_url = f"http://{proxy}"
    test_url = "http://httpbin.org/ip"

    try:
        async with session.get(test_url, proxy=proxy_url, timeout=timeout) as resp:
            if resp.status == 200:
                data = await resp.json()
                ip_used = data.get("origin", "")
                console.print(f"[green]✔ Working: {proxy} [IP: {ip_used}][/green]")
                return proxy
    except (aiohttp.ClientError, asyncio.TimeoutError, socket.error):
        pass
    except Exception as e:
        console.print(f"[red]✖ Error: {proxy} — {e}[/red]")
    return None

async def check_with_semaphore(session, proxy, timeout, sem):
    async with sem:
        return await test_proxy(session, proxy, timeout)

async def check_all_proxies(proxies, timeout, concurrency):
    sem = asyncio.Semaphore(concurrency)
    valid = []

    async with aiohttp.ClientSession() as session:
        tasks = [
            check_with_semaphore(session, proxy, timeout, sem)
            for proxy in proxies
        ]
        results = await asyncio.gather(*tasks)

    valid = [p for p in results if p]

    with open("data/working_proxies.txt", "w") as f:
        for p in valid:
            f.write(p + "\n")

    console.print(f"\n[bold green]{len(valid)} working proxies saved to data/working_proxies.txt[/bold green]")

def check_proxies_from_file(file_path):
    try:
        timeout = float(input("Timeout: ") or "7")
        concurrency = int(input("Threads: ") or "100")
    except ValueError:
        console.print("[red]Invalid input. Using default values.[/red]")
        timeout = 7
        concurrency = 100

    try:
        with open(file_path, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print(f"[red]File not found: {file_path}[/red]")
        return

    if not proxies:
        console.print("[red]No proxies found in the file.[/red]")
        return

    console.print(f"\n[bold yellow]Checking {len(proxies)} proxies from {file_path}...[/bold yellow]")

    start_time = time.time()
    asyncio.run(check_all_proxies(proxies, timeout, concurrency))
    duration = time.time() - start_time
    console.print(f"\n[bold green]Checked {len(proxies)} proxies in {duration:.2f} seconds.[/bold green]")