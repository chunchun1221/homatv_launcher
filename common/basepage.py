import os
from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import config
from middleware.handler import Handler
import airtest

class keycode():
    """"常见的keycode事件"""
    BACK= 4#后退
    HOME= 3#(HOME)
    UP=19 #（向上按键）
    DOWN=20#（向下按键）
    LEFT=21#（向左按键）
    RIGHT=22#（向右按键）
    OK=23#（ok按键）
    VOLUP=24#（声音放大）
    VOLDOWN=25#（声音放小）
    POWER=26#电源
    ENTER=66#输入确认
    DEL=67#输入删除

class BasePage:
    title = None

    def __init__(self, driver):
        self.driver = driver




    def find_element(self, locator):
        """查找元素"""
        try:
            el = self.driver.find_element(*locator)
            return el
        except:
            # 如果找不到元素，截图
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))
            raise TimeoutError("没有找到元素")

    def screen_shot(self):
        """截图"""

        path = config.IMG_PATH
        ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = os.path.join(path, ts + ".png")
        self.driver.save_screenshot(filename)

    def wait_element_visible(self, locator, timeout=20, poll=0.5):
        """等待某个元素可见"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))


    def wait_element_clickable(self, locator, timeout=20, poll=0.5):
        """等待某个元素可以被点击"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))


    def wait_element_presence(self, locator, timeout=20, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))


    def click(self, locator):
        """点击某个元素"""
        self.wait_element_clickable(locator).click()
        return self

    def write(self, locator, value=''):
        """输入信息"""
        self.wait_element_presence(locator).send_keys(value)
        return self

    def get_toast(self):
        """获取toast弹窗
        """
        el = self.wait_element_presence(("xpath", "//android.widget.Toast"))
        return el

    def press_enter(self):
        """点击回车或者确认按钮.
        特别常用的键盘操作
        """
        self.driver.press_keycode(keycode.ENTER)

    def press_ok(self):
        """ok按键"""
        self.driver.press_keycode(keycode.OK)

    def long_press_ok(self):
        """长按ok按键"""
        self.driver.long_press_keycode(keycode.OK)

    def press_up(self):
        """up按键"""
        self.driver.press_keycode(keycode.UP)

    def press_down(self):
        """down按键"""
        self.driver.press_keycode(keycode.DOWN)

    def press_left(self):
        """左按键"""
        self.driver.press_keycode(keycode.LEFT)

    def press_right(self):
        """右按键"""
        self.driver.press_keycode(keycode.RIGHT)

    def press_back(self):
        """返回按键"""
        self.driver.press_keycode(keycode.BACK)


