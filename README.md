# Newsboard Recommender System 
  
## Our website has an introduction about this project, please see: https://sites.google.com/view/newsbaordrecommender/home  

### Data   
link: https://drive.google.com/file/d/1qVeMlehhn3W9OpOZ854GGOIitbbpX7jb/view?usp=sharing  
this compressed folder includes the crawled news and some code generated files.
  
MIND data: https://msnews.github.io/ training set.  


### Function  
The code is in the newsrec.ipynb.  
  
### Prerequisite
To run this jupyter notebook, you do not need to download the data from the provided link above, but we recommend you to download as it provide the raw crawled news data from NYT API, and carwling news cost long time. But training set of MIND need to be downloaded, to run the code you will also need a Mailchimp account for building a user signup page and generating survey to collect user feedback, an email account for sending news.  
 
We also provide the code for generating news website which hosting on AWS S3. please go to folder generate_new_url.
  
Please note:  

For safety reason, the api key of Mailchimp and email key is not provided in the code. But you can create your own one to test the functions.   
If you have any questions about this project, feel free to email us at ruofan.chen19@gmail.com, swu6@wpi.edu.
