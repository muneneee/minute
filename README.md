# PITCHER


## Description

Pitcher is a web application that will allow users to post pitches, like, dislike and comment on other pitches.

## Features
- The home page allows users to see various pitches from the following Categories:
    - Interview
    - pickup lines
    - Famous-quotes
    - Bible verses
- User can see all pitches for that category chosen.
- Users create an account and receive a welcome message in their email.
- Once registered a user can log in and have additional capabilities including:
    - A user can like and dislike a pitch but only once.
    - Users can additionally comment more than once on other pitches.
    - Users can as well create their own pitch.



## View Live Site here
View the complete site [here](https://pitcherke.herokuapp.com/)


## Technologies Used
    - Python 3.6
    - Flask Framework
    - HTML, CSS and Bootstrap
    - Postgressql
    - Heroku


## Set-up and Installation
    1. Clone or download the Repo
    2. Create a virtual environment:
        sudo apt-get install python3.6-venv
        python3.6 -m venv virtual source virtual/bin/activate
    3. Read the specs and requirements files and Install all the requirements.
    4. Install dependancies that will create an environment for the app to run:
        pip3 install -r requirements
    5. Edit the start.sh file to prepare your environment variables:
        export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
        export SECRET_KEY='Your secret key'
        export MAIL_USERNAME='Your email'
        export MAIL_PASSWORD='Your email password'
    6. Run database migrations:
        python manage.py db init
        python manage.py db migrate -m "initial migration"
        python manage.py db upgrade
    7. Run chmod a+x start.py to make the app executable
    8. Run ./start.py
    9. Access the application through `localhost:5000`

### Contributions
Yet to complete all tests for each model class. If you have ideas you may contribute to this project.

## Known bugs
There is a problem with uploading the profile photo because of the csrf missing token.


## Contributors
    - Kevin Munene

### Contact Information
lukekevin39@gmail.com

### Licence
MIT license [here](https://raw.githubusercontent.com/muneneee/minute/master/LICENSE)
