import sys
import subprocess as sp
import pkg_resources
import art

# Check if the user has the required packages installed
required = {'progressbar', 'playsound'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# If the user is missing any of the required packages, install them
if missing:
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    sp.call("cls", shell=True)
    print("Dependencies installed")


def intro():
    sp.call("cls", shell=True)
    print("nah no way")
    print(art.intro_name)

intro()