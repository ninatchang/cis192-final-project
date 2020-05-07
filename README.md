# cis192-final-project: TODO list
## Project members
 - James Bigbee
 - Nina Chang
 - Subin Lee
## Demo Video
- < INSERT LINK HERE >
## Installation instruction
1. Run `pip3 install -r requirements.txt`
2. Run `python3 manage.py runserver`
## Code Structure
### Class definition
- Reminder
	- Magic methods
		- __ str __
		- __ timeRemaining __
### First class packages
- datetime: for easy calculations of time left to complete task
- random: for randomly generating tasks to complete
### Third class packages
- Django: for web framework
- Djongo: for storage on MongoDB
- humanfriendly: for human readable format of datetime
### Folder Structure
- user_management
	- contains code for user related code, such as log in, sign up, log out
- reminders
	- contains code for todo list related code, such as creating new tasks marking tasks as complete, generating random tasks to complete