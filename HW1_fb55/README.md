# PUI 2017 HW 1

**On NYU classes please turn in your github account name where the repositories you will create in this and the following homework sets will be hosted.**

## Reading:

[What is the question? Jeff Leek & Roger D. Peng](https://www.d.umn.edu/~kgilbert/ened5560-1/The%20Research%20Question-2015-Leek-1314-5.pdf)

## Assignment 1: Finish Lab 1

Finish the lab started in the first lab session:
https://github.com/fedhere/PUI2017_fb55/Lab1_fb55

If you were able to follow along you should have a repository set up on your local machine as well as on your github account named gittest_\<your net id\>, with a single file in it named myfirstfle.txt, and you should have a resolved merge conflict. Because your repo is public we can access it, and see the history of your file, and the conflict in it. If you fell behind, please take yourself to this point, and feel free to work with others, but remember that it is your responsibility to learn, and be able to reproduce by yourself the work that you do in groups. 


GRADING: 

On your github account we must be able to see :
- your own repo, and in its history we need to see the merge. 
- your fork of your class mate repo and the changes you made to their file in its history
On your classmate repo we need to see your merge request.

## Assignment 2: Set up your environment:

follow the instructions in [HW1_2_instructions.md](https://github.com/fedhere/PUI2017_fb55/blob/master/HW1_fb55/HW1_2_instructions.md)

GRADING: 

We will grade you based on the README file you create in the github directory as described above. The screen shots need to show the appropriate lines in the .bashrc/.bash_profile, and that running the commands takes you to the right directory.

## Assignment 3:  Reproducible research.

**EXTRA CREDIT**

This may be hard, but figuring it out will greatly help you get the most out of the next several lectures. We keep track of your EC assignments and they will help your final grade. This homework is a notebook: this is the standard format of the homeworks in the future. To get full points your notebook must

- be rendered (e.g. plots must be visible) so that we see what you intended to turn in

- run: the TA must be able to download your notebook and run it without error. 

Create a notebook of your own following the steps outlined in [this notebook](https://github.com/fedhere/PUI2017_fb55/blob/master/HW1_fb55/HW1_3_instructions.ipynb)

To get the scheleton notebook you can clone my repository, fork my repository, or do it manually as follows:

1) On the terminal (bash shell) go to the PUI2017_<NYUid> directory you created in Assignment 2 and set up as a repo in the lab/Assignment 1.

2) Download the notebook I created (link above). To do so **click on Raw** next to the notebook. 
Now you have 2 choices: you can copy and paste the RAW ipython notebook (which is  a JSON file) onto a new file on your own machine (name the file HW1_reproducible_distributions.ipynb) or you can use the wget command on the terminal: typing 
```
wget https://raw.githubusercontent.com/fedhere/PUI2016_fb55/master/HW1_fb55/HW1_3_fb55.ipynb?token=ABnkhiKFUXlZp9NtNLMICRtVcjW0qRA0ks5Zwdl-wA%3D%3D
```
will save a version of the notebook in the directory where you were when you typed the command. **wget**, which stands for web get, downloads any files, or even entire directories, from a web URL.

3) Fill in the code cells that I left empty following the directions.

4) Once the notebook is done and rendered (you see the plots at the end of it) “stage it” so that git can track it (hint: follow the procedure in the lab assignment and use git add and git commit)

5) link the current directory to your new github repo which you created in assignment 2 (PUI2015_<firstinitialandlastname> on your github account). (hint: just like in the lab assignment use git remote add origin and git push -u as in the image on the right, but using the URL of your new repo of course)

6) push the notebook into the github repo and check that it renders ok. remember to check that it runs ok as well: before you commit open a new instance of ipython notebook (or restart your kernel!) and go through the notebook cell by cell to assure that there are no problems








## References:

markdown syntax - http://daringfireball.net/projects/markdown/syntax

basic bash commands - http://www.tldp.org/LDP/abs/html/basic.html

environment setup - http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html#sect_03_01_02

additional references were provided in the class slides.

**Text Editors.**

-m

remember to add the -m “my commit message” when you commit to github, otherwise github will automatically open a text editor for you to type your message in , and then you have to deal with it. If github opened a text editor it is either emacs or vi, depending on your setup. If you are using emacs or vi, either because github opened them or to edit files, this is how you save your work and exit:


*emacs* 

Save: Ctrl+x Ctrl+s

Exit: Ctrl+x Ctrl+c

(if your emacs is running on the terminal you have to use these shortcuts, if it is running in its own X window you can use the dropdown menu)


*vi*

Save: esc :w

Exit: esc :q


## Key Concepts:

falsifiability and law of parsimony

types of scientific questions

reproducible research

PEP8 and style standards 

work with github 

basic bash commands

understand how to setup your environment

creating and checking into github an ipython notebook

