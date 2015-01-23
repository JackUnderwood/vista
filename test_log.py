__author__ = 'John Underwood'
import logging

from colorama import init, Fore, Back, Style


init()

# logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
logging.debug(Fore.GREEN + 'This is a DEBUG message' + Fore.RESET)
logging.info(Fore.CYAN + 'This is an INFORMATION message' + Fore.RESET)
logging.warning(Fore.YELLOW + 'This is a WARNING!' + Fore.RESET)
logging.error(Fore.RED + 'This is an ERROR!' + Fore.RESET)
logging.critical(Fore.WHITE + Back.RED + 'This is CRITICAL!' +
                 Fore.RESET + Back.RESET)
logging.debug(Fore.GREEN + 'This is a DEBUG message' + Fore.RESET)

