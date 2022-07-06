import json
import yaml
import creds
import requests
import urllib3


def getToken(session: requests.Session):
    """
    Get a token from DNA Cemter using given credentials
    Params:
        Session:    Session object from Requests Library
    Return:
        Token:      Token from DNA Center appliance
    """
    auth_url = creds.URL + "/dna/system/api/v1/auth/token"
    session.headers.update({"Content-Type": "application/json"})
    session.auth = (creds.UNAME, creds.PASS)
    res = session.post(auth_url, data=None, verify=False).json()
    return res["Token"]


def getDevices(session: requests.Session, config):
    """
    Get device information from DNA Center using specified IP Addresses
    Params:
        Session:    Session object from Requests Library
        config:     Python Dictionary loaded from YAML
    Return:
        retDict:    Python Dictionary containing configuration information
    """
    retDict = []
    count = 0
    for addr in config["deviceCollection"]["ipAddresses"]:
        dev_url = creds.URL + "/dna/intent/api/v1/network-device"
        if type is not None:
            req_url = f"{dev_url}?managementIpAddress={addr}"
        else:
            req_url = dev_url
        fulljson = session.get(req_url, verify=False).json()
        response = fulljson["response"][0]
        retDict.append(dict())
        retDict[count]["id"] = response["id"]
        retDict[count]["addr"] = addr
        retDict[count]["role"] = response["role"]
        retDict[count]["type"] = response["type"]
        retDict[count]["softwareType"] = response["softwareType"]
        retDict[count]["softwareVersion"] = response["softwareVersion"]
        retDict[count]["macAddress"] = response["macAddress"]
        count += 1
    return retDict


def getDeviceConfig(session: requests.Session, devInfo: dict):
    """
    Writes configuration information to a device-specific file
    Params:
        Session:    Session object from Requests Library
        config:     Python Dictionary containing configuration information
    Return:
        None
    """
    for addr in devInfo:
        id = addr["id"]
        add = addr["addr"]
        with open(f"{add}-config.json", "w") as f:
            vlan_url = creds.URL + f"/dna/intent/api/v1/network-device/{id}/config"
            conf = session.get(vlan_url, verify=False).json()
            conf = conf | addr
            json.dump(conf, f, indent=3)


def main():
    session = requests.Session()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    token = getToken(session)
    session.headers.update({"X-Auth-Token": token})
    with open("config.yaml", "r") as f:
        devInfo = getDevices(session, yaml.safe_load(f))
    getDeviceConfig(session, devInfo)


if __name__ == "__main__":
    main()
