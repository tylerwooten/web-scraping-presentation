from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://www.weather.com"

driver = webdriver.Chrome( executable_path="dependencies/chromedriver" )
driver.get(url)
time.sleep(10)

search_box = driver.find_element_by_id("LocationSearch_input")
search_box.send_keys("Houston, TX")
search_box.send_keys(Keys.ENTER)
time.sleep(10)

more_button = driver.find_element_by_xpath( "//*[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff" \
                                            "-9a1a-d99a39f16abe']/nav/div/div[2]/button" )
more_button.send_keys(Keys.ENTER)
time.sleep(10)

allergy_button = driver.find_element_by_xpath( "//*[@id='WxuLocalsuiteNav-header-71dadf79-621d-43ff" \
                                                "-9a1a-d99a39f16abe']/nav/div/div[2]/nav/div/div/nav/div/a[2]" )
allergy_button.send_keys(Keys.ENTER)
time.sleep(10)

pollen_breakdown_table = driver.find_elements_by_xpath( "//section[@aria-label='Pollen Breakdown']" \
                                                        "//div//div[contains(@class,'breakdownContainer')]" )

time.sleep(10)
for pollen_info in pollen_breakdown_table:
    print( pollen_info.text, "\n" )

driver.quit()