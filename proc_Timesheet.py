import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

from hrs_calc import calc_wrkHrs


def proc_Timesheet(in_lastName, in_FirstName, in_posnClass, in_supervisorEmail,
                   in_submit='N',
                   in_arrive='8:00', in_outLunch='12:00', in_inLunch='12:30',
                   in_leave='16:00'):
    """submit adobe time sheet for CCSF user
    goto adobe esign URL allowing login, selects workflow for ITS-timesheet,
    enters supervisor email into workflow form, calculate date and hrs based on entry,
    fills in sheet with data points, if in_submit = 'Y' will autosubmit form
    :param in_lastName: last name on time sheet
    :param in_firstName: first name on time sheet
    :param in_posnClass: position (i.e. 1063, 1544)
    :param in_supervisorEmail: email of supervisor
    :param in_submit: defaults to 'N' but flip to 'Y' to auto submit
    :param in_arrive: time arrived at work
    :param in_outLunch: time out for lunch
    :param in_inLunch: time in from lunch
    :param in_leave: time leave from work
    """
    l_url = 'https://citycollegesf.na1.echosign.com/'

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(l_url)

    # EXECUTE WORKFLOW BUTTON
    l_pause = True
    while l_pause == True:
        try:
            l_class = "spectrum-Button--secondary"
            btnLibraryStart = driver.find_element(By.CLASS_NAME, l_class)
            ActionChains(driver).double_click(btnLibraryStart).perform()
            l_pause = False
        except:
            l_pause = True
            time.sleep(2)  ##in seconds

    # initialize time sheet workflow
    l_pause = True
    while l_pause == True:
        try:
            l_class = "libraryWorkflows"
            workFlowLink = driver.find_element(By.CLASS_NAME, l_class)
            ActionChains(driver).click(workFlowLink).perform()

            l_class = 'single-select-row'
            workFlowMenu = driver.find_elements(By.CLASS_NAME, l_class)
            timeSheetLink = workFlowMenu[5]
            ActionChains(driver).double_click(timeSheetLink).perform()
            l_pause = False
        except:
            l_pause = True
            time.sleep(1)  ##in seconds

    time.sleep(2)
    l_class = "recipient-email-input"
    tbRecpEmail = driver.find_elements(By.CLASS_NAME, l_class)
    tbRecpEmail[1].send_keys(in_supervisorEmail)

    l_class = "send-btn"
    btnSubmit = driver.find_element(By.CLASS_NAME, l_class)
    ActionChains(driver).double_click(btnSubmit).perform()

    l_workHrs, l_rwwHrs = calc_wrkHrs(in_arrive, in_outLunch,
                                      in_inLunch, in_leave)

    # adjust to beginning saturday of 2 weeks
    # day of week is 0-monday to 6-sunday
    l_day = dt.date.today()
    l_diff = 4 - l_day.weekday()  # 4 is friday
    l_startDate = l_day + dt.timedelta(days=(l_diff - 13))
    l_startDate = l_startDate.strftime("%m/%d/%Y")

    # %% Data entry into form
    # wait for form to appear
    l_pause = True
    while l_pause == True:
        try:
            l_class = "text_field_input"
            tbInputs = driver.find_elements(By.CLASS_NAME, l_class)

            tbLname = tbInputs[0]  ##last name
            tbLname.send_keys(in_lastName)

            l_pause = False
        except:
            l_pause = True
            time.sleep(1)  ##in seconds

    # fill in top line of form

    tbFname = tbInputs[1]  ##first name
    tbFname.send_keys(in_FirstName)

    tbClass = tbInputs[2]  ##class number
    tbClass.send_keys(in_posnClass)

    # %% populate form times
    tbClass = tbInputs[3]  # initial date
    keys = tbClass.send_keys(l_startDate)

    # Each row is 8
    l_entryPoints = list(range(20, 53, 8)) + list(range(76, 109, 8))
    for i in l_entryPoints:
        tbArrive = tbInputs[i]
        tbLunchOut = tbInputs[i + 1]
        tbLunchIn = tbInputs[i + 2]
        tbDepart = tbInputs[i + 3]
        tbTotalHr = tbInputs[i + 4]
        tbRWW = tbInputs[i + 5]

        tbArrive.send_keys(in_arrive)
        tbLunchOut.send_keys(in_outLunch)
        tbLunchIn.send_keys(in_inLunch)
        tbDepart.send_keys(in_leave)
        tbTotalHr.send_keys(l_workHrs)
        tbRWW.send_keys(l_rwwHrs)

    l_class = 'faux_field'
    signField = driver.find_element(By.CLASS_NAME, l_class)
    ActionChains(driver).click(signField).perform()
    # wait for form to appear
    l_pause = True
    while l_pause == True:
        try:
            l_class = 'apply'
            btnApply = driver.find_element(By.CLASS_NAME, l_class)
            ActionChains(driver).click(btnApply).perform()

            l_class = 'click-to-esign'
            btnEsign = driver.find_element(By.CLASS_NAME, l_class)
            l_pause = False
        except:
            l_pause = True
            time.sleep(1)  ##in seconds

    if in_submit == 'Y':
        ActionChains(driver).double_click(btnEsign).perform()
    else:
        ActionChains(driver).click(btnEsign).perform()
