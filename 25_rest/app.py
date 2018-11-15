#Kevin Lin
#SoftDev1 pd6
#K 25: Getting More REST
#2018-11-15

import json, urllib
from flask import Flask, render_template
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def home():
    symbolSel = "MSFT"
    apiKey = "Z9QhmJVYDfuFqx3hBYG9MhlRRJ3xPSu18wkfbsHd"
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(symbolSel,apiKey)
    response = urllib.request.urlopen(url)
    response = response.read()
    response = json.loads(response)
    currPrice = response["Global Quote"]["05. price"]
    openPrice = response["Global Quote"]["02. open"]
    highPrice = response["Global Quote"]["03. high"]
    lowPrice = response["Global Quote"]["04. low"]
    return render_template('template.html', symbol = symbolSel, curr = currPrice, openP = openPrice, high = highPrice, low = lowPrice)


if __name__ == "__main__":
    app.debug = True
    app.run()
