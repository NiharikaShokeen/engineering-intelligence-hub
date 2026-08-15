# Authentication

## Overview

TaskFlow uses JSON Web Tokens (JWT) to authenticate users. Authentication is handled by the Node.js and Express backend, while user account information is stored in PostgreSQL.

## User Registration

A new user can create an account by providing their name, email address, and password.

The backend validates the provided information before creating the account.

The user's password is never stored as plain text. Instead, it is securely hashed before being stored in the PostgreSQL database.

## User Login

When a registered user logs in, they provide their email address and password.

The backend checks whether the account exists and verifies the provided password against the stored password hash.

If the credentials are valid, the server generates a JWT for the user.

If the credentials are invalid, the login request is rejected.

## Password Storage

TaskFlow does not store passwords in plain text.

Passwords are converted into secure hashes before being stored in PostgreSQL. The original password cannot be retrieved from the stored hash.

## Authentication Token

After successful login, the server generates a JSON Web Token (JWT).

The client sends this token with requests to protected API endpoints.

The backend verifies the token before allowing access to protected resources.

## Token Expiration

JWTs have an expiration time.

When a token expires, the user must authenticate again to obtain a new token.

## Failed Login

If a user provides an incorrect email address or password, the backend rejects the login request.

The system does not reveal whether the email address exists in order to avoid exposing unnecessary account information.