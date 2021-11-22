import os.path
import wget

def download():
    url = 'https://www.geradedenken.net/privat/chromedriver.exe'
    file = 'chromedriver.exe'

    if os.path.isfile('chromedriver.exe'):
        print('File already Downloaded')
    else:
        wget.download(url, file)