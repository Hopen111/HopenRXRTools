input("Press Enter To Begin Uninstallation." )
import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'pillow'])