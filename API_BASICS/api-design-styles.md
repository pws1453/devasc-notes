#   API Design Styles

##  Synchronous APIs
These APIs respond to a request directly, often providing data
*   Enable application to immediately receive data
*   Application must wait for API before executing additional code
*   Relatively standardized at this point

##  Asynchronous APIs
These APIs will send one response to confirm receipt, and will send another when the data has been recieved
*   Often used when an API needs to perform additional processing
*   Application can continue without being blocked
*   Client may to use special implementation for each API
    *   Response Queue?
    *   Polling Mechanism?