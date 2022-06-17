import json
import requests
import creds

def userLogin(name,password,ses):
    userAttrs = dict()
    userDict = dict()
    userAttrs["attributes"] = {"name": name, "pwd": password}
    userDict["aaaUser"] = userAttrs
    return ses.post(creds.URL+"/api/aaaLogin.json",json=userDict,verify=False)


def fabricAppQuery(session):
    res = session.get(creds.URL+"/api/class/fvAp.json",verify=False)
    return res.text

def main():
    ses = requests.Session()
    print(userLogin(creds.LOGIN,creds.PASSWORD,ses))
    with open("basic.json","w") as f:
        faq = fabricAppQuery(ses)
        js = json.loads(faq)
        json.dump(js,f)



if __name__ == "__main__":
    main()