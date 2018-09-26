# PUI2018 HW 4.

## ASSIGNED READING:

- [The Earth is Round (p<0.05)](http://psycnet.apa.org/fulltext/1995-12080-001.html), Jacob Cohen 1994. A critique of _p_-value based science. 


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

### I developed an example [here] (https://github.com/fedhere/PUI2018_fb55/blob/master/HW4_fb55/citibikes_gender.ipynb)

  
You can work on [ADRF](http://cusp.adrf.cloud/), on your docker. 
Choose a citibikes dataset (one or two months, earlier datasets are convenient cause they are smaller. More than one month may help address seasonal effects).

1. Fire off a Jupyter notebook with Jupyter Hub or Jupyter Lab and switch to the Kernel PUI2017_Python2 or PUI2017_Python3 from the Jupyter dropdown menu under Kernels -> Change Kernel.

2. States the question you want to ask, and formulates the Null and Alternative hypothesis (remember the confidence level!) in words and as a formula. 
*You will not test the hypothesis yet!* please do not do it even as extra credit (others will do your hypothesis)
3. Use pandas to read in the CitiBike files, you must be able to download the data within the notebook, and move it to $PUIDATA (so the TA can reproduce your work). 
3. Display the top few rows of the DF in your notebook. This table __must be rendered__.
5. Display the reducted dataframe (with .head() for example). This table __must be rendered__.
6. Plot your data distributions.

### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis to be tested
- the data tables for the unreducted datasets (first few columns)
- the data tables for the reducted datasets (first few columns)
- the plots for each dataframe, with usual rules for plotting applying: visible and readable axes, title, legend, caption. 

## Assignment 3: Finish z-test lab and turn it in as a notebook .

I am looking for here is: seeing a good Null/alternative hypothesis statement and treatment, with a clear Null and Alternative spelled out AND written out as a formula, and a good interpretation of the Z value you obtain in terms of ability or inability to reject the Null Hypothesis. 
Here is the forumla

<img src="http://bit.ly/2N3HGT6" align="center" border="0" alt="Z = \frac{\mu_{pop} - \mu_{sample}}{\sigma / \sqrt{N}}" width="154" height="44"/>

This is also in the slides attached (in a more readable format).

The chapter of _Statistics In a Nutshell_ that covers these topics is called Inferential statistics. 
It is chapter 3 in the hard copies of the book in the CUSP library, 
but it was moved to chapter 7 in the online book version which is in the link. Same content more or less.


### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis (Null and Alternative) to be tested in words and formula
- the download of the data (which is in https://github.com/fedhere/PUI2018_fb55/blob/master/Lab4_fb55/times.txt, but you must get the raw data!)
- the calculation of the z statistics (with the given formula and the data processed from the data file)
- the comparison of the statistis with the significance threshold and the conclusions about the Null Hypothesis

