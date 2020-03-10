#!/bin/bash

#History:
#v1: first version of geting the correct branch
#v2: fix the bug, if the current git-language is french..


#Set to English
alias git='LANG=en_GB git'


#v1: add the automatically get the local branch name
git status


#Parceque: On branch tutorial_quiz_with_api_example
#N=        1    2              3
#[Jean]: On utiliser la N=3
N=3

#Obtenir la status de git
ja_git_status=$(git status)
echo $ja_git_status
#Utiliser the method pour obtenir le nom de branch
ja_branch=$(echo $ja_git_status | cut -d " " -f $N)

#Normal Information
echo "---"
echo "[JA]: in branch: \"$ja_branch\""
echo -n "[JA]: This script will push back your code to git are yo sure to do it ?  "
read nothing

echo "[JA]: Start git add process"
git add .
echo "[JA]: Finish git add"
echo

echo -n  "[JA]: Prepare for commit, please enter the commit message:   "
read ja_commit
echo "[JA]: your commit is $ja_commit"

echo "[JA]: Start commit.."
git commit -m $ja_commit
echo

echo "[JA]: Start to push back to $ja_branch"
git push origin $ja_branch
echo
echo "[JA]: End the ja_git_push_back.sh"
echo
