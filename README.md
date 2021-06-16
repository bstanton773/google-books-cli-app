# google-books-cli-app with Python and Flask
The goal of this project was to make a CLI app that accesses the Google Books API. A user can search for books in the command line and add one of the books from the search to a reading list.

## Technologies
* Flask - a microframework written in Python
* Flask-SQLALchemy - A Python SQL toolkit

## System Requirements
`python3` and `pip` should be installed

## Installing modules
1. Create a new virtual environment with `python3 -m venv venv`
2. Activate the virtual environment with `. venv/bin/activate` (for Mac) or `. venv/Scripts/activate` (for Windows)
3. `pip install -r requirements.txt`

## Setting up the SQLAlchemy database
1. Make a `.env` file outside of the app folder
2. Copy and paste these credentials into the `.env` file

`SECRET_KEY=b'\xb6{s\x9f\xb1\x1b~\xf3K\xb2\xd8\xf7Z\xb7\xadw\xbd2\xeas\x83\xc3h\xc5'`
`FLASK_APP=run.py`
`FLASK_ENV=development`
`SQLALCHEMY_DATABASE_URI=postgres://ofhyfytu:WB090jjikVe_B0pKJ7SSSikr1gtCsKRv@batyr.db.elephantsql.com/ofhyfytu`
`SQLALCHEMY_TRACK_MODIFICATIONS=False`

Note: These credentials are for testing purposes. Normally the Secret Key and database URI would not be accessible for security. This will connect you the SQL database where the books from the reading list are being stored.

3. In your terminal type: `flask db init` then `flask db migrate && upgrade`. If it does not work, type in `flask db stamp head` and try the init, migrate, and upgrade steps again.

## Command to search Book Titles
`flask google search '<book title>'`  
  
* Example: `flask google search 'Python Crash Course'`

## Next steps
1. The instructions in the terminal will prompt you to type in a number from 1-5 that corresponds with the book title you would like to add.
2. Once you enter the number, the book will be added to your reading list and the books inside your reading list will be printed in the terminal.