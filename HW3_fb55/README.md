# PUI2018 HW 2.

## ASSIGNED READING:

- [Appendix A](http://greenteapress.com/thinkpython/html/thinkpython021.html) of _Think Python_ by Allen Downey (2012)
  The full PDF and HTML versions of the book can be found [here](http://greenteapress.com/wp/think-python/)

- The markdown I prepared with tips on how to ask and answer a coding or computational question: [PUI2018_fb55/blob/master/HowToAskACodingQuestion.md](https://github.com/fedhere/PUI2018_fb55/blob/master/HowToAskACodingQuestion.md)


## ASSIGNMENTS:

### Part 1: perform the instruction in deleteData.md: delete data and its history from a GitHub repo

Deliverable: turn in the screenshot in your repo README.md and make sure your HW3_fb55 repo does not show any trace of the history of the test.csv file

### Part 2: Choose a CSV file from [NYC Open Data](https://opendata.cityofnewyork.us/) and use pandas to read the file and mangle the data within it.

### Part 3: Write scripts to stream real-time bus data from MTA through the MTA Bus Time interface. In order to access this data, you must first request an API key from MTA. 

This homework is based on assignments by Prof. Vo, who is a specialist in transportation and databases, and whome you will meet later in the semester. Please request your API right after class! It may take some time before you get a reply from MTA.

  1. Visit MTA Bus Time for Developers at the [MTA Developers Tools](http://bustime.mta.info/wiki/Developers/Index)
  2. Click on the “Go here” link to fill in your information and request an API. You should be
  receiving an email from MTA within an hour (most of the time within only a few minutes).
  3. The key should be in the form of xxxxx-xxxxx-xxxxx-xxxxx-xxxxx. Please keep this key only to yourself as it would be your authorization token for MTA access and will be in this assignment. 


## Submission Info:
### You can work in groups, and you are encouraged to. Create a HW2\_\<netID> directory in your PUI2018\_\<netID> repository. Include a README.md that briefly summarizes the scope of the homework (so we know you understand what you did), and states with whome you worked and what you specifically contributed to.  Submit Assignment 1 and Assignment 2 by pushing the scripts into your PUI2018\_\<netID>/HW2\_\<netID>  repository. You can work on whatever computer you wish to develope these scripts. Work on Assignment 3 in the jupyter environment within CUSP (like you did for UCSL), so you have acces to the Data Facility. Keep in mind that we will look for possible cases of plagiarism, and if the code appears too similar to that of people that you did not work with to be original work (there are automated ways to look for plagiarism in code) *you will be penalized*. 

  
MTA is using the SIRI (Service Interface for Real Time Information) API to serve their data in both XML and JSON format. I want you to use JSON for its increasing popularity in data access API over the web, and because it is a very natural format in Python, since it maps identically to a Python dictionary. 
Information on the vehicle monitoring stream is available [here](http://bustime.mta.info/wiki/Developers/SIRIVehicleMonitoring).

For example, using your key, you can retrieve all vehicle information for a bus line, e.g. B52, by
accessing the following URL http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52 after replacing YOUR_KEY in the URL string with your own API key.

### IMPORTANT NOTE:
The BusTime API server strictly enforces users to issue only 1 request per 30
seconds. Please do not constantly download or fetch data from the API in
shorter periods. It is a good idea to download a copy of the response to your
local machine for testing purposes. Also make sure to open it in an editor to
familiarize yourself with all the fields of the response.


# Assignment 3:  tracking each vehicle for a line

Write a Python script (not a notebook this time, so that you can experiment with writing code that takes line inputs) to retrieve and report information about active
vehicle for a bus line. 

__The final hand-in should be a single Python file, named
show_bus_locations\_\<netID>.py that takes exactly 2 arguments in the following format:__
```
python show_bus_locations.py <MTA_KEY> <BUS_LINE>
```

For example \<BUS_LINE> could be B52:

```
python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52
```
The above command has to fetch data from the MTA website through the SIRI API using the
provided key and return information on all available vehicles for the bus line \<BUS_LINE> (e.g. B52). 

__Your program
should output the following to the console:__ 
- the bus name, 
- the number of vehicles
- their current position

###SAMPLE OUTPUT:
```
Bus Line : B52
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694
```
### Grading:
 
 All or nothing at all: 
 - 100% of the points if the TA can run the code with his/her MTA key and get a correctly formatted output.
 
 The TAs will do minimal inspection of your code if it does not work. If the issue is not immediately obvious you will not get points for this assignment. 
 
 Working code but wrong output format (but correct content) will earn 50% of the points.

# Assignment 4: next stop information

Write a Python script that displays information on the
next stop location of all busses of a given line. For example, whether the bus is approaching a stop, or is 1 stop
away from it. All the information is already included in the response JSON: your code needs to pull the current JSON file from the MTA API (as before) and parse it to find it. 
Have this script *output the data to a CSV file*. 
For buses that do not have this information,
please output “N/A” in the stop information fields. 

__The final hand-in should be a single Python
file, named get_bus_info\_\<netID>.py that takes 3 arguments in the following format:__

```
python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv
```
__and output to a CSV file named \<BUS_LINE>.csv__:

```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```

Hint:

- The stop information are included in the “OnwardCalls” field nested somewhere in the
JSON file.

Notes:

- Your program will be tested against the grader API key with different bus lines. Please
make sure that your Python scripts can read arguments from the command line.
- The bus line name is case-sensitive, aka. B52 is not the same as b52
- You can assume that your Python script will be run using the most recent Anaconda
distribution. If you use any additional Python packages that are not included in Anaconda,
please specify them in your README.md when you turn in your github repository.
- When the OnwardCalls field is empty, you must output “N/A” as values for both the “Stop
Name” and “Stop Status” fields.

### Grading:

All or nothing at all: 
- 100% of the points if the TA can run the code with his/her MTA key and get a correctly formatted output.

The TAs will do minimal inspection of your code if it does not work. If the issue is not immediately obvious you will not get points for this assignment. 

Working code but wrong output format (but correct content) will earn 50% of the points.

# Assignment 2: Read CSV files with pandas

Choose a [dataset from NYC Open Data](https://opendata.cityofnewyork.us/)) that is available in CSV format (look at the format labels in the list of datasets or use CSV in the search bar). Chose one that has _at least_ 2 __numerical value__ columns. If it is a CSV file directly read it in with pandas 
```pd.read_csv(_url_). 
```
If it is a zipped file (.zip or .gz or similar) download the zip and unpack it in $PUIDATA, then read it in with pandas 
```pd.read_csv(os.getenv("PUIDATA") + <filename>)
```


1. Work in the [ADRF](http://cusp.adrf.cloud/). Fire off a Jupyter notebook with Jupyter Hub or Jupyter Lab  for Mac and Linux 
and switch to the Kernel PUI2016_Python2 or PUI2016_Python3 from the Jupyter dropdown menu under Kernels -> Change Kernel.

   Write a Jupyter Notebook that:

2. Check that an environmental variable PUIDATA exists and that it points to the PUIdata directory. Forcefully set it up within the notebook if it is not.Follow the instructions in [this notebok](https://github.com/fedhere/UInotebooks/blob/master/dataWrangling/setupPUIDATA.ipynb). The CSV file must have at least 2 numerical value columns.

3. Display the top 7 rows of the DF in your notebook. This table __must be rendered__.

4. Remove all but 2 _numerical values_ columns of your choice (you can use the drop method of the dataframe, like in the [lab example](https://github.com/fedhere/PUI2018_fb55/blob/master/Lab2_fb55/FormattingTables.ipynb).) 

6. Display the reducted dataframe. This table __must be rendered__.

7. Plot the columns one against the other in a scatter plot using the datafraome plot method, like in the [lab example](https://github.com/fedhere/PUI2018_fb55/blob/master/Lab2_fb55/FormattingTables.ipynb).  (usual rules for plotting apply, see [Grading Guidelines](https://github.com/fedhere/PUI2018_fb55/blob/master/README.md) and the [instruction notebooks for HW1 Extra Credit](https://github.com/fedhere/PUI2018_fb55/blob/master/HW1_fb55/HW1_3_instructions.ipynb), part 3, for more detailed hints on how to display your rendered plots, and the [Lab3](https://github.com/fedhere/PUI2018_fb55/blob/master/Lab3_fb55) and [Class notebooks](http://github.com/fedhere/UInotebooks/blob/master/dataWrangling) examples on how to use the dataframe plot modules. The plot __must be rendered__.

### GRADING: 
You must use the environment variable PUIDATA.

Your notebook must display
- the data tables for the unreducted datasets (first few columns)
- the data tables for the reducted datasets (first few columns)
- the plots for each dataframe, with usual rules for plotting applying: visible and readable axes, title, legend, caption. 



# Extra Credit Assignment : work with dates in Pandas

Repeat the steps above 1-7 with a CSV file that contains _a date/time column and a numerical value_. Plot the numerical value against the date/time (hint: make sure your tick labels are readable. you can use they keyword rot in the df.plot() method, as for example df.plot(....., rot=90) to rotate the tick labels by 90 degrees.


### GRADING:                                                

Same rules as for HW1 Assignment 3 apply. Make sure your plots are rendered, with axis labels, with a caption that describes what I see, and what I should notice in the plot
