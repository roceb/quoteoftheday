#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import lxml
from pathlib import Path
from datetime import date
import os

today = date.today()
fileName =f'{today}.txt'
filepath = str(Path(__file__).parent.absolute()) + '/quotes/'
fileLocation = filepath+fileName


def fetch():
    wotdURL = "https://www.dictionary.com/e/word-of-the-day/"
    qotdURL = "http://api.quotable.io/random"

    # Check if folder exist. if it does not, create quote folder
    quoteDir = Path(filepath)
    if quoteDir.is_dir():
        pass
    else:
        os.mkdir(quoteDir)
    # Get quote

    qotdData = requests.get(qotdURL).json()
    quote = qotdData["content"]
    artist = qotdData["author"]

    class bcolors :
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        ITALIC = '\033[3m'

    #Get word
    wotdData = requests.get(wotdURL).content
    soup = BeautifulSoup(wotdData,"lxml")
    word = soup.find_all(class_ ="otd-item-headword__word")[0].h1.text.strip()
    pronunciation = soup.find_all(class_ ="otd-item-headword__pronunciation")[0].div.text.strip()
    form = soup.find(class_ ="otd-item-headword__pos").p.text.strip()
    definition = soup.find(class_ ="otd-item-headword__pos").find_all('p')[-1].text.strip()
    pronunciation = pronunciation[1:-1]

    with  open(fileLocation, "w+") as file_object:
        file_object.write(f'{bcolors.WARNING}"{quote}" {bcolors.ENDC}')
        file_object.write(f'by {bcolors.FAIL}{artist}')
        file_object.write('\n')
        file_object.write(f'{bcolors.BOLD}{bcolors.OKGREEN}{word}{bcolors.ENDC} ')
        file_object.write('\n')
        file_object.write(f'{bcolors.ITALIC}{pronunciation}{bcolors.ENDC} {bcolors.FAIL}{form}')
        file_object.write('\n')
        file_object.write(f'{bcolors.OKBLUE}{definition}{bcolors.ENDC} ')





my_file = Path(fileLocation)
if my_file.is_file():
    exit()
else:
    fetch()
