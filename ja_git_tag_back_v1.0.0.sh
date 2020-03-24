#!/bin/bash
# Author: Mary
# Version : v1.0.0
# ---------------------
# Support display current tag
# Support tag option and push back to current branch
# ------------------------



# [Jean]
# Version: v2  
# sh->bash function
# add tagging information with commit message

# ja_git_push_bafck_v2
    # ja_git_push_back_v2 $input_tag $input_name $time_str $input_reason
    #                         $1         $2          $3        $4
#########################################################
ja_git_push_back_v2 (){
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
    echo "----------------------------------------------------------------"
    echo "[JA]: in branch: \"$ja_branch\""
    echo -n "[JA]: This script will push back your code to git are yo sure to do it ?  "
    read nothing

    echo "[JA]: Start git add process"
    git add .
    echo "[JA]: Finish git add"
    echo "----------------------------------------------------------"

    # [Mary]: Add tag information as following format
        # [tag: v1.0.0]: add_brabrabra_file_delete_brabrabra_files..
        # [tag: $1]: $ja_commit
    ja_commit_for_tag_action="\"tag_${1}_${2}_${4}_${3}\""
    echo "[JA]: your commit become ->  $ja_commit_for_tag_action"

    echo "[JA]: Start commit.."
    git commit -m $ja_commit_for_tag_action
    echo

    echo "[JA]: Start to push back to $ja_branch"
    git push origin $ja_branch
    echo
    echo "[JA]: End the ja_git_push_back.sh"
    echo
}
#########################################################


# git_push_tag
    # git tag -a  'v1.0.0' 'f0710072eb5be339c79f7238ad672b45c962ac72' -m "initial_v1.0.0"
    #                $1                $2                                     $1_msg
#########################################################
git_force_push_origin_tag(){

    echo $1 # tag
    echo $2
    echo "---------"
    echo 

    commit_msg="\"Force_Taging_${1}\""
    git tag -f -a $1 $2 -m $commit_msg 
    echo 
    echo "------"
    git tag
    echo "------"
    echo 
    
    #echo $2 # sha
    #echo $3 # commit
    git push -f origin $1 
}
#########################################################



###################################################################################
echo "[System]: checking..current tag "
echo "---------------------------------------------"
git tag
echo "---------------------------------------------"

echo "[Mary]: I am gonna tag back(force updated if the same tag is being used in remote side) !!"
echo "choose the tag name or create new one by add 1  or... quit by Crtl+C "
echo "e.g:  v1.0.0 -> v1.0.1 , type v1.0.1"
read input_tag
echo


echo "[Mary]: Before taging ... I need to commit all your stuff back to this branch first"
echo "        Are you ready for git push back to origin:YOUR_CURRENT_BRANCH ?"
read nothing
echo

# Checking the last commit process
echo "Enter Name: Mary"
read input_name
echo

echo "Enter Date: 2020_02_22 "
read time_str
echo

echo "Enter Reason: (short words..) like, finish branch, or implement some function ..etc.."
read input_reason




# [Mary]: Add tag information as following format
    # [tag: v1.0.0]: add_brabrabra_file_delete_brabrabra_files..
    # [tag: $1]: $ja_commit
echo "######################################################"
ja_git_push_back_v2 $input_tag $input_name $time_str $input_reason
echo "######################################################"
echo "######################################################"
echo
echo


echo "--------"
git log -n 1
echo "--------"
echo "[Mary]: type the latest sha to attached your tag"
read my_sha
echo "-------"
echo $my_sha
echo "-------"


# Push tag back format:
    # git push -f origin v1.0.0
git_force_push_origin_tag $input_tag $my_sha

# git tag -a  'v1.0.0' 'f0710072eb5be339c79f7238ad672b45c962ac72' -m "initial_v1.0.0"
    # $1 = 'v1.0.0'
    # $2 = sha
    # $3 = commit_msg
echo "Done...."
echo "---------------"
git log -n 2 --pretty=oneline
echo "----------------"
echo











