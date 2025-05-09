from tools.scraper import scrape_proxies
from tools.checker import check_proxies, check_proxies_from_file
from tools.ui import print_banner, print_menu

def main():
    last_action = None

    while True:
        print_banner()
        print_menu()
        if last_action:
            print(f"\nLast action: {last_action}")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            scrape_proxies()
            last_action = "Scraped proxies"
        elif choice == '2':
            check_proxies()
            last_action = "Checked scraped proxies"
        elif choice == '3':
            print("Goodbye!")
            break
        elif choice == '4':
            check_proxies_from_file("util/proxies.txt")
            last_action = "Checked from util/proxies.txt"
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()