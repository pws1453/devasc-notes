import requests
import creds
import json

def getDevice(deviceName,session : requests.Session):
    session.headers.update({"Content-Type":"application/yang-data+json"})
    req_url = f"{creds.STAN_URL}devices/device={deviceName}/config"
    print(req_url)
    return session.get(req_url,verify=False).json()

def main():
    session = requests.Session()
    session.auth = (creds.USER,creds.PASS)
    device_name = "dist-rtr01"
    devInfo = getDevice(device_name,session)
    with open(f"devInfo-{device_name}.json","w") as f:
        json.dump(devInfo,f,indent=3)

if __name__ == "__main__":
    main()