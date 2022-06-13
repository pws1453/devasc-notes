import json
import requests
import creds

def getAuthToken(session : requests.Session):
    fullurl = f"{creds.HOST}/j_security_check"
    dicload = {'j_username': creds.USER,'j_password':creds.PASS}
    # sends as formencoded rather than JSON
    resp =  session.post(fullurl,data=dicload,verify=False)
    return resp.cookies.get_dict()["JSESSIONID"]

def csrf(session : requests.Session):
    fullurl = f"{creds.HOST}/dataservice/client/token"
    getAuthToken(session)
    resp = session.get(url=fullurl,verify=False)
    session.headers.update({"X-XSRF-TOKEN":resp.text})


def getDevice(session : requests.Session):
    fullurl = f"{creds.HOST}/dataservice/device"
    resp = session.get(fullurl,verify=False)
    return resp.json()

def main():
    session = requests.Session()
    csrf(session)
    print(getDevice(session))

    


if __name__ == "__main__":
    main()