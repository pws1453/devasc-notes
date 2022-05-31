#   Common Architectural Styles
An application can expose an interface in a strange manner, but please don't.

##  RPC
RPC - Remote Procedure Call

*   Request-Response Model
*   Client-Server Model
    *   Both usually located on the same network
*   Client is usually unaware that the request is being executed remotely
*   RPC is mostly performed in a synchronous manner
    *   Asynchronous calls can be performed
*   RPC can be applied to different transfer protocols
    *   SOAP
    *   JSON-RPC
    *   XML-RPC
    *   NFS

##  SOAP
SOAP - Simple Object Access Protocol

*   XML-Based protocol developed by Microsoft
*   SOAP can be used by HTTP OR other protocols

Three Characteristics
*   Independent
    *   All types of apps can communicate with each other
*   Extensible
    *   SOAP just applies XML, and as such extensions can be built atop it
*   Neutral
    *   Can be used with any transport protocol (HTTP, SMTP, TCP, UDP, JMS)

### SOAP Messages
A SOAP message is an XML Document that can contain four elements
*   Envelope
    *   Must be root element of the XML Document
        *   Must be the thing everyone else is in
    *   Namespace provided that defines that XML is a SOAP Message
*   Header
    *   Optional element, must be the first element if used
    *   Application-specific information like authorization, SOAP attributes, or application attributes
*   Body
    *   Must be within it's own namespace
    *   Actual data to be sent to the recipient
*   Fault
    *   Optional element,m bust be a child of the body
    *   Only one of these can be present
    *   Provides error and status information

##  REST
REST - REpresentational State Transfer

Author: Roy Thomas Fielding
*   REST defined as a hybrid style
*   **Six constraints applied to elements within the architecture**
*   Client-Server
    *   Client and Server are independent of each other
*   Stateless
    *   Requests to server must contain all information server needs to make requests
    *   Server cannot contain session states
*   Cache
    *   Responses from the server must state whether response is cacheable
*   Uniform Interface
    *  **Four principles**
    *  Identification of resources
       *  Resource must be identified in the request as the individual object server manipulates
       *  Resource can be document, image, etc.
    *  Manipulation of resources through representation
       *  Client receives a representation of the resource from the server
       *  Must contain enough data or metadata so client may manipulate it
       *  Does not need to be a copy of the resource on the server
    *  Self-descriptive messages
       *  Message must contain enough information for recipient to process the image
       *  **Examples**
          *  Protocol type
          *  Data format of message
          *  Requested operation
    *  Hypermedia as engine of application state
        *  Data sent by server must include resources so client may access supplemental information
*   Layered System
    *   System made of different layers, where each provides to a layer above it
    *   Client
    *   Client + Cache
    *   Server
*   Code-On-Demand
    *   Optional
    *   REST service can include executable code
        *   Example: Payment services may use REST to display published javascript libraries for making payments
        *   

##  Example Messages

### SOAP

```
<?xml version="1.0"?>

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header/>
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>Query request too large.</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>
```