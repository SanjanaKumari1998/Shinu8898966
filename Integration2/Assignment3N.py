# Importing required libraries

# pip install selenium


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Shine page
driver.get("https://ca.shein.com")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("Dress")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Dress" in driver.title

# Selecting a Dress from the search results
Dress_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[2]/section/div[1]/section[1]/div[1]/a/img[2])
# Dress_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
Dress_link.click();



# Waiting for the laptop details page to load
time.sleep(5);

# Adding the laptop to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button");
add_to_cart_button.click();

# Waiting for the cart to update
time.sleep(5);

#click on add to cart button that is on image
#Clicking on add to cart button
add_to_cart_button= driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[2]/section/div[1]/section[1]/div[1]/section[1]/div[1]/div/div/button)
add_to_cart_button.click();
time.sleep(2);

#Click on size (s)button
size_s_button= driver.find_element("xpath","/html/body/div[15]/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/span[2]/div[1]/div)
size_s_button.click();
time.sleep(2);

#click on add to cart button

add_to_cart_button= driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/div/button[2]/div
add_to_cart_button.click();
time.sleep(2);

# view cart

view_cart_button= driver.find_element("xpath","/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/div/div[1]/div/div/div[3]/div[3]/button)
view_cart_button.click();
time.sleep(2);


#for checkout
checkout_now= driver.find_element("xpath","/html/body/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/button)
checkout_now.click();
time.sleep(2);


# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
