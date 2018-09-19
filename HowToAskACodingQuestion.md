# The right way to ask a question when it is about code. 

First off: we, me and your TA's, are in the business to help you learn. 
Literally that is what we get a paycheck for. 
Thus we welcome your questions! 

However, and especially considering there are about 100 of you, please try to minimize our effort by asking questions the right way, 
and making efforts to find a solution on your own before you come to us. 
This workflow, which minimizes our effort, also maximizes your learning. 

1. __If you come across an error message__, in bash, Python, or in whichever software or language you are working, 
__read the error__. Go beyond the word 'error' or the word 'fatal' and try and understand what the software is complaining about. 
Many pieces of software will offer details, and propose solutions to you right away! 
Git for example always gives you suggestions on what to do to address an error. Here is an example:
    ```
    fbianco@octomore: 19:44:12:~/science/Dropbox/UI/PUI2016_fb55$git push

    To https://github.com/fedhere/PUI2016_fb55.git
    ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'https://github.com/fedhere/PUI2016_fb55.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    ```

2. __Read the _error every time_!!__ It often happens that your commands fails, and you read the error and try to address the issue
only to try your command again and again getan error. It is natural to suspect that the error was not resolved by the changes you implemented, but you should check: 
Just because you still have an error after changing things up do not assume that it is _the same error_. 
Your code, just like mine, just like anyone's, is blooming with bugs like a warm summer night in NYC. 
Even when it works, and even when it gives the correct answer, it's still buggy. 
As you solve one issue others may come up. Read the error message every time. 
(For me and the TAs trying to help you, it is difficult if you tell us the solution we gave you had no effect, 
and we go look into the problem and try and figure out another solution, 
and then it turns out we had in fact solved the problem and something else entirely was also wrong. We waste our time, 
but you alsowaste your time waiting for help on a problem already solved!)



3. __Look around__. Look on the NYU classes resources, announcements, board, 
to see if the problem already came up and is solved there. Make sure you have the most recent version of the 
homework assignment (make a gresh $git pull). Then try Google it: Google is your friend! 
Then, by all means, if you find solutions that are not clear to you, or you do not find solutions, come to us. 
Ideally the TA fist, then me. There is an endless stream of computational problem-solving resources out there. 
But it takes a bit of time to familiarize with the lingo, if you are not used to it. 
The first place to look for solution to computational issues is [stackoverflow](http://stackoverflow.com/), 
and in most cases if you google an error you will come across one, or many, stackoverflow threads. 
Unfortunately, the computational comunity, and more generally the scientific community, is not always polite. 
Answers will be at times condescending, at times just outright rude. We of course do not support that. 
__Please be polite to your peers if you give answers__ and do not let online trolls discourage you 
from asking questions, or make you feel bad for not knowing something. You are here to learn!


4. __Give us all the information we need to help you__. 
If you have an error on your terminal, for example, tell us, by copy and paste, and/or with a screenshot, 
what _the command_ that causes the error is, and what _the full error_ is. 
If it is code you are running, make sure we have access to the code to inspect it. 
Tell us which platform you are working on, Linux, mac, widows (git bash or something else...). 
Otherwise it's garbage in, garbage out. 
Look on [stackoverflow](http://stackoverflow.com/), to get a sense of how people write questions 
(look at the replies and see if the users complain about the format of the question). 

5. __If you are giving help__ always be respectuful of your classmates! Trolling, and rudeness will not be tollerated. 
Look at this [code of conduct](https://www.recurse.com/manual#sec-environment) from the [Recourse Center](https://www.recurse.com/).
Also from the same resource, let me take a wonderful piece of advise:
    ```
    Don't panic

Regardless of how much experience you have, 
we admitted you because we believed you would be a positive influence on the batch, 
and we think being at the Recurse Center can help you dramatically improve as a programmer. 
This is really important, so we'll say it again: Everyone is here because we want them to be here, 
so if you're reading this, don't worry about how much more or less other people in your batch know. 
You are here because we want you to be here and believe in you.
```
