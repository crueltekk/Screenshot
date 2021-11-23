import os.path
import wget
from gui import dldriver


def driverdownload():
    
    # Gets choosen webdriver from GUI and downloads it if file not exist
    
    url = f'https://www.geradedenken.net/privat/{dldriver}driver.exe'
    file = f'{dldriver}driver.exe'
    
    if os.path.isfile(f'{dldriver}driver.exe'):
        print('File already Downloaded')
    else:
        wget.download(url, file)