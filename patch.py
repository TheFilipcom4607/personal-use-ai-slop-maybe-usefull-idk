import requests
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════╗")
    print(f"{Fore.CYAN}{Style.BRIGHT}║        SkyStats Limit Patcher        ║")
    print(f"{Fore.CYAN}{Style.BRIGHT}╚══════════════════════════════════════╝\n")

    print(f"{Fore.WHITE}This script updates your SkyStats interesting aircraft limit to bigger numbers then the GUI allows.")
    print(f"{Fore.WHITE}Default feeder address is {Fore.YELLOW}adsb-feeder.local:5173\n")

    raw = input(f"{Fore.CYAN}Enter your feeder URL {Fore.WHITE}[press Enter for default]: {Style.RESET_ALL}").strip()

    if not raw:
        base_url = "http://adsb-feeder.local:5173"
        print(f"{Fore.YELLOW}Using default: {base_url}")
    else:
        if not raw.startswith("http"):
            raw = "http://" + raw
        base_url = raw.rstrip("/")
        print(f"{Fore.YELLOW}Using: {base_url}")

    raw_limit = input(f"\n{Fore.CYAN}Enter the limit {Fore.WHITE}[press Enter for default 9999]: {Style.RESET_ALL}").strip()

    if not raw_limit:
        limit = 9999
        print(f"{Fore.YELLOW}Using default limit: {limit}")
    else:
        try:
            limit = int(raw_limit)
            print(f"{Fore.YELLOW}Using limit: {limit}")
        except ValueError:
            print(f"{Fore.RED}Invalid number, using default: 9999")
            limit = 9999

    print(f"\n{Fore.WHITE}Sending request...")

    payload = {
        "route_table_limit": "5",
        "interesting_table_limit": str(limit),
        "record_holder_table_limit": "5",
        "disable_planealertdb_tags": "false"
    }

    try:
        response = requests.put(f"{base_url}/api/settings", json=payload)

        if response.ok:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ Success! {Fore.WHITE}Your backend will now return up to {limit} interesting aircraft.")
        else:
            print(f"\n{Fore.RED}{Style.BRIGHT}✗ Request failed. {Fore.WHITE}Status: {response.status_code}")
            print(f"{Fore.RED}{response.text}")

    except requests.exceptions.ConnectionError:
        print(f"\n{Fore.RED}{Style.BRIGHT}✗ Could not connect. {Fore.WHITE}Check that your feeder is reachable at {Fore.YELLOW}{base_url}")
    except Exception as e:
        print(f"\n{Fore.RED}{Style.BRIGHT}✗ Unexpected error: {Fore.WHITE}{e}")

    print()

if __name__ == "__main__":
    main()
