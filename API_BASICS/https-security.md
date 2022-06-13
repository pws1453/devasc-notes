# HTTP Security Concerns
* **HTTPS spoofing:** Can be used to send fake certificates to the client, thus making the client trust your connection as the real one.
    
* **SSL hijacking:** Describes copying fake authentication keys to the client and server, having full access to the communication channel.
    
* **SSL Stripping:** Tries to convert the HTTPS connection to a regular HTTP by interrupting the TLS handshake and exploiting redirects.
    
* **Downgrade attacks:** Focus on abusing backward compatibility, which many protocols feature. It tries forcing the system to fall back to an older or less protected version of software in order to exploit any known vulnerabilities that they feature.
    
* **Exploiting software bugs:** Can have disastrous consequences, as was seen with the Heartbleed bug that exploited a vulnerability in OpenSSL library.
    
* **Phishing attacks:** Used to try to trick the user into accepting some fraudulent certificates as trusted (either with fake websites or fake emails).