from selenium import webdriver
from time import sleep

# page opening ( 10 )
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="chromedriver.exe")
driver5 = webdriver.Chrome(executable_path="chromedriver.exe")
driver6 = webdriver.Chrome(executable_path="chromedriver.exe")
driver7 = webdriver.Chrome(executable_path="chromedriver.exe")
driver8 = webdriver.Chrome(executable_path="chromedriver.exe")
driver9 = webdriver.Chrome(executable_path="chromedriver.exe")


# direction ( link )
driver.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver1.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver2.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver3.get("https://www.youtube.com/shorts/AxS43K7eL7o")
driver4.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver5.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver6.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver7.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver8.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")
driver9.get("https://www.youtube.com/watch?v=MWDyDQqC5G0")


# refresh loop
while True:
    #in second
    sleep(60)
    driver.refresh()
    driver4.refresh()
    driver3.refresh()
    driver2.refresh()
    driver1.refresh()
    driver5.refresh()
    driver6.refresh()
    driver7.refresh()
    driver8.refresh()
    driver9.refresh()