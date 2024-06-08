# Social Networking API

A Django Rest Framework-based social networking API with user authentication, friend request functionality, and search capabilities.

## Features

- User Signup/Login
- Search users by email and name
- Send/Accept/Reject friend requests
- List friends
- List pending friend requests
- Rate limiting on friend requests (max 3 per minute)

## Requirements

- Python 3.11
- Django 5.0.6
- Django Rest Framework
- SQLite (default database)

## Installation

1. **Clone the repository:**
   
   git clone https://github.com/kharishgit/socialmedia.git
   cd social_network

2. **Create and activate a virtual environment**
   
    `python -m venv venv`
    `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**

    pip install -r requirements.txt

4. **Apply database migrations**

    python manage.py migrate

5. **Create a superuser**

    python manage.py createsuperuser

6. **Run the development server**

    python manage.py runserver

## DOCKER SETUP - You can also run this application using Docker

1. **Build and start the containers**

    docker-compose up --build




## Postman Collection

    https://elements.getpostman.com/redirect?entityId=22783304-c2acca3c-749f-410c-a11f-4e1854bd16c6&entityType=collection

## API Endpoints

    Signup: /social/signup/ [POST]
    Login: /social/login/ [POST]
    Search Users: /social/search/ [GET] In params (key='query' value="String to search")
    Send Friend Request: /social/friend-request/send/ [POST]
    Accept Friend Request: /social/friend-request/accept/{request_id}/ [POST]
    Reject Friend Request: /social/friend-request/reject/{request_id}/ [POST]
    List Friends: /social/friends/ [GET]
    List Pending Friend Requests: /social/friend-requests/pending/ [GET]


