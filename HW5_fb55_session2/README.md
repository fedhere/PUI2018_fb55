# PUI2017 HW 7.

## ASSIGNED READING:

[The simple rules for structuring papers](http://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1005619) 

Please read this carefully. In the second half of the semester I will pay a lot more attentions to the subtiltes of your presentations, starting with this homework.


## ASSIGNMENTS:

### Submission Info:

For Assignment 1: Submit through notebook **and** [Authorea](https://www.authorea.com/)

For Assignment 2: Submission however Prof. Vo organizes it.

![https://xkcd.com/327/](exploits_of_a_mom.png)


## Assignment 1: Finish your Citibike miniproject

**Work with the same team with which you submitted the proposal and turn in a single Authorea report.**
If you worked in a group your team should have recieved more than one review, merge and discuss their content as apprioriate.

1. make an account on [Authorea](https://www.authorea.com/) (if you do not have it yet). Authorea is a collaborative writing platform. It is likely the platform that we will used for the capstone reports so please begin familiarizing with it now.

2. Finish the Citibike analysis you set up in HW3 in a notebook. Perform the appropriate statistical test. 
Incorporate your classmate's comment (from the review you recieved in HW4) where appropriate, and when you are not incorporating them discuss why the suggestions were not embraced.

3. Write up a summary of the project as an Authorea article (a single article for your working team) which MUST includes:

**Abstract** - summary of idea and result

**Introduction** - a short introduction that explains what citibike is and why your question is interesting. Normally this would also include a discussion of similar work previously done (a literature review) but you do not have to worry about it now.

**Data** - a description of the data you use and how it is processed. This should include figures (with captions!!) that help visualize and understand the data.

**Methodology** - a description of the methodology (test) chosen, the motivation behind it, a discussion of alternative options that were not adopted. Either this session of the next one should contain figures as well to show the results.

**Conclusions** - The result and its significance, including the weaknesses and strengths of the analysis. Either this session of the previous one should contain figures as well to show the results.

Each session has to be included, each has to be written in plain English, full sentences. Each session should be between 50 and 100 words.

Incorporate the notebook in the Authorea paper following [these instructions](https://intercom.help/authorea/host-data/integrations/jupyteripython-notebook) and also upload it to your HW7_<netID> repo


NOTES: 
  - look for your classmate's review in HW3, HW4 and in the main repo. It should have been uploaded to HW3, but some people got creative with the destination. 
  - do not assume that the content of the review is right, wheather I commented on it or not! think for yourselves whether you want to incorporate it and justify it.
  - If you did not get a review by a classmate I am uploading a review for you. 
  - If you have ** NOT ACCEPTED THE PULL REQUEST THAT CONTAINS THE REVIEW ** that is your fault and points will be deducted if the review is not uploaded and considered in your report.
  - There is some confusion about the various chi sq tests, including understandable confusion arising from the various flowcharts that help chosing tests. In general, if you want to test 2 proportions use the chi sq as we did for the ex-convict job reintegration exercise (most commonly called chi sq test for proportions)
  - There is some confusion about the word "parametric": a parametric test means a test that assumes something about the variables tested (often that they are Gaussian distributed). The data is not parametric, the data can follow a distribution or functional form, so that you can use a parametric test, or it does not (or you cannot tell) and then you should use a non-parametric test (or at least acknowledge that the test you use makes assumptions that may not be correct)
  
### Grading 

You will be graded on the quality of the writing, as well as the correctness of the analysis. You will also be graded on whether you have discussed and considered the recommandations of your "referees", the classmates that reviewed your proposal.

## Assignment 2: Follow Prof. Vo instructions
SQL lab [Instructions](https://serv.cusp.nyu.edu/~hvo/files/SQL_Lab.pdf)

return the lab as a jupyter notebook using the [SQL_query notebook](https://github.com/fedhere/PUI2017_fb55/blob/master/HW7_fb55/SQL_query.ipynb) to start (in this repo) and submitting the sql queries through the carto API

