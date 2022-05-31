import json
import yaml
from os import path,mkdir
import requests

DEST = "./BASIC-IMAGES/"
ANIMALS = ["bird","dog","cat"]

"Convert boolean to string for use in url"
def btoS(boo):
    if boo:
        return "true"
    else:
        return "false"


"Convert valid animal string to API-compatible syntax"
def animalToParam(animal):
    "A good example of python's switch statemnents"
    match animal:
        case "dog":
            return "shibes"
        case "cat":
            return "cats"
        case "bird":
            return "birds"
        case _:
            print("animal is not valid")
            quit(0)

"Leverages Python's requests module to send HTTP GET requests"
"API Request syntax is here: https://shibe.online/"
def apiRequest(animal,count,urls,https):
    animal = animalToParam(animal)
    requestString = f"http://shibe.online/api/{animal}?count={count}&urls={btoS(urls)}&httpsUrls={btoS(https)}"
    resp = requests.get(requestString)
    return resp.text


"Grab binary representation of link from hosting provider"
def grabImage(links):
    return requests.get(links).content


def main(animal, count, urls, https):
    reldir = DEST+animal+"/"
    if path.exists(reldir):
        pass
    else:
        mkdir(reldir)
    stlinks = apiRequest(animal, count, urls, https)
    "Make JSON object from string"
    links = json.loads(stlinks)
    for link in links:
        filename = link.split("/")[-1]
        fullpath = reldir+filename
        if path.exists(fullpath):
            pass
        else:
            with open(fullpath,'wb') as f:
                content = bytes(grabImage(link))
                f.write(content)
    



if __name__ == "__main__":
    main("cat",10,True,True)