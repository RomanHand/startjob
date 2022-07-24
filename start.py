import os
import shutil

os.system('apt update')
os.system('apt upgrade -y')


os.system('cd /usr/bin')
my_file = open("update", "w")
my_file.write("#!/usr/bin/python3 \n"
              "import os \n \n"
              "os.system('apt update') \n"
              "os.system('apt upgrade -y') ")
my_file.close()
shutil.move("update", "/usr/bin")
os.system('chmod ugo+x /usr/bin/update')
os.system('apt install htop net-tools lm-sensors openssh-server -y ')