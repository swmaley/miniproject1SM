# INF601 - Advanced Programming in Python
# Spencer Maley
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

#Get closing price for last 10 trading days
def getClosing(ticker):
    #get closing price for last 10 days
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    #Loop through closing prices and add to list
    for price in hist['Close']:
        closingList.append(price)

    return closingList

def printGraph(stock):

    stockClosing = np.array(getClosing(stock))

    len(stockClosing)

    days = list(range(1, len(stockClosing) + 1))

    # Plots graph
    plt.plot(days, stockClosing)

    # low and high for y
    prices = getClosing(stock)
    prices.sort()
    low = prices[0]
    high = prices[-1]

    # Set axis
    plt.axis([1, 10, low - 1, high + 1])

    # labels for graph
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # saves graphs
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # shows graph
    plt.show()


def getStocks():

    #define stocks
    stocks = []
    print("Please enter 5 stocks to graph")
    for i in range(1,6):

     while True:
        print("Enter stock ticker number " + str(i))
        ticker = input("> ")
        try:
            print("Checking ticker.")
            stock = yf.Ticker(ticker)
            stock.info
            stocks.append(ticker)
            print("Valid ticker.")
            break
        except:
            print("That is an invalid stock. Please try again.")

    return stocks



#start of program
 # create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass
for stock in getStocks():
    getClosing(stock)
    printGraph(stock)




