

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from middleware.handler import Handler


class SearchPages(BasePage):


    #输入框
    edit_locator = (MobileBy.XPATH,
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")





    def search_keyboard(self):
        self.press_left()
        self.press_ok()





    def search(self,text):
        self.write(self.edit_locator,text)
        self.press_enter()
        return self
        


    def get_error_msg(self):
        """toast
        找到我们的错误信息"""
        el=self.get_toast()
        return el.text



if __name__=="__main__":
    pass























