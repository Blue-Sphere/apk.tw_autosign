try:
    import time
    from selenium import webdriver

    browser = webdriver.Chrome()
    browser.get('https://apk.tw')
    browser.maximize_window()

    time.sleep(3)

    browser.find_element_by_xpath(
        "//*[@id='toptb']/div/div[3]/ul/li[1]/div/a").click()
    browser.find_element_by_xpath(
        "/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[1]/div/input").send_keys("輸入你的帳號")
    browser.find_element_by_xpath(
        "/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/div[2]/div/input").send_keys("輸入你的密碼")
    time.sleep(1)
    browser.find_element_by_xpath(
        "/html/body/div[3]/div/div[3]/ul/li[1]/div/div/form/div/div/button").click()

    time.sleep(20)
    browser.find_element_by_xpath(
        "//*[@id='my_amupper']").click()
    time.sleep(10)
    browser.quit()

    print("已完成APK.TW的每日簽到")

except:
    print("APK.TW的每日簽到執行失敗")