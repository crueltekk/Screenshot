from os import times
from PySimpleGUI.PySimpleGUI import P
from selenium import webdriver
from selenium.webdriver.chrome import options
from gui import dldriver
import time

def take_screenshot():
    links = ["https://google.de", "tdomeet.de"]
    
    WINDOW_SIZE = "1920, 1080"
    
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y-%H-%M-%S', t)
    
    if dldriver == 'firefox':
        options = webdriver.FirefoxOptions()
        #options.add_argument('--headless')
        options.add_argument('--window-size=%s' %WINDOW_SIZE)
        
        driver = webdriver.Firefox(executable_path=f'{dldriver}driver.exe', options=options)
        
        driver.get(links[0])
        
        time.sleep(5)
        
        driver.save_screenshot('screens/spawn/screenshot_spawn_area' + timestamp + '.png')
    
        print(f'Screenshot {links[0]} is taken')
        
        driver.close()
    elif dldriver == 'chrome':
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        options.add_argument("--window-size=%s" %WINDOW_SIZE)
        
        driver = webdriver.Chrome(executable_path=f"{dldriver}driver.exe", options=options)
        driver.get(links[0])
        
        time.sleep(5)
        
        driver.save_screenshot('screens/spawn/screenshot_spawn_area' + timestamp + '.png')
    
        print(f'Screenshot {links[0]} is taken')
        
        driver.close()
    elif dldriver == 'edge':
        options = webdriver.Edge()
        options.add_argument("--headless")
        options.add_argument("--window-size=%s" %WINDOW_SIZE)
        
        driver = webdriver.Edge(executable_path=f"{dldriver}driver.exe", options=options)
        driver.get(links[0])
        
        time.sleep(5)
        
        driver.save_screenshot('screens/spawn/screenshot_spawn_area' + timestamp + '.png')
    
        print(f'Screenshot {links[0]} is taken')
    elif dldriver == 'opera':
        options = webdriver.Opera()
        options.add_argument("--headless")
        options.add_argument("--window-size=%s" %WINDOW_SIZE)
        
        driver = webdriver.Opera(executable_path=f"{dldriver}driver.exe", options=options)
        driver.get(links[0])
        
        time.sleep(5)
        
        driver.save_screenshot('screens/spawn/screenshot_spawn_area' + timestamp + '.png')
    
        print(f'Screenshot {links[0]} is taken')
    else:
        print('Maybe wrong driver selected')
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=%s" %WINDOW_SIZE)
    
    # driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    
    # driver.get(links[0])
    
    # time.sleep(5)
    
    # t = time.localtime()
    # timestamp = time.strftime('%b-%d-%Y-%H-%M-%S', t)
    # driver.save_screenshot('screens/spawn/screenshot_spawn_area_' + timestamp + '.png')
    
    # print(f'Screenshot {links[0]} is taken')
    
    # time.sleep(5)
    
    # driver.get(links[1])
    
    # time.sleep(5)
    
    # driver.save_screenshot('screens/stigga/screenshot_stigga_area_' + timestamp + '.png')
    
    # print(f'Screenshot {links[1]} is taken')
    
    # driver.quit()