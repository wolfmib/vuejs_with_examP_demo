#!/bin/bash

delete_branch () {
    # $1 branch_name
    git branch -d $1
}


echo "[Jean]: Bonjour, chosir une branch pour supprimer"
echo
echo "--------------------------"
git branch
echo "--------------------------"

read branch_name

echo 
echo "[Jean]: Preparer pour supprimer $branch_name , T'as sure ??"
echo "        Appuyez sur Entrée"
read nothing

echo "[Jean]: Run: --------------------------------- "
echo "             git branch -d $branch_name"
echo "----------------------------------------------"
echo
delete_branch $branch_name
echo
echo "[Jean]: Fini !  Voilla"
echo 
echo "-----------------------"
git branch
echo "-----------------------"

