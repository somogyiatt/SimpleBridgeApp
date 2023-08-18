# SimpleBridgeApp

## Table of Contents

1. **Introduction**
2. **Installation**
3. **Usage**
    - Running the Django Project
    - Setting Up the Frontend
4. **HTTP Gateway**
5. **WebSocket Consumer**
6. **Error Handling**
7. **Logging**
8. **Testing**
9. **Frontend Integration**

## 1. Introduction

The WebSocket JSON Bridge project aims to provide a seamless connection between HTTP and WebSocket protocols, enabling HTTP and WebSocket communication between clients and server. This documentation outlines the installation, usage, and components of the project.

## 2. Installation

To get started, follow these steps to set up the project:

| Package         | Version |
|-----------------|---------|
| Python        | 3.10   |
| Django          | 4.2     |
| django-cors-headers  | 4.2.0    |
| channels | 4.0.0   |
| channels-redis | 4.1.0 |
| daphne | 4.0.0 |

```bash
$ git clone https://github.com/somogyiatt/SimpleBridgeApp.git
$ cd json-bridge_app
$ pip install Django
$ pip pip install django-cors-headers
$ pip install channels
$ pip install channels-redis
$ pip install daphne
```

## 3. Usage
Running the Django Project
To run the Django project, use the following command:

```bash
$ daphne json_bridge_app.asgi:application
```
This command will start the Django application and allow the HTTP to WebSocket gateway to operate.

Setting Up the Frontend
Install XAMPP to serve the frontend locally.
Clone the WebSocket Frontend Repository.
Place the cloned repository inside the XAMPP htdocs directory.
Set XAMPP port to 8001.
Access the frontend using the URL: http://localhost/websocket-frontend.

## 4. HTTP Gateway
The HTTP gateway (http_gateway function in views.py) exposes the /api/ui/ endpoint to receive HTTP POST requests containing JSON content. It forwards the JSON data to the WebSocket server and sends back the JSON response to the http client without changing it.

## 5. WebSocket Consumer
The WebSocket consumer (WebSocketConsumer class in consumers.py) handles WebSocket connections, receives JSON data, and sends it back to the client. It also listens for events and sends data to the WebSocket server.

## 6. Error Handling
Errors are handled in the http_gateway function using try-except blocks. Example the invalid JSON data results in a 400 Bad Request response.

## 7. Logging
The project implements logging for different scenarios, including HTTP requests and WebSocket events. Logs are output to the console.

## 8. Testing

The project includes automated tests to ensure the functionality and reliability of the components. To run the tests, execute the following command:

```bash
$ python manage.py test
```

This command will trigger the test suite and display the results in the terminal. The tests cover various aspects of the project, error handling.

## 9. Frontend Integration
The frontend provides a user-friendly interface for sending HTTP POST requests and receiving WebSocket messages. It displays sent and received JSON data side by side.
