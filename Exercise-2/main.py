import requests
import pandas as pd
from bs4 import BeautifulSoup
import os


def main():
    PATH = os.getcwd() + '\Responses'
    os.makedirs(PATH, exist_ok=True)
    URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    page = requests.get(URL)
    #print(page)
    if page.ok:
    
        #Parse page with beautiful soup to get the right tag
        soup = BeautifulSoup(page.content, "html.parser")
        element = soup.find(
            "td", string=lambda text:"204k" in text.lower()
        )
        element = element.parent.find("a").attrs['href']
        
        #Download the file from the tag using the site url + filename
        downloadURL = URL + element
        #print(downloadURL)
        climateCSV = requests.get(downloadURL)
        
        #Downloading data
     
        #Creating specific path the for the data based on it's filename
        #Saving data to file
        pathToCSV = PATH + '\\Ding.csv'
        with open(pathToCSV, 'wb') as fp:
            fp.write(climateCSV.content)
            
        #Load the file into pandas
        data = pd.read_csv(pathToCSV)
        #print(data.max)
        dota = data.loc[data['HourlyDryBulbTemperature'] ==
                        data['HourlyDryBulbTemperature'].max()]
        print(dota['HourlyDryBulbTemperature'])

        #2021-07-26T11:00:00
    else: 
        pass
    
    ###
    #print(climateFile)
    #pass


if __name__ == "__main__":
    main()
