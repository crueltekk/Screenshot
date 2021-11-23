import os
from pathlib import Path
import schedule
from time import sleep
from takescreenshot import take_screenshot
from gui import load
import download

class Main():

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    if load == True:
        download.driverdownload()
        print('Download start')
    else:
        print('Oh not, you have to fix something')

    Path('screens').mkdir(parents = True, exist_ok = True)
    Path('screens/spawn').mkdir(exist_ok = True)
    Path('screens/stigga').mkdir(exist_ok = True)

    schedule.every(5).seconds.do(take_screenshot)
    while True:
        schedule.run_pending()
        sleep(1)
        
        
    if __name__ == '__main__':
        main()