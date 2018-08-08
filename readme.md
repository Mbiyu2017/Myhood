# My Hood
#### A django web app that informs a user about their neighbourhood, 3/8/2018
#### By **Ben Mbiyu**
## Description
* The application enables users to keep updated about what is going on in their Neighbourhood
* To be a user, one must first sign up to the application.
* When a user sign's up, an email with an activation link is sent to the user's email.
* To activate a one's account a user needs to click the link sent in the email to activate their account.
* After succefully activating one's account,a profile is automatically created for the user.  
* The user needs to now login to the app using the credentials they supplied at sign up
* Once loggged in a user can see all the neighbourhoods available on the website.
* If a user feels that their neighbourhood is not represented, they can add it from the form on the left of the landing page
* Once a neighbourhood exists, a user can hence join the neighbourhood by clicking on it.
* When a user joins a neighbourhood, they can view updates or events that relate to the neighbourhood
* If a user has an event that they want to post to the neighbourhood, then they can add the event including its image from the form on the left of the neighbourhood page.

## Setup/Installation Requirements
* Create an empty folder in your preferred location on your computer
* create a virtual environment in that virtual environment using python3.6.
  ```bash
    python3.6 -m venv virtenv
  ```
* Activate the virtual environment
  ```bash
    source virtenv/bin/activate
  ```
* clone the repository from 'https://github.com/Mbiyu2017/Myhood.git'
* Create a `.gitignore` file in your project root and include the virtual environment inside the file
* Install the dependecies listed in requirements.txt file
  ```bash
      pip install -r requirements.txt
  ```
* Choose the database of your choice to connect to the app. Personally I used postgres for this project.
* If you choose to use postgres, you'll need to install the CLI for postgres then go to you terminal and create a database for the app.
* To connect to postgres
  '''bash
    psql
  '''
* To create the database
  ```bash
    CREATE DATABASE <name_of_database>
  ```
* After creating a database, exit the psql terminal by CRTL+D then make migrations.
*
  ```bash
   python manage.py makemigrations
  ```
* Migrate the changes to the database
```bash
  python manage.py migrate
```
* Run the server to run the app from local host
```bash
  python manage.py runserver
```
* You can now use the app
## Known Bugs
* There are no known bugs affecting the application for now, but some great features are underway and being worked on

## Technologies Used
* Python
* Django web framework
* Semantic UI

## Support and contact details
* Incase of contributions to the application or bugs you run through in the app, feel free to collaborate and github ```Mbiyu2017``` or reach me on email ben.the.dev@gmail.com
### License
*Copyright 2018 Ben Mbiyu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*
Copyright (c) 2018 **Ben Mbiyu**
