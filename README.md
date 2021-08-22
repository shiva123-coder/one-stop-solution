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