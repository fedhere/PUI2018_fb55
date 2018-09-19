# remove sensitive files from repos

1. Create a file in this repo inside of the folder _Lab3_fb55_ called _test.csv_ - the content should be a few lines of text following the csv syntax, for example

    ```
    a,b,c
    
    Hello,World,!
    ```
  

2. commit this file to your repo and take a repo screen shot and a screenshot of the folder _Lab3_fb55_'s history

![screen shot](img/test.csv.png)
![screen shot](img/history.png)

3. go to a terminal where you have a clone of the PUI2018 repository and pull the changes, so that you have the test.csv file locally. 

4. type the commands that allow you to remove the file AND ITS HISTORY from the repo. See the screenshot below and type the commands

![screen shot](img/commands.png)

5. make sure the file was removed from your local: type ls inside of Lab3_fb55 and take a screenshot of the result (like below) - test.csv should no longer ber there. and that there is no longer a _test.csv_ file in your remote repo. When the graded looks at the repo they should not find the file or its history at all!

![screen shot](img/repo_history.png)
