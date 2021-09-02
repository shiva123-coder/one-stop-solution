# ONE-STOP Solution

## Aim/ Purpose

- The ONE-STOP Solution is a website dedicated as a platform for various self-employed people who want to sell their skills and provide services to the communities. The   website allows users to search and view various services, register and add the applicable services as well as interact with the website’s administrator to query and book available services. Furthermore, users can be added and removed by the admin. This website is my Milestone Project 3 for the Full Stack Developer course at Code Institute. In addition, I am planning to use this website to start my own online business in the near future.


## Issues and Ressolutions
- Live browser did not worked and upon checking on Gitpod terminal , Error 98 was shown
 - I did my research on google/slack and stack overflow and found the solution of it by closing all the open ports by using kill command as below :
   - First I viewed all the open ports by clicking on Ports which is displayed on bottom right of my workspace
   - Then I typed lsof -i:<'port number'> command in my terminal, this displyed PID associated with port number
   - Finally I have used kill -9 <'PID'> command which then kill the port that I wanted.

- I was not able to see the live preview on browser while using python3 app.py command on my terminal, upond checking on the terminal I noticed that ValueError was shown
  - I then checked all of my codes and logic and noticed [typo](static/images/valueerror1.jpg) on env.py file where I typed MONGO.URI instead of MONGO_URI, problem solved after i fixed this typo.

- Browser threw werkzeug.routing.BuildError while I was initially testing my registration page, this took me a while to figure out as I couldn't spot any issue in my codes and neither any speeling error, however I have somehow spoted that there was [typo](static/images/typo1.jpg) on app.py file as I as missing @ symbol on my routing and this was causing an error which solved after I corrected this.

- There was [TypeError](static/images/typeError1.jpg) shown on live browser and also on my terminal while I was testing my account.html page after writing python logic to app.py file. upon checking the error message I knew that this was related to app.py file and I started to run through logic on app.py file and found that I was missing to pass an argument inside the function while creating function for account.html page, issue ressolved once I passed an argument to the function.

- [405 error](static/images/405error.jpg) noticed While I was testing my add_job.html page on live browser, I was mainly checking the functionality to add new job however it didnt worked and threw an error
  - I did some depth research on 405 error and then start checking my logic on app.py then I spotted that no methods were given while creating @app.route for add_job template, I then added methods=["GET", "POST"] to @app.route which then fixed an issue

- Issue with POST method on the form that I created to add new job for users, I filled the form and submit however after checking on MongoDB databse, I have noticed that some of the input value were not shown on collection , instead [null](static/images/null1.jpg) was shown, upon cross checking all the name and speelings on my HTML and flask I have found that there was mismatch on the name that I used, I was using job_description on HTML and description on app.py file while building POST method and this was causing problem which then fixed once I updated this