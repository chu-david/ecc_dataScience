import sys
import subprocess

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', '<packagename>'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'seaborn'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn'])