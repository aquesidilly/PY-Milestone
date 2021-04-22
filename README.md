## Movie Application
   This is a Movie Application where movie lovers can watch movies update and delete movies they have already watched. With various  movies available for all as well as options to add your very own, there is something for everyone. Think you could be the next movie star? You have to let the world know of your amazing  creativity, and you can do so at Movie Application! Movie Application is an amazing place to learn,watch and add new movies to spice up your your collections. You can also choose from a variety of movies uploaded on the app, the type of movies available to watch as well.

UX
List of User Stories

As an aspiring movie content blogger, I want to publish a movie app , so that I can gather attention to movies and amass a following.
As an office worker with little time, I want to know about movies that i can watch with in an hour and half or two, so I can be glued to it .
As a child, I want to learn about  movies that will educate me and broaden my horizon, so that I can learn alot .
As someone who is depressed and down-hearted, I would want to watch movies which will elevate me.
As a sick person, I want to watch movies which will catch my interest so i don't think about my illness.
Features
Existing Features
Recipe Creation - Allows users to create their own recipes, by having them fill up a recipe creation form.
Recipe Updating - Allows users to update their own recipes, by having them fill up a recipe update form.
Recipe Deletion - Allows users to delete their own recipes, with checks in place if they try to delete a recipe they did not create.
Searching for Recipes - Allows users to search for recipes, by having them type in a search bar.
User Creation - Allows users to create user accounts, by having them fill up a user creation form.
User Account Details Updating - Allows users to update their user details, by having them fill up a user details updating form.
User Deletion - Allows users to create their own recipes, by having them fill up a recipe creation form.
View Counter - Allows the number of views on each recipe to increase whenever a user clicks on that recipe
User & Recipe Photo Upload - Allows the user to upload photos for their recipes as well as their profiles, by storing the photos in AWS S3.
Features Left to Implement
Comments Section: Where users can leave comments on each of the recipes as well as other's users' comments.
Review Section: Community driven review section, based of 5 stars, with the inclusion of certified reviewers whose reviews will be highlighted
Blog Section: Community Written Blogs
A webpage for each individual category with the relevant recipes displayed
Technologies Used
Boostrap
The project uses Boostrap to create a mobile responsive and stylish webpage.
JQuery
The project uses JQuery to simplify DOM manipulation.
Flask
The project uses Flask as it's main framework.
Flask-Bcrypt
The project uses Flask-Bcrypt to hash user passwords.
Flask-S3
The project uses Flask-S3 to allow for the uploading of photos to AWS S3.
boto3
The project uses boto3 to allow for the uploading of photos to AWS S3.
botocore
The project uses botocore to allow for the uploading of photos to AWS S3.
cffi
The project uses cffi to allow python to call C code.
dnspython
The project uses dnspython to allow for the pymongo connection to be more secure.
gunicorn
The project uses gunicorn as a python WSGI HTTP server to deploy the app on Heroku.
pymongo
The project uses pymongo to connect the app to a MongoDB Atlas database.
PyMySQL
The project uses PyMySQL to connect the app to a remotemysql database.
python-dateutil
The project uses python-dateutil to allow python to get the current date.
s3transfer
The project uses s3transfer to allow for the uploading of photos to AWS S3.
urllib3
The project uses urllib3 as a HTTP client.
Boostrap-Select
The project uses Boostrap-Select to allow for the user to search of an option in the select input.
Axios
The project uses Axios to simplify AJAX calls.
Testing
Manual Testing:

Interesting Bugs/Problems:

The hashed passwords were not being accepted by Flask-Bcrypt as I had limited the number of characters in the password field on the database to only 30. This meant that the stored values were a substring of the actual hashed password and thus would not be accepted by the hashing algorithm.
Jquery's onclick function would not work for dynamically loaded buttons, therefore I had to switch the Jquery to be an on function instead.
To make all of the recipes in the recipe list be of the same height. The number of categories displayed for each recipe could not be more than 5. So if the number of categories for a particular recipe was above 5, the app would randomly choose 5 to display. This however does not limit the search functionality.
The custom selectpicker were not appearing when they were added dynamically, therefore i added a selectpicker refresh function to run each time they were added.
Deployment
On the development version, sensitive information is stored in an env.py that is not pushed to github. Where as on the deployed version, these sensitive information are stored in the Heroku Config Vars

To run the app locally:

Open the app.py in the main directory.
Run this python script.
Click on the local host link address to open the app the web browser.
You can view the deployed version on Heroku 

Credits
Content
The text for recipes were taken from Tasty
Media
The photos used in this site were obtained from Stock Snap,Pexels,Unsplash,Pixabay,FoodiesFeed
Acknowledgements
The Boostrap Template was taken from ColorLib