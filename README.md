# Applegate Park Zoo Web Application

This project was started to develop a Web Application for Applegate Park Zoo at mercedzoo.org.  

## Getting Started

In order to store a local copy of the repository, clone it into the desired directory with the line

```
git clone https://github.com/karnaerrande/Zoo-Project.git
```

### Prerequisites

The prerequisites of this application are the latest Python 3 release, flask, flask_wtf, flask_sqlalchemy, google-auth, and google-api-python-client flask_bcrypt 

You can install the packages with the line below.

```
pip install Flask Flask-WTF Flask-SQLAlchemy google-auth google-api-python-client flask_bcrypt

```

### How to run the project

First navigate to the project's root directory within a terminal.

Second, run the below line to run the Web Application

```
python run.py
```

And then open your Web Browser and navigate to 

```
localhost:5000
```

Or replace 'localhost' with your IPv4 address to access the site from other devices on your network

### How to access the admin page

At the bottom of each page is a button labeled "Admin Portal"

Once at the following page, enter the password you set or "MercedZoo2019" as default 

### How to change the admin password

At line 38 in the "run.py" file, replace 'MercedZoo2019' with the desired password
