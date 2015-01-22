__author__ = 'John Underwood'
import logging
from colorama import init
from colorama import Fore
from colorama import Back


init()

# logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
logging.debug(Fore.GREEN + 'This is a DEBUG message' + Fore.RESET)
logging.info(Fore.CYAN + 'This is an INFORMATION message' + Fore.RESET)
logging.warning(Fore.YELLOW + 'This is a WARNING!' + Fore.RESET)
logging.error(Fore.RED + 'This is an ERROR!' + Fore.RESET)
logging.critical(Fore.RED + Back.YELLOW + 'This is CRITICAL!' + Fore.RESET +
                 Back.RESET)
logging.debug(Fore.GREEN + 'This is a DEBUG message' + Fore.RESET)
# print(Fore.RESET + "")

# print(Fore.WHITE + "")

