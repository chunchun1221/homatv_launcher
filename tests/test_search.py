import pytest
from appium import webdriver
from data.search_data import search_data
from pages import search
from pages.search import SearchPages
from pages.tab import TabPage


@pytest.mark.parametrize("search_info",search_data)
# def test_search(search_info,driver):
def test_search():
    search_info = [
        {"text": "  ", "expected": "Config is Empty"},]
    """
    测试步骤：
    0.在首页”home“，向左按键
    1.tab移动到“search”
    2、在输入框，ok按键，跳出虚拟键盘
    3、输入文本（text）【为空？数字？特殊字符？过长？】
    4、确认按键
    5、搜索结果（是否有三种类型的rail结果出来，并且显示结果是否正确，焦点选择的时候）
    6、点击搜索结果，看是否能成功跳转。
    7.断言


    1、手工执行流程，得到所以有的locator(这个测试步骤里面需要的元素，先把所有的lactor放在一个地方）
    2、封装页面行为，PO模式
    3、设置前置条件（conftest）

    :return:
    """

    caps = {
        "platformName": "Android",
        "deviceName": "QASEI8300000755",
        "appPackage": "com.nes.hometv",
        "appActivity": ".activity.SplashActivity",
        "automationName": "UiAutomator2",
    }
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=caps,
    )
    driver.implicitly_wait(10)  # 设置隐形等待


  # yield driver  # 得到会话对象，这样不用每次用例都重启app
    driver.quit()

    actual=SearchPages(driver).\
        search_keyboard().\
        search(search_info["text"]).\
        get_error_msg()
    assert actual != search_info["expected"]

    # S=SearchPages()
    # S.press_left()
    # S.press_ok()
    # actual=S.search(search_info['text']).get_error_msg()
    # assert actual != search_info["expected"]










