import requests
import creds

session = requests.Session()
session.headers.update({"Authorization":f"Bearer {creds.TOKEN}"})

def getMyInfo():
    return session.get("https://webexapis.com/v1/people/me").json()

def getMemberships(id):
    return session.get("https://webexapis.com/v1/memberships").json()

def main():
    id = getMyInfo()["id"]
    getMemberships(id)
    

if __name__ == "__main__":
    main()