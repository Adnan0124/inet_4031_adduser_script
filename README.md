# inet_4031_adduser_script

Description:


Create users.py is a python script that is desinged to create user accunts and input user infromtion the three imports called at the top of the function os, re , sys, each are pivotal os is for running system commands, re is used for regualr expressions in the case of this lab it was used for the match to check if the input line has a #. Sys is used to read the input files. # in the fucntion is used to show that the line is a comment.



Operation:


Input File specification:
Createuser is the name of the input file. 
This is the format user06:pass06:Last06:First06:group01,group02



Running the script.


This code was orignally written in python2 but was changed to python 3 by me.To run the code Sudo was used so access to my password after that it was just execute and run. Using chmod a+x create-users.py to execute. Then just run using sudo ./create-users.py < create-users.input

