import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

argtwo = sys.argv[1]

cprint(figlet_format(argtwo, font='speed'))
       
