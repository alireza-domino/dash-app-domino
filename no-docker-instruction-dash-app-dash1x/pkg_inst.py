import subprocess
 
def index():
    subprocess.call("sudo pip install -r requirements_apps.txt", shell=True)
 
index()