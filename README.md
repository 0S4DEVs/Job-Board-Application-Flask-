# Job-Board-Application-Flask-
This is a simple job board application built using Flask and SQLAlchemy. Employers can post job openings and job seekers can search for jobs based on keywords in the job title or description.

Getting Started
To get started, you'll need to do the following:

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Create a SQLite database by running python and then the following commands:
python
Copy code
from app import db
db.create_all()
Run the application using python app.py.
Navigate to http://localhost:5000 in your web browser to use the application.
Routes
The application consists of the following routes:

/
Displays a list of all the available jobs.

/add
Allows employers to post a new job opening.

/search
Allows job seekers to search for jobs based on keywords in the job title or description.

Templates
The application uses HTML templates for each of the routes. The templates are located in the templates folder. You can customize these templates as per your needs.

Models
The application uses a single model called Job. The Job model consists of the following fields:

id: The ID of the job.
title: The title of the job.
description: The description of the job.
employer: The employer of the job.
location: The location of the job.
salary: The salary of the job.
Contributing
If you find any issues or have suggestions for improvement, feel free to create a pull request or raise an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
