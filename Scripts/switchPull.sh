#!/bin/bash

# banner
echo "[+] Launching switch pull Script!"

# prompt user for ip
printf "IP: "
read ip

# prompt user for usernmae
printf "Username: "
read username

# prompt user for password
#printf "Password: "
#read -s password

# ssh into switch using sshpass
# sshpass -p $password ssh -o StrictHostKeyChecking=no $username@$ip > sshLog.txt
ssh -l $username <IP>

