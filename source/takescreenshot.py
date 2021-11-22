from os import times
from selenium import webdriver
import time

def take_screenshot():
    links = ["https://google.de", "tdomeet.de"]
    
    WINDOW_SIZE = "1920, 1080"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=%s" %WINDOW_SIZE)
    
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    
    driver.get(links[0])
    
    time.sleep(5)
    
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y-%H-%M-%S', t)
    driver.save_screenshot('screens/spawn/screenshot_spawn_area_' + timestamp + '.png')
    
    print(f'Screenshot {links[0]} is taken')
    
    time.sleep(5)
    
    driver.get(links[1])
    
    time.sleep(5)
    
    driver.save_screenshot('screens/stigga/screenshot_stigga_area_' + timestamp + '.png')
    
    print(f'Screenshot {links[1]} is taken')
    
    driver.quit()