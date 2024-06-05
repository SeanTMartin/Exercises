import requests
import os
import zipfile
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]
## /FOR ME TO RUN BY ITSELF - download first file
# print(download_uris[0])
# response = requests.get(download_uris[0])
# print (response.url)
# print(response.status_code)
# x = response.content
# os.listdir()
# x = response.headers

# with open('newFile.zip', 'wb') as fp:
#         fp.write(response.content)



 
#End of testing zone /
PATH = os.getcwd() + '\Responses'

def main():
    
    #If 'Downloads' folder doesn't exist in this directory, make it.
    os.makedirs(PATH, exist_ok=True)
    #Getting data from download_uris
    for i in download_uris:
        #Check if data is legit
        response = requests.get(i)
        #Downloading data
        if response.ok: 
            #Creating specific path the for the data based on it's filename
            cleanFileName = response.url.split('/')[3]
            newPath = PATH + '\\' + cleanFileName
            #Saving data to file
            with open(newPath, 'wb') as fp:
                fp.write(response.content)
            #Unzipping data
            with zipfile.ZipFile(newPath, 'r') as zip_ref:
                 zip_ref.extractall(path=PATH)
        else: 
            pass
#Delete zip files
forDeletion = os.listdir(PATH)
for i in forDeletion:
    if i.endswith('.zip'):
        os.remove(PATH + '\\' + i)


if __name__ == "__main__":
    main()
