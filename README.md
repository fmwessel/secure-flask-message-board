# Secure Flask Message Board

A secure, full stack Flask web application that allows users to register, log in, and post messages to a community message board. The project is deployed on AWS EC2. 

## Features

- User registration, login, and logout
- Session-based authentication and access contol
- Message posting with username attribution
- HTML templates
- Public deployment on AWS EC2

## Tech Stack
- **Backend** Python, Flask
- **Frontend** HTML, CSS
- **Database** SQLite
- **Cloud** AWS EC2

## Security Considerations
- Session isolation to prevent users from accessing other users information
- Restricted access to authenticated users only
- Secure access to EC2 via key pairs
