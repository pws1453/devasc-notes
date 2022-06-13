import requests
import creds
import json

def getService(session : requests.Session):
    session.headers.update({"Content-Type":"application/yang-data+json"})
    req_url = f"{creds.STAN_URL}services/"
    print(req_url)
    return session.get(req_url,verify=False).json()

def main():
    session = requests.Session()
    session.auth = (creds.USER,creds.PASS)
    devInfo = getService(session)
    with open(f"services.json","w") as f:
        json.dump(devInfo,f,indent=3)

if __name__ == "__main__":
    main()