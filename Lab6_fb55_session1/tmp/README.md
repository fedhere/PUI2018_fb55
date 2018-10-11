Data used in these notebooks can be found at https://serv.cusp.nyu.edu/~fbianco/PUI2017/data. (If you have issues downloading from that website from compute or jupyterhub (you get a connection refused) you can download most of the data (except the large files like 311_Service_Requests_from_2010_to_Present.csv) from our class github repo. Remember that when you download from github you have to look for the _raw files_! The link stam is https://raw.githubusercontent.com/fedhere/PUI2017_fb55/master/data/)
Class slides for this lecture are here
https://github.com/fedhere/UInotebooks/blob/master/slides2017/UI2_PUI2017.pdf
To download data to compute use the wget command as follows:
  ```
  wget https://serv.cusp.nyu.edu/~fbianco/PUI2017/data/FILENAME.csv
  ```
  
replacing FILENAME with the appropriate name of course

or in on your local machine also with 
  ```
  curl -O https://serv.cusp.nyu.edu/~fbianco/PUI2017/data/FILENAME.csv
  ```
 
 or read them in directly (for example pandas.read_csv("https://serv.cusp.nyu.edu/~fbianco/PUI2017/data/FILENAME.csv")
 
 Remember to move data to $PUIDATA
 
 
 
