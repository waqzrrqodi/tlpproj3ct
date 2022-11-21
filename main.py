import sys
import time
import subprocess as sp
import pkg_resources
import ui_elements

# Check if the user has the required packages installed
required = {'progressbar', 'playsound'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# If the user is missing any of the required packages, install them
if missing:
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    sp.call("cls", shell=True)
    print("Dependencies installed")

# Makes text appear one letter at a time
def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def intro():
    sp.call("cls", shell=True)
    print("nah no way")
    print(ui_elements.intro_name)

def main():
    intro()
    
if __name__ == "__main__":
    main()

animate_text("Hello world")