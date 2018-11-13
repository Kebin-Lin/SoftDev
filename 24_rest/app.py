#Kevin Lin
#SoftDev1 pd6
#K 24: A RESTful Journey Skyward
#2018-11-14

import json, urllib
from flask import Flask, render_template
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def hello_world():
    url = "https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&cloud_score=True&api_key=Z9QhmJVYDfuFqx3hBYG9MhlRRJ3xPSu18wkfbsHd"
    response = urllib.request.urlopen(url)
    response = response.read()
    response = json.loads(response)
    cloudScore = response['cloud_score'] * 100
    return render_template('template.html', pic = response['url'], cloud_score = cloudScore)


if __name__ == "__main__":
    app.debug = True
    app.run()
