#   Introduction to webhooks
Webhook - HTTP Callback to a specifried URL that notifies your app when an event has occurred

##  Why use a webhook?
Webhooks enable apps to get real-time data when they're triggered by particular activities or events.
Apps are more efficient when they do not need to poll a service.
Webhooks are called "reverse APIs" as applications subscribe to a webhook server by registering with the webhook provider
Application porovides a URI to be called by the server when the target event or activity occurs
* URI is usually an API that the application hosts
### When the webhook is triggered
1. Server sends a notification by sending a request to the URI
2. Application consumes the request
**Roles are reversed from traditional API roles**
## Consuming a webhook
To recieve a notification from a provider, application must meet requrements
* Must always run to recieve requests
* Must register a URI on the provider, so it knows where to send a notification when events occur
* Must handle notifications from the webhook server

### Debugging functionality
Free onloine tools that makes sure application can recieve notifications