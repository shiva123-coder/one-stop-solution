# ONE-STOP Solution

## Aim/ Purpose

- The ONE-STOP Solution is a website dedicated as a platform for various self-employed people who want to sell their skills and provide services to the communities. The   website allows users to search and view various services, register and add the applicable services as well as interact with the website’s administrator to query and book available services. Furthermore, users can be added and removed by the admin. This website is my Milestone Project 3 for the Full Stack Developer course at Code Institute. In addition, I am planning to use this website to start my own online business in the near future.


## User Experience(UX)

The goal of this website is to provide a satisfactory user experience and an accessible platform for users to find various available services which can be useful to support the necessities and day-to-day activities. The website should allow users to easily register or login and search for the right services at the right time based on their requirements. The users are also able to easily add and edit their services as well as find the required services via this website.

### User Stories

#### First Time User Goals
- As a first time user, I would like to be able to search for any specific services on the website.
- As a first time user, I would like to be able to register and create my own account on the website.
- As a first time user, I would like to be able to add, edit and remove my own services.

#### Frequent User Goals
- As a frequent user, I would like to be able to search for any specific services on the website.
- As a frequent user, I want to login to my existing account to add, edit and remove my services.
- As a frequent user, I want to be able to save my services for other users to search and view them.
- As a frequent user, I want to be able to contact the admin to query and book for available services.
- As a frequent user, I would like to be able to logout from my own profile.

#### Return User Goals
- As a return user, I want to easily navigate the site across all pages.
- As a return user, I want to easily search for any specific services on the website.
- As a return user, I would like to be able to access my existing profile to add, edit and remove my services.
- As a return user, I want to be able to save my services for other users to search and view them.
- As a return user, I want to be able to interact with the admin to query or book for various services.

## UX Framework

### Strategy

The ONE-STOP Solution is an online platform to access various services with front-end and back-end functionality, created using HTML, JavaScript, CSS, Python, Flask, and MongoDB. The goal is to create a website that is user-friendly and allows users to easily search and get various available services.

### Scope

The website is interactive and allows users to input or add their own services for other users to view or display, allowing them to edit and remove or delete their registered services and search for different services. The website has CRUD functionality. The users should also be able to contact the admin and get support with query and booking of the available services.

#### Functional Requirements

Functional requirements include: a user-friendly navigation menu, a search bar, working templates for services to be added, database functionality that stores user login information and ability to create new accounts, with authentication. In addition, the website should be responsive for various screen sizes, whilst maintaining the same level of functionality. The main functionality of the website is to allow users to create, read, update, and delete data, known as CRUD. The data created is stored in a database, and can be read through various pages on the website. The users also have the option to update and edit the data they have submitted, as well as delete it altogether. A search field allows users to search for specific services they are interested in.

#### Content Requirements

The content of the site should include a header and image, as well as a navigation menu. A search bar should allow users to search for services types. For each service, an image should be included, as well as its type or category and a short description of the service. An input field for users will allow them to add different services, and they are also able to provide their availability, which will be compiled as a list or options alongside other service categories.

### Structure

The website is structured to allow new visitors to view numerous services on the landing page once they open the website. From there, they are able to log in or register, which will allow them to create and view their profile page of existing services. Once logged in, users are able to click on the main header, which allows them to search for different services, as well as add and edit their own services. In addition, the users are able to save the registered services. Once the user wishes to end their session, they can click the 'Log Out' option in the menu to return to the home page.

### Skeleton

The skeleton of the website will utilise Materialize for the CSS layout of the pages. A navigation menu will allow users to go to their chosen pages. The main landing page will function to allow users to select numerous service types or categories they are interested in, and provide links to add or edit their own services. This minimises the need for different pages for users to visit and provides a seamless experience. When adding or editing a service, additional options in the navigation menu allow the user to navigate back to their own profile, or to end the session and log out. This simplifies the number of options for the user and keeps the website easy to use.

### Surface

The surface design of the website will also utilise Materialize CSS to provide a theme and styling for the components of the website. Google Fonts is used to style the text using the Yusei Magic' and 'Ovo' fonts  and FontAwesome is used for various icons. The colour scheme is designed to be professionally appealing to the target audience of varied professionals, and provide clear readability as well as being responsive.




## Issues and Resolutions
- Live browser did not worked and upon checking on Gitpod terminal , Error 98 was shown
  - I did my research on google/slack and stack overflow and found the solution of it by closing all the open ports by using kill command as below :
    1. _First I viewed all the open ports by clicking on Ports which is displayed on bottom right of my workspace_
    1. _Then I typed lsof -i:<'port number'> command in my terminal, this displyed PID associated with port number_
    1. _Finally I have used kill -9 <'PID'> command which then kill the port that I wanted._

- I was not able to see the live preview on browser while using python3 app.py command on my terminal, upond checking on the terminal I noticed that ValueError was shown
  - I then checked all of my codes and logic and noticed [typo](static/images/valueerror1.jpg) on env.py file where I typed MONGO.URI instead of MONGO_URI, problem solved after i fixed this typo.

- Browser threw werkzeug.routing.BuildError while I was initially testing my registration page, this took me a while to figure out as I couldn't spot any issue in my codes and neither any speeling error, however I have somehow spoted that there was [typo](static/images/typo1.jpg) on app.py file as I as missing @ symbol on my routing and this was causing an error which solved after I corrected this.

- There was [TypeError](static/images/typeError1.jpg) shown on live browser and also on my terminal while I was testing my account.html page after writing python logic to app.py file. upon checking the error message I knew that this was related to app.py file and I started to run through logic on app.py file and found that I was missing to pass an argument inside the function while creating function for account.html page, issue ressolved once I passed an argument to the function.

- [405 error](static/images/405error.jpg) noticed While I was testing my add_job.html page on live browser, I was mainly checking the functionality to add new job however it didnt worked and threw an error
  - I did some depth research on 405 error and then start checking my logic on app.py then I spotted that no methods were given while creating @app.route for add_job template, I then added methods=["GET", "POST"] to @app.route which then fixed an issue

- Issue with POST method on the form that I created to add new job for users, I filled the form and submit however after checking on MongoDB databse, I have noticed that some of the input value were not shown on collection , instead [null](static/images/null1.jpg) was shown, upon cross checking all the name and speelings on my HTML and flask I have found that there was mismatch on the name that I used, I was using job_description on HTML and description on app.py file while building POST method and this was causing problem which then fixed once I updated this

- I stored some images on my databse using their URL which I wanted to render on my home page directly, however upon testing on browser images did not displayed, instead only URL was shown as a string. I had to then do some depth research on how to store images on mongoDB however I couldnt find any easy process, after few hours of struggle I decided to re-check my codes and noticed that I have [not supplied img tag inside jinja for loop](static/images/image_url1.jpg) in home.html which was causing an issue in this case. This one sorted after I updated my jinja for loop with img tag inside the loop.

- Modal that I used on the home page did not worked as expected, I was testing page on live browser after adding six jobs and I was expecting modal to trigger and disply information upon clicking on each button however all the button displayed same information instead of each button showing different information
 - I did depth online research on how to use modal while inside the loop and cross check on my code then I realised that issue was due to my modal-id the as modal was in a loop - and each time I run that loop if the modal id was the same so it was keep just retruning the same detail - so I needed to use unique id when modal call. I have set modal id as below which then resolve my issue
```
id="job_modal{{ job._id }}
```

## Credit

- Thanks to SDTE- Automatopn Techie for [youtube video](https://www.youtube.com/watch?v=mG3aGgFYJSE) on special character vaerification, this video help me to understand the concept of password validation with special character.
- Thanks to The IT Guy for [youtube video](https://www.youtube.com/watch?v=W4-5WM60gWg&t=121s), this video helped me to understand the input field validation with error message on form. I have also taken some of the code from this video and modified as per my requirement.
