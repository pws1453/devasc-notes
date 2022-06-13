# HTTP Overview
**Application-level protocol**
Based on a client/server model
Any type of data can be sent
* Client and server must know how to handle the data

## Request-Response Cycle
1. Client sends req to server
2. Server recieves req
3. Server processes req
4. Server sends repsonse
5. Client recieves response

## HTTP Request
___
**Request Line**
* {METHOD [GET/POST/PUT]} {Resource} {Protocol_version}
—
**Request Headers**
—
line
—
**Request Body**
Only used when applicable. Content-Type must be specified
___

## HTTP Response

___
**Response Line**
* {Protocol_version} {Response_Code} {Reason}
—
**Response Headers**
—
line
—
**Response Body**
Only used when applicable. Content-Type must be specified
___

## HTTP URLs
Componsed from URI Components
* Scheme -> identify the type of data and how it should be handled
* Host -> UJRL host can be FQND or IP Address
* Port -> Connection port number
* Resource path -> Path segments diovided by forward-slashes
* Query parameters -> Optional parameters separated by key/value. Often used by GET requests
* Fragment -> Optional parameters that provide the client direction to a secondary resource

URI -> Identifies a resource
* ../people/alice
URL -> Locates the resource
* http://www.example.com/people/alice.

## HTTP Methods
* GET -> Get user info
* POST -> Create user
* PUT -> Replace the user
* PATCH -> Update the user
* DELETE -> Delete the user
* HEAD -> Only headers sent

## HTTP Status Code