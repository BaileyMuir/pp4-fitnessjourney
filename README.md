# Fitness Journey
Fitness journey was annd is ment to be a platform for people to share advice, insporation or even workout routines for others to use for free.

# Features

## Header
The header contains a navigation bar for which there are three links each to a relevant page and a logo in the top right corner.

The navigation menu is designed to be responsive and easy for anyone to use; they clearly list the page they correspond to and allows the reader to get a brief description of what they are going to access.

Because of this, it will provide a smooth and relaxing experience for my target audience.

## Main image

Includes a landscape image to act as a visual cue to the target audience and act as a visually appealing section to catch their attention and acts as a nice contrast to what else is just a white background with some text about.

It's designed to be reactive, so on smaller screens, the image won't appear pixilated as a result.

## Footer

- the footer provides something visual fo the user to ingage with being the social tabs that link to e.g. twitter. (code from walkthrough django project codeinstitute).

## blogs
- each blog has a optional picture that can be added to make it more appealing to the users.

## messages
following e.g. login in their will be a message prompt apear.

# Future improvements.

- Due to it being unfinished i would have liked to get the comments and like functionality to work.
- I would have liked to have added the contact us page.
- I would have liked to have styled my pages more to make them more my own and appealing to look at.

# Testing

- I used google chromes developer tools to see how it would display in other viewports.
- I also used my phone and a tablet to see how it works on them directly.
- I tested it on chrome, Microsoft edge and firefox to see how it would work on popular browsers.
- I also used the w3c site to check the HTML and CSS aswell as pep8 to check the python/django.

# UX

# User stories

## Website owner
- I want my users to be able to navigate through the webpage effortlessly.

- I want my users to be able to make posts themselves and have the ability to see peoples comments.

- As the owner, I want to be able to review posts before they are posted and to be able to delete them if they are rude or false information.

- As the sight owner, I want to be able to approve comments, so there is no obscene language.

- As the owner, I want my users to be able to log in and out of their accounts at will.

- As the sight owner, I want to be able to receive emails from users about potential issues or ideas.

## New user

- I want to be able to create my own account and log in/ log out.

- I want to be able to publish my own articles and routines.

- As a user, I want to be able to comment on others posts and communicate as part of a community.

- As a new user, I want to understand how to navigate the website at a glance.

- As a new user, I want to understand the purpose of the website.

## Returning user

- I would like to be able to review old posts that I have saved.

- As a returning user, I would like to be able to delete my old posts.

- As a returning user, I would like to see the genuine consensus of the post based on the number of likes and dislikes.

- As a returning user, I would like to filter through the posts based on time, likes and user name.

# Website structure
First, I used Wireframe to provide a basic template of my website. This was to put across my ideas to make an efficient and visually appealing layout for my users and provide a hassle-free environment for them to learn in, such as the navigation bar.

# Wireframe design



# Bugs/Fixes

- My first bug and or error was caused in my original repository as i was using a unstable version of django-gunicorn.
- During early development i forgot to use pascalcase naming system which caused minor errors but was easily rectified by changing the required inputs text type to PascalNaming style such as "FitnessJournal".
- During  early development i couldnt get the home page url to work as it turned out i needed a model to get it to work but it was unused and a waste of code as a result but then i found you could load the index..html into the django as it is displayed in the html.
- I added my issues to github after my initial deployment to heroku as a result my terminal wouldnt allow me to commit changes due to a fork in the deployment to fix this I  had to use git pull to add the new changes in the new fork sepret to main into main.
- used a h1  closing tag on the start of a h2 tag fixed by changing the trailing close tag to a h2.

# Validator used
https://jigsaw.w3.org/css-validator/
https://validator.w3.org/
http://pep8online.com/checkresult

# Deployment procedure

### Deployment
The project is deployed on GitHub Pages, and I used Gitpod to develop my assignment. When I committed all changes, I used git add . followed by git commit -m "" providing a description or summary of the changes. I used git push to save changes to GitHub.

## To deploy a project, I had to:

### Deployment to Heroku

requirements.txt - You can create one using pip3 freeze --local > requirements.txt and after to update it and a Procfile is required before anything can be posted to heroku.

## Create app.
- Go to Heroku's site and Register or Login if you have an account.
- Click on the new button in the top right hand corner and select "Create new app".
- Enter the app name and make sure its unique as each one is one of a kind and pick the region that is closet to you.
- If the above is fine create the app.
- after created go to resources and search for Heroku Postgres this is required for our project and its free to use.

## Set environment variables:
Click on the settings tab and then click "Reveal config vars" copy the DATABASE_url as its required in the settings.py and procfile as a result won't run without it.

then in the procfile add a SECRET_KEY and CLOUDINARY_URL and put them into herokus convig vars.

make sure to preform python3 manage.py makemigrations follow by python3 manage.py migrate in the gitpod terminal.

after this use python3 manage.py createsuperuser this will be handy as it also allows us to autherise and add new blogs.

## To connect your Heroku app to be deployed from a Github repository, follow these steps:

- Open the heroku app page on the deploy tab and select GitHub - Connect to GitHub.
- when prompted to if required login to GitHub if not already.
- search for your specific github file you want to deploy.
- Once the repository has been found, click to connect.
- Once you have your GitHub repository connected correctly use the deployment option under automatic and it will build it based on your main.filename

## Final deployment 
Make sure debug = False in settings.py and that DISABLE_COLLECTSTATIC is removed from config vars in settings.

### Host locally

Log in to GitHub and click on the repository to download the file. Click the code button next to the green Gitpod button and press download ZIP; this will download all files in this repository and is easier than using the link it provides you to download.

# Credits

### template

The template comes from https://github.com/Code-Institute-Org/gitpod-full-template provided in the using our template section of the course.

### Code

all Fontawesome code came directly from https://fontawesome.com/

all the basic.html exscluding the inddex.html was from the django walkthrough project on codeinstitute.
the django models and functionality are also based on the walkthrough project on codeinstitutes website.

## Content

## Images
Unsplash.com provided all images.

# Resources used

- HTML and CSS - to structure and style the pages, respectively.
- Fontawesome - for icons used.
- Googlefonts - provided me with the fonts needed to style my page.
- GitHub-was used as a way to store my assignment.
- Gitpod - allowed me to develop my assignment.
- Developer tools chrome - allowed me to make small changes to work without affecting Gitpod, and check how it would look on specific devices based on their viewport size.
- Balsamiq wireframe - was used to make the basic design as a template.
- Heroku allowed me to host my website.
- grammerly for spelling and grammer.
- bootstrap was used to make styling more simple

# testing
all the testing was done manualy

- login/logout/register all work and on completion take you to the requested page followed witha success prompt.
- all the slugs for journals work.
- currently the placeholder image doesnt work but did in past versions.
