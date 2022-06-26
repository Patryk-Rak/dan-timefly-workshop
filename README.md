
# Dan Timefly Workshop
#### **CURRENT STATUS - WORK IN PROGRESS**

This is my first attempt at creating a website from scratch to production stage,
hosting it using Heroku, based on my previous knowledge with many small projects
using Python + Django.

The idea for the website was actually pretty simple and came from the desire to
showcase my hobby collection of 3d printed and painted figurines.

The site has only one user, the administrator, who manages all the content of
the site - from posting new figures along with the photo gallery, to building
a database of paints and tools used to complete the model / diorama.

The site also has a contact form, information about the creator,
description of services and the potential for expanding the site to include
tutorials on miniature painting.


## Screenshots
Home page
![App Screenshot](https://i.imgur.com/7TyiSTK.png)
Porftolio page
![App Screenshot](https://i.imgur.com/F5Pzefa.png)
Portfolio details
![App Screenshot](https://i.imgur.com/5p6wbXr.png)


## Features

- Portfolio database with CRUD (50% finished)
- Model details overview (70% finished)
- Contact Form (10% finished)
- Admin content control (100% finished)
- Interactive services page (0% finished)


## Roadmap

- Additional browser / filter support when searching figures

- Implement Django REST Framework

- Make working Contact Form

- Make something similar to Wordpress CMS tool for creating tutorial pages on one template


## Tech Stack

**Client:** Python, Django, TinySQL (for testing, intended to use with Mysql)

**Server:** Gunicorn, Heroku


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY` - django key for project to work

## Lessons Learned

---


## Authors

- [@Patryk Rak](https://github.com/Patryk-Rak)

