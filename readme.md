# Tutorial
## Author: CLIN
## Date: 2024-05-08
## [Source](https://www.geeksforgeeks.org/selenium-python-introduction-and-installation/?ref=next_article)
### Installation
* Firefox driver
    * https://formulae.brew.sh/formula/geckodriver
* Chromium Driver
    * https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i4

### Components
* driver = webdriver.Firefox() -- webdriver object creation
* driver.get(url) -- get page
* Getting elements
    * element = driver.find_element(By.ID, "main")
    * driver.find_element(By.NAME, "passwr")
    * driver.find_element(By.XPATH, "")
* Interact with elements
    * element.send_keys("Arrays")
    * element.send_keys("some text")
    * element.send_keys(" and some", Keys.ARROW_DOWN)
    * element.clear()