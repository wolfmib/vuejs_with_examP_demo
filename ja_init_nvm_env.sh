#!/bin/bash

echo "[Jean]: Bonjour Mary, export the nvm-variable under your home for you"
echo "export NVM_DIR=\"\$HOME/.nvm\""
export NVM_DIR="$HOME/.nvm"
echo "[Jean]: Checking NVM_DIR"
echo "------------"
echo $NVM_DIR
echo "------------"
echo 


echo "[Jean]: Add nvm to bash profile"
echo "[ -s \"\$NVM_DIR/nvm.sh\" ] && . \"\$NVM_DIR/nvm.sh" 
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This lodad nvm
echo "--------------------------------"
echo 


echo "[System]: Install required node packages"
echo "          In order to create (and use) Vue efficiently, we'll need some packages installed. You can use"
echo "            - npm i -g [package]"
echo "            - npm install --global"
echo "-----------------------------------"
echo "Type global , "
read cmd_global
$cmd_global
echo "----------------------"
echo


echo
echo
echo "[System]: Now try the following command "
echo "           vue init webpack hello-vue"
read cmd_var
$cmd_var

echo "Done !"
echo