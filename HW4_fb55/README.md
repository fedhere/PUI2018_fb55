# PUI2018 HW 4.

## ASSIGNED READING:

- [The Earth is Round (p<0.05)](https://www.researchgate.net/profile/Andrew_Marshall13/post/Are_likelihood-based_approaches_to_statistical_modelling_REALLY_removing_the_arbitrary_problem_of_95_significance/attachment/59e33c7d4cde2617ef83d882/AS%3A549676011458560%401508064381495/download/Cohen1994_TheEarthIsRound_AmPsych.pdf), Jacob Cohen 1994. A critique of _p_-value based science. 
(The above link is free, the [official link](http://psycnet.apa.org/fulltext/1995-12080-001.html) should be free whenn accessed within thhe NYU network.

## ASSIGNMENTS:

## Submission Info
### You can work in groups, and you are encouraged to. 
Create a HW4\_\<netID> directory in your PUI2018\_\<netID> repository. 
Include a README.md that briefly summarizes the scope of the homework (so we know you understand what you did), 
and states with whome you worked and what you specifically contributed to.  
Submit Assignment 1, Assignment 2 and Assignment 3 by pushing the notebooks into your PUI2018\_\<netID>/HW4\_\<netID>  
repository.  Keep in mind that we will look for possible cases of plagiarism, 
and if the code appears too similar to that of people that you did not work with to be original work 
(there are automated ways to look for plagiarism in code) *you will be penalized*. 


### Assignment 1: Write an ipython notebook that demonstrates visually in a data-driven way the Central Limit Theorem. 
A skeleton notebook is [here](https://github.com/fedhere/PUI2018_fb55/blob/master/HW4_fb55/Assignment1.ipynb)

- GENERATE  100 samples of different sizes N (N>10 & N<2000) from each of 5 different distributions (500 samples in total), _all with the same population mean_
- Include a _Normal_, a _Poisson_, a _Binomial_, a _Chi-Squared_ distribution, and 1 more of your choice.    
- For each sample PLOT the sample mean (dependent var.) against the sample size N (independent var.) (if you want you can do it with the sample standard deviation as well). 
- DESCRIBE (in a caption to your figure) the behavior you see in the plots in terms of the _law of large numbers_ or _Central Limit Theorem_.
- PLOT the distributions of all sample means (together for all distributions).  
  _Mandatory_: as a histogram. 
  _Optional_: in any other way you think is convincing
 
__Extra Credit__: FIT a gaussian to the distribution of means            

### GRADING: 

Your notebook must: 
- generate the distributions, correctly generated for each of the 5 ditributions, all with same mean.
- display all plots: a scatter plot per distribution and a histogram of all distributions, usual rules for plotting applying: visible and readable axes, title, legend, caption. 
- each plot must have a caption which describes the plot in terms of _Central Limit Theorem_


### Assignment 2: Set up the work for data-driven inference based on CitiBike data. You should, even more than usual, work in groups for this!

### I developed an example [here](https://github.com/fedhere/PUI2018_fb55/blob/master/HW4_fb55/citibikes_gender.ipynb)

  
You can work on [ADRF](http://cusp.adrf.cloud/), or on your docker. 
Choose a citibikes dataset (one or two months, earlier datasets are convenient cause they are smaller. More than one month may help address seasonal effects, etc, etc...).

1. Fire off a Jupyter notebook from the command line, or with Jupyter Hub or Jupyter Lab and switch to the Kernel PUI2017_Python2 or PUI2017_Python3 if on ADRF from the Jupyter dropdown menu under Kernels -> Change Kernel.

2. States the question you want to ask, and formulates the Null and Alternative hypothesis (remember the confidence level!) in words and as a formula. 
*You will not test the hypothesis yet!* please do not do it even as extra credit (others will do your hypothesis)
3. Use pandas to read in the CitiBike files, you must be able to download the data within the notebook, and move it to $PUIDATA (so the TA can reproduce your work). 
3. Display the top few rows of the DF in your notebook. This table __must be rendered__.
5. Display the reducted dataframe (with .head() for example). This table __must be rendered__.
6. Plot your data distributions. The data left at this point should be the data that you think will be useful to answer your question. Drop all other columns/rows.

### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis to be tested
- the data tables for the unreducted datasets (first few columns)
- the data tables for the reducted datasets (first few columns)
- the plots for each dataframe, with usual rules for plotting applying: visible and readable axes, title, legend, caption. 

## Assignment 3: Finish z-test lab and turn it in as a notebook .

Follow the instructions on the slides as discussed in class. You are using the Z test to understand if a (fictitious) implementation of an alternative bus route for (fictitious) bus line X8 improves circulation. You know that the priginal bus rout for X8 took 36 +- 6 minutes (mean and standard deviation _parameters_ of the population) and you have a table for the duration of a number of trips with the new bus routes. You do not need to import packages or run a pre-written _Z_ test. The test is simply the formula below. What I am looking for here is: seeing a good Null/alternative hypothesis statement and treatment, with a clear Null and Alternative spelled out AND written out _as a formula_ (spometihing - something >=0 for example), and a good interpretation of the Z value you obtain in terms of ability or inability to reject the Null Hypothesis.

Here is the forumla

<img src="Screen Shot 2018-09-26 at 1.14.09 PM.png" align="center" border="0" alt="Z = \frac{\mu_{pop} - \mu_{sample}}{\sigma / \sqrt{N}}" width="154" height="44"/>

This is also in the slides attached (in a more readable format).

Acquire the data as needed, measure the statistics for the distribution (the mean of the sample and sample size) and plug them in the formula. The number you get, the _Z statistics_ is the number of standard deviations away from the mean of your sample. _Have you set a significance level ahead of time as you should have?_ Then you can compare that probability threshold with the probability of getting a result at least as extreme as the one you got for your Z test. Remember that the Z test is returning multiples of the standard deviation of a Normal distribution, so 1sigma corresponds to 68% inclusion, 2sigma 95%, 3sigma 99.7%


The chapter of [_Statistics In a Nutshell_](https://theswissbay.ch/pdf/Gentoomen%20Library/Maths/Statistics/OReilly.Statistics.in.a.Nutshell.A.Desktop.Quick.Reference.Aug.2008.pdf) that covers these topics is called Inferential statistics, including the Z test. 
It is chapter 3 in the hard copies of the book in the CUSP library, 
but it was moved to chapter 7 in the online book version which is in the link. Same content more or less.


### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis (Null and Alternative) to be tested in words and formula
- the download of the data (which is in https://github.com/fedhere/PUI2018_fb55/blob/master/Lab4_fb55/times.txt, but you must get the raw data!)
- the calculation of the Z statistics (with the given formula and the data processed from the data file)
- the comparison of the statistis with the _significance threshold_ and the conclusions about the Null Hypothesis

