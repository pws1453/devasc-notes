import json
from time import sleep
import creds
import requests

def getNets(org,session):
    url = creds.BASE_URL + f"/organizations/{org}/networks"
    js = json.loads(session.get(url).text)
    nets = []
    for item in js:
        netID = item["id"]
        nets.append(netID)
    return nets

def getOrgs(session):
    url = creds.BASE_URL+"/organizations"
    res = session.get(url).text
    hs = json.loads(res)
    orgs = []
    for thing in hs:
        orgs.append(thing["id"])
    return orgs

def getDevices(net,session):
    url = creds.BASE_URL+f"/networks/{net}/devices"
    js = json.loads(session.get(url).text)
    for device in js:
        if 'lanIp' in device:
            devIP = device["lanIp"]
        elif 'wan1Ip' in device:
            devIP = device["wan1Ip"]
        else:
            devIP = device["address"]
        model = device["model"]
        if 'name' not in device:
            devName = "anonymous"
        else:
            devName = device["name"]
        print(f"Device named {devName} with IP {devIP} is a Cisco Meraki {model}")

def main():
    session = requests.Session()
    session.headers.update({"X-Cisco-Meraki-API-Key":creds.API_KEY})
    orgs = getOrgs(session)
    for org in orgs:
       nets = getNets(org,session)
       for net in nets:
           getDevices(net,session)
           sleep(0.5)


if __name__ == "__main__":
    main()

    