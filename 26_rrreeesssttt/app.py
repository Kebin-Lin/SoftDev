#Kevin Lin
#SoftDev1 pd6
#K 26: Getting More REST
#2018-11-16

import json, urllib, random
from flask import Flask, render_template
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def home():
    #Gets the amount of art the API can use
    numObjects = json.loads(urllib.request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects").read())["total"]
    randomArt = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    toDisplay = ""
    while True:
        #Until a displayable piece is selected, look for a new piece of art
        #Image will be squished to 200x200px
        artUrl = randomArt + str(random.randint(1,numObjects+1))
        try:
            toDisplay = json.loads(urllib.request.urlopen(artUrl).read()) #Dictionary for a randomly selected piece of art
        except:
            continue
        if toDisplay["primaryImage"] != "": break

    #Stuff to do if bored
    boredActivity = json.loads(urllib.request.urlopen("https://www.boredapi.com/api/activity").read())["activity"]

    #Chuck Norris Joke (Explicit jokes filtered out)
    chuckNorris = json.loads(urllib.request.urlopen("http://api.icndb.com/jokes/random?exclude=[explicit]").read())["value"]["joke"]

    return render_template('template.html', artLink = toDisplay["primaryImage"], artTitle = toDisplay["title"], activity = boredActivity,
                                            chuckJoke = chuckNorris)




if __name__ == "__main__":
    app.debug = True
    app.run()
