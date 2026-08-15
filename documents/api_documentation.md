# API Documentation

## Base URL

The TaskFlow API is served through the backend application.

For local development, the API is available at:

http://localhost:3000/api

## Authentication

Protected endpoints require a valid JWT.

The token must be included in the Authorization header:

Authorization: Bearer <token>

Requests without a valid token receive a 401 Unauthorized response.

## User Registration

### POST /api/auth/register

Creates a new TaskFlow user.

Required fields:

- name
- email
- password

A successful registration returns a 201 Created response.

If the email address is already registered, the API returns a 409 Conflict response.

## User Login

### POST /api/auth/login

Authenticates an existing user.

Required fields:

- email
- password

A successful login returns a JWT.

If the credentials are incorrect, the API returns a 401 Unauthorized response.

## Get Current User

### GET /api/users/me

Returns information about the currently authenticated user.

This endpoint requires a valid JWT.

## Create Task

### POST /api/tasks

Creates a new task for the authenticated user.

Required fields:

- title
- description
- dueDate

This endpoint requires authentication.

A successful request returns a 201 Created response.

## Get Tasks

### GET /api/tasks

Returns the tasks accessible to the authenticated user.

This endpoint requires authentication.

## Update Task

### PUT /api/tasks/:id

Updates an existing task.

The user must be authenticated and have permission to modify the requested task.

A successful update returns a 200 OK response.

## Delete Task

### DELETE /api/tasks/:id

Deletes a task.

The user must be authenticated and have permission to delete the requested task.

A successful deletion returns a 204 No Content response.