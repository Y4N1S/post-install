import os

def commandebash (commande):
    os.system(commande)

commandebash("echo 'UBUNTU POST-INSTALL SCRIPT' > log.txt")



commandebash("echo 'mise a jour de apt et apt-get' >> log.txt")

commandebash("echo 'sudo apt update && sudo apt upgrade")

commandebash("echo 'sudo apt-get update && sudo apt-get upgrade' >> log.txt")

commandebash("echo 'Installation de git curl et python' >> log.txt")

commandebash("echo 'apt-get install --yes git git-extras build-essential python3-pip htop glances'>> log.txt")

commandebash("echo 'sudo snap install discord'>> log.txt ")

commandebash("echo 'sudo snap install code --classic'>>log.txt")