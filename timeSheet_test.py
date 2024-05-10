# PROJECT TO CREATE SELENIUM
# %%import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

l_url = 'https://citycollegesf.na1.echosign.com/'
supervisorEmail = "clin@ccsf.edu"

# %%
driver = webdriver.Firefox()
driver.get(l_url)

## Await login

# %% EXECUTE WORKFLOW BUTTON
l_class = "spectrum-Button--secondary"
btnLibraryStart = driver.find_element(By.CLASS_NAME, l_class)
ActionChains(driver).double_click(btnLibraryStart).perform()

# %% initialize time sheet workflow
l_id = "selectFiles-view29-tab-2"
workFlowLink = driver.find_element(By.ID, l_id)
ActionChains(driver).click(workFlowLink).perform()

l_id = "cell-title-c370"
timeSheetLink = driver.find_element(By.ID, l_id)
ActionChains(driver).double_click(timeSheetLink).perform()

# %% Submit supervisor email
l_class = "recipient-email-input"
tbRecpEmail = driver.find_elements(By.CLASS_NAME, l_class)
tbRecpEmail[1].send_keys(supervisorEmail)
# %%
l_class = "send-btn"
btnSubmit = driver.find_element(By.CLASS_NAME, l_class)
ActionChains(driver).double_click(btnSubmit).perform()

# %%
l_class = "text_field_input"
tbInputs = driver.find_elements(By.CLASS_NAME, l_class)

# TOP INPUT
tbLname = tbInputs[0] ##last name
tbLname.clear()
tbLname.send_keys('Lin')

tbFname = tbInputs[1] ##first name
tbFname.clear()
tbFname.send_keys('Chien')

tbClass = tbInputs[2] ##class number
tbClass.clear()
tbClass.send_keys('1064')

## Each row is 8
# %%INITIAL DATE
tbClass = tbInputs[3] #initial date
tbClass.clear()
tbClass.send_keys('03/02/2024')

# %% populate box
l_entryPoints = list(range(20, 53, 8)) + list(range(76, 109, 8))
for i in l_entryPoints:
    print(i)
    tbArrive    = tbInputs[i]
    tbLunchOut  = tbInputs[i + 1]
    tbLunchIn   = tbInputs[i + 2]
    tbDepart    = tbInputs[i + 3]
    tbTotalHr   = tbInputs[i + 4]
    tbRWW       = tbInputs[i + 5]

    tbArrive.clear()
    tbLunchOut.clear()
    tbLunchIn.clear()
    tbDepart.clear()
    tbTotalHr.clear()
    tbRWW.clear()

    tbArrive.send_keys('8:00')
    tbLunchOut.send_keys('12:00')
    tbLunchIn.send_keys('12:30')
    tbDepart.send_keys('16:00')
    tbTotalHr.send_keys('7.5')
    tbRWW.send_keys('0.5')

# %%
l_class='faux_field'
signField = driver.find_element(By.CLASS_NAME, l_class)
ActionChains(driver).click(signField).perform()

l_class='apply'
btnApply = driver.find_element(By.CLASS_NAME, l_class)
ActionChains(driver).click(btnApply).perform()

# %%
l_class='click-to-esign'
btnEsign = driver.find_element(By.CLASS_NAME, l_class)
ActionChains(driver).click(btnEsign).perform()


# %%
t2 = tbInputs[76]
print(t2.get_property('name'))
# %%