import pytest
from appium import webdriver

# from config import unsafe_config
# from pages.nav import NavPage

@pytest.fixture()
def driver():
    # yaml.load()
    caps = {
        "platformName": "Android",
        "deviceName": "QASEI8300000755",
        "appPackage": "com.nes.hometv",
        "appActivity": ".activity.SplashActivity",
        "automationName": "UiAutomator2",
    }

    # 初始化客户端
    # driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4723/wd/hub',
    #     desired_capabilities=caps,
    # )
    # driver.implicitly_wait(10)#设置隐形等待
    # yield driver#得到会话对象，这样不用每次用例都重启app
    # driver.quit()

##每次用例执行完之后，我们都需要做一个回到首页的操作
@pytest.fixture()
def back_to_home():
    """返回首页的动作,自己补充"""
    pass















## 设置了成 class
## 测试完。有没有额外的清理工作。



# @pytest.fixture()
# def login(driver):
#     """登录前置条件"""
#     NavPage(driver). \
#         click_my(). \
#         click_avatar(). \
#         login_success(unsafe_config.username, unsafe_config.pwd)
#     yield driver