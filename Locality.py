#packages
import webview as web
import easygui as gui
import requests as req
import urllib.parse as url
from bs4 import BeautifulSoup
import os
import getpass

#settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

#ask for choice
option = gui.buttonbox('Pick an action to do on your Locality Browser!\nBrowsing Online requires Internet, but you can access anything.\nDownloading also requires Internet, but once you download it, you can access it offline using Browse Offline.\nBrowse Offline requires no Internet, but you have to download the website first.', 'Locality', ('Browse Online', 'Download', 'Browse Offline'))

#button options
if option == "Browse Offline":

    #get url
    offlinelink = gui.enterbox("Enter the URL to your offline website. Please include the protocol.", "Offline", "https://")

    #find file
    encodedlink = str(url.quote_plus(offlinelink))

    file_path = "/Users/" + str(getpass.getuser()) + "/Documents/Locality Websites/" + encodedlink + "/locality.txt"

    #read and open file
    with open(str(file_path), "r") as f:
        file = f.read()
    
    #render window
    web.create_window('Offline Browsing', html = str(file))
    web.start()
elif option == "Download":

    #get link
    downloadlink = gui.enterbox("Enter the URL of the website you would like to download. Please include the protocol.", "Download", "https://")

    #focus onto user directory
    home_dir = os.path.expanduser("~")

    #create files necessary
    documents_dir = os.path.join(home_dir, "Documents")
    downloads_folder = os.path.join(documents_dir, "Locality Websites")
    os.makedirs(downloads_folder, exist_ok=True)

    #format and write file contents
    encoded_url = url.quote_plus(downloadlink)
    url_folder = os.path.join(downloads_folder, encoded_url)
    os.makedirs(url_folder, exist_ok=True)
    file_path = os.path.join(url_folder, "locality.txt")
    download = req.get(str(downloadlink))
    download = download.content
    finaldownload = BeautifulSoup(download, "html5lib")

    #create file
    with open(file_path, 'w') as f:
        f.write(str(finaldownload))

    #alert user that the process has finished
    gui.msgbox('Website Downloaded', 'Hey!')
elif option == "Browse Online":
    #opens website
    onlinelink = gui.enterbox("Enter the URL of the online website. Please include the protocol.", "Online!", "https://")
    web.create_window('Online Browsing', str(onlinelink))
    web.start()
else:
    pass
