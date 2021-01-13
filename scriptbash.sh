#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT"

echo "Updating APT..."

sudo apt-get update 

clear

echo "Installing base packages"

sudo apt-get install --yes git git-extras build-essential python3-pip htop glances


sudo snap install discord # sudo = superutilisateur snap commande va chercher dans le store ubuntu equivau a apt-get


sudo snap install code --classic #utre maniere vs code


# wget https://go.microsoft.com/fwlink/?LinkID=760868 -O vscode.deb   #relis au liens de dl

# sudo dpkg -i ./vscode.deb   #importe paquet

# sudo apt-get install -f   #install
