#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT" > log.txt

echo "Updating APT..." >> log.txt
# sudo = super utilisateur //   apt-get update permet de mettre a jour
sudo apt update && sudo apt upgrade && sudo apt-get upgrade && sudo apt-get update 

# clear permet d'effacer les commandes dans le terminal 

clear      


# echo est un équivalent de print en python3

echo "Installing base packages" >>log.txt  

sudo apt-get install --yes git git-extras build-essential python3-pip htop glances git python3.6 curl 

echo "Installing Discord" >> log.txt

#commande snap permet d'installer des logiciels depuis le store ubuntu

sudo snap install discord 

echo "Installing Vscode"   >> log.txt

sudo snap install code --classic 


                                                ###### AUTRE MANIERE POUR VSCODE ######

# wget https://go.microsoft.com/fwlink/?LinkID=760868 -O vscode.deb  

# sudo dpkg -i ./vscode.deb   

# sudo apt-get install -f   
