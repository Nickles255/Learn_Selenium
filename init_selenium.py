# Python program to demonstrate
# selenium

# %%import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# %%
l_head = "http://www.google.com/"
l_search = "search?q=geeksforgeeks"
# %%create firefox webdriver object
driver = webdriver.Firefox()

# %% create chrome webdirver
driver = webdriver.Chrome()
# %%
# l_url = l_head + l_search
l_url = "https://www.geeksforgeeks.org/"
driver.get(l_url)

# %% find ID of search box
my_id = "gcse-search-input"
element = driver.find_element(By.ID, my_id)

# %%send keys
element.send_keys("Arrays")
