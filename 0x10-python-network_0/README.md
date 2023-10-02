# Hyper Text Transfer Protocol (HTTP)
This is an asymmetric request-response client-server protocol. It is a stateless protocol (The current request does not know what has been done in the previous requests)
## Uniform Resource Locator (URL)
```protocol://hostname:port/resource_path```
## HTTP Message
It consists of a message header and an optional message body separated by a blank line.  
### HTTP Request
#### Request Line
This is the first line of the request
```request-method request-URI HTTP-version```
##### Request methods
###### GET
Used to get a resource from the server
###### HEAD
Used to get the header that a get request would have obtained
###### POST
Used to post data to the web server
###### UPDATE
###### DELETE
###### PUT
###### OPTIONS
Ask the server to return a list of request methods it supports
###### CONNECT
Used to tell a proxy to make a connection to another host and simply reply the content without caching or parsing
#### Request Headers
```request-header-name: request-header-value1, request-header-value2, ...```  
An example of an HTTP request
```
GET /test.html HTTP/1.1
Host: www.xyz.com
Accept: image/gif, image/jpeg

optional body
```
### HTTP Response
#### Status Line
```HTTP-version status-code reason-phrase```
##### Status code
The status code is a 3-digit number:  
1xx (Informational): Request received, server is continuing the process.  
2xx (Success): The request was successfully received, understood, accepted and serviced.  
3xx (Redirection): Further action must be taken in order to complete the request.  
4xx (Client Error): The request contains bad syntax or cannot be understood.  
5xx (Server Error): The server failed to fulfill an apparently valid request.  
Common status-codes and reason-phrases  
200 - OK  
301 - Moved Permanently  
403 - Forbidden  
404 - Not Found  
#### Response Headers
```response-header-name: response-header-value1, response-header-value2, ...```
An example of an HTTP Response
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 75

<html>
<head>Hello World</head>
<body>
<h1>Hello World</h1>
</body>
</html>
```
