"""
Description: Imports stock portfolio values from a JSON file. Charts the stock-value distribution of investor's stock portfolio, displays data as pie-chart, and outputs PNG file. 

I/O Files: Loads JSON data from AllStocks.json - Outputs PNG file StockValueDistributionPieChart.png

Author: Robert Osborn
Last Revision: 6/7/2019
"""
try:
    import stockModule
    import json
    import matplotlib.pyplot as plt
    import matplotlib

    from datetime import datetime

    try:
        filepath = r"/Users/dreamcanvas/Desktop/python_work/AllStocks.json"

        with open(filepath) as f:
            dataSet = json.load(f)
        #Print to check if data received from JSON file. 
        #print(dataSet)
        
        try:
            stockDictionary = {}

            for stock in dataSet:
                if stock['Symbol'] not in stockDictionary:
                    #print(stock['Symbol'], stock['Close'], stock['Date'])
                    newStock = stockModule.Stock(stock['Symbol'])
                    #print(newStock.stockSymbol)
                    stockDictionary[stock['Symbol']] = {'stock': newStock}
                stockDictionary[stock['Symbol']]['stock'].addStockData(stock['Close'], datetime.strptime(stock['Date'], '%d-%b-%y'))


            label = [] #Labels for Pie-Chart
            value = [] #Closing Values of Stock Portfolio
            for stock in stockDictionary:
                close = stockDictionary[stock]['stock'].closePriceList
                #print(close)
                dates = matplotlib.dates.date2num(stockDictionary[stock]['stock'].stockDatePurchased)
                symbol = stockDictionary[stock]['stock'].stockSymbol

                label.append(symbol) #Adds each symbol to list for Pie-Chart
                value.append(close[-1]) #Grabs final stock value for each stock
            try:
                #Pie-Chart
                colors = ['lightblue', 'grey', 'gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'purple'] #Colors for Piechart
                plt.pie(value, labels=label, colors=colors, autopct='%1.1f%%', pctdistance=0.87, startangle=65) #Pie-Chart settings
                plt.axis('equal') #Top-down view of chart
                plt.title("Stock Portfolio Value Distribution") #Chart Title
                #Output
                
                plt.savefig('StockValueDistributionPieChart.png') #Saves output to .png file
                plt.show() #Displays chart
            except:
                print('There is an error displaying the graph.')
        except:
            print('There is an error iterating through JSON database data.')
    except:
        print('There is an error with the file. Check the filename or file location.')
except:
    print('Well this is embarassing. There is an error within the code.')

