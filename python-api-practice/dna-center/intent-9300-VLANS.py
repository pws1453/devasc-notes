import json
import creds
import requests


def getToken(session : requests.Session):
    auth_url = creds.URL+"/dna/system/api/v1/auth/token"
    session.headers.update({"Content-Type":"application/json"})
    session.auth = (creds.UNAME,creds.PASS)
    res = session.post(auth_url,data=None,verify=False).json()
    return res["Token"]

def getDeviceList(session : requests.Session, type):
    dev_url = creds.URL + "/dna/intent/api/v1/network-device"
    if type is not None:
        req_url = f"{dev_url}?type={type}"
    else:
        req_url = dev_url
    return session.get(req_url,verify=False).json()

def getDeviceVLAN(id,session : requests.Session):
    vlan_url = creds.URL + f"/dna/intent/api/v1/network-device/{id}/vlan"
    return session.get(vlan_url,verify=False).json()

def getDeviceHealth(session : requests.Session):
    health_url = creds.URL + "/dna/intent/api/v1/device-health"
    return session.get(health_url,verify=False).json()

def main():
    session = requests.Session()
    token = getToken(session)
    session.headers.update({"X-Auth-Token":token})
    type = "Cisco Catalyst 9300 Switch"
    fulljson = getDeviceList(session,type)
    response = fulljson["response"]
    with open("9300.json","w") as f:
        json.dump(response,f,indent=4)
    with open("vlan.json","w") as f:
        for device in response:
            json.dump(getDeviceVLAN(device["id"], session),f,indent=4)
    with open("health.json","w") as f:
        json.dump(getDeviceHealth(session),f,indent=4)
        


if __name__ == "__main__":
    main()