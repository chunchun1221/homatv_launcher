from appium import webdriver



caps = {
        "platformName": "Android",
        "deviceName": "QASEI8300000755",
        "appPackage": "com.nes.hometv",
        "appActivity": ".activity.SplashActivity",
        "automationName": "UiAutomator2",
    }
driver = webdriver.Remote(

     command_executor='http:/127.0.0.1:4723/wd/hub',
     desired_capabilities=caps,
    )
driver.implicitly_wait(10)  # 设置隐形等待







