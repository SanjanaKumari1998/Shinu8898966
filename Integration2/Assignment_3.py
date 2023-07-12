# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
#search_bar = driver.find_element("id","twotabsearchtextbox")
#search_bar.send_keys("laptop")

# Submitting the search query
#search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
#time.sleep(5)

# Verifying that the search results page has loaded
#assert "laptop" in driver.title

#click on the prime day deals
prime_day_deals_button = driver.find_element("id","prime-day-deals-button")
prime_day_deals_button.click()

# Select deals under $25
deals_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[12]/div/div/div/div[1]/div/div/div/div[2]/div/ol/li[4]/a/span[2]")




# Select a laptop from the search results
#laptop_link = #driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/#div/div/div/div[1]/span/a/div/img")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
#laptop_link.click()



# Waiting for the page to load
time.sleep(5)


#click on the image of skincare and laneige and innisfree
skincare_link = driver.find_element("xpath","//html/body/div[1]/div[2]/div[12]/div/div/div/div[2]/div[3]/div/div[1]/div/div/a/div/div/img")
# skincare_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
#skincare_link.click()


time.sleep(3)

# trying prime
try_prime_button = driver.find_element("id","try_prime")
try_prime_button.click()
















# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
