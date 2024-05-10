# Tutorial
## Author: CLIN
## Date: 2024-05-08
## [Source](https://www.geeksforgeeks.org/selenium-python-introduction-and-installation/?ref=next_article)
## [selenium.dev](https://www.selenium.dev/)
### Installation
* Firefox driver
    * https://formulae.brew.sh/formula/geckodriver
* Chromium Driver
    * https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i4

### Components
* driver = webdriver.Firefox() -- webdriver object creation
* driver.get(url) -- get page
* Getting element - single
    * element = driver.find_element(By.ID, "main")
    * driver.find_element(By.NAME, "passwr")
    * driver.find_element(By.XPATH, "")
      * By.ID
      * By.PARTIAL_LINK_TEXT, By.XPATH, By.LINK_TEXT 
      * By.NAME, By.CLASS_NAME, By.TAG_NAME, By.CSS_SELECTOR
* Getting elements - multiple
    * element = driver.find_elements(By.ID, "main")
* Interact with elements
    * element.send_keys("Arrays")
    * element.send_keys("some text")
    * element.send_keys(" and some", Keys.ARROW_DOWN)
    * element.clear()