# PUI 2018 HW 2

**On NYU classes please turn in your github account name where the repositories you will create in this and the following homework sets will be hosted.**
You may want to clone my PUI2018_fb55 repository on your machine to get the updates and gthen git pull from it every week, aor "watch" it.

## HW1

Finish the lab started in the first lab session:
https://github.com/fedhere/PUI2018_fb55/Lab1_fb55

Including the part where you pair up with a classmate and fork their repository, git clone it on your local machine, make changes to it, push the changes to your fork, and submit a pull request to your classmate.

If you were able to follow along you should have a repository set up on your local machine as well as on your github account named gittest_\<yourname\>, with a single file in it named myfirstfle.txt, and you should have a resolved merge conflict. Because your repo is public we can access it, and see the history of your file, and the conflict in it. If you fell behind, please take yourself to this point, and feel free to work with others, but remember that it is your responsibility to learn and be able to reproduce by yourself the work that you do in groups. 
 

## HW2

1. Create a new repository called PUI2018_\<your NYU ID\> (this for me would be PUI2017_fb55: https://github.com/fedhere/PUI2017_fb55 ). 

Inside it crete a README file that states the purpose of this repository. 

Create a HW1_\<your NYU ID\> folder in your PUI2018_\<your NYU ID\> repository on GitHub.

Your environment should be setup from last week. Follow the github directions to create a repository on the command line on your local machine. Notice that in this case you are working in the reverse order compared to the lab: you create the first instance of the repository on the remote server (on the web) and then you create a local repo to link to it on your machine. Follow the steps indicated by github to create the repo, a README.md file, and to link the online and local repos.

Now modify your README.md file: edit the copy on your machine to have it describe what you did to set up your enviroment and upload the screenshots I directed you to crete last week, so that they are displayed in your README.md (like in the image below). The README.md is a “markdown” file. To see what the syntax to upload an image in a markdown file, or in general to format the text, you can look at the README.md file in my PUI2018_\<fb55\> repository and if you look at the raw file by clicking the Raw button on the top right you can see the syntax. Remember that you also need to upload the images in your remote directory for them to be displayed in your README! just like any file you add them by git add and git commit, git push.

Your repository should automatically show the images

![Alt text](../HW1_fb55/screenShots/setup_env.png)
![Alt text](../HW1_fb55/screenShots/fbianco_bash.png)

My bash_profile is complicated. Yours will likely be shorter and simpler. But in mine you should be able to spot the export line and the alias line for PUI2015 and/or PUI2017 (yours should be 2018).


Grading: each one of you should have the repository PUI2018_\<your user name\> with a HW1_\<fb55\> directory in it with the readme file displaying your bash setup

If you did the extra credit last week upload that too to this repository. We will review it next week. 

## Reading:

[What does research reproducibility mean? Steven N. Goodman*, Daniele Fanelli and John P. A. Ioannidis](http://stm.sciencemag.org/content/8/341/341ps12 )






## References:

markdown syntax - http://daringfireball.net/projects/markdown/syntax

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
reproducible research

basic bash commands

github setup
