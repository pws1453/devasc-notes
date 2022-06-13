# Networking For App Deployment
## Reverse Proxy
Regular proxy - makes all requests look like they come from the same client
Reverse proxy - makes all requests look like they come from the same server
All requests from the network go to the proxy, where they're evaluated and sent to the same internal server

## Firewall
Most basic defense against unauthorised access
**Most basic level**
* Accepts or rejects packets dependent on sc/dst IP and Port
* NGFW - Deeper application-level packet inspection
* Block based on protocol type as well
* Controls whether packets sent, and can modify them
* Separates internal/DMZ/external networks
* Presence on the network

**Things to keep in mind**
1. Keep any outside access to an untested app from occuring
2. Firewalls need to be configured so the app can be tested
3. Environment should be as close to prod asd possible, to catch firewall-related issues

## DNS
Converts hostnames to IP addresses and vice-versa
* MX - Mail Server
* SOA - Start of Authority
* NS - Name Server
* 
## Load Balancing
Takes requests, and balances them throughout many servers
### Strategies
1. Persistent sessions
    * If a user requires a persistent session, load balancer sends to server handling the session 
3. Round Robin
    * Server sends requests to "next" server on the list 
4. Least Connections
    * Send requests to leadt busy server
5. IP Hash
    *  Destination dependent on hash of source IP
    *  Simple way to maintain persistent sessions
6. Blue-Green Deployment
    * Applies changes to a new production (blue)
    * Rather than making them to old production (green)
    * Load balancer sends to blue when it is ready
    * Can rollback if neccesary 
7. Canary Deployment
    * Divert small amount of traffic to new prod (blue)
    * Increase traffic diverted until issues are detected, or all on new
    * Once all on new, old one is retired or used again 