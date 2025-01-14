import subprocess
import os

cur_path = os.path.dirname(os.path.realpath(__file__))

class keyevent():
    """"常见的keyevent事件"""
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
    A = 29
    B = 30
    C = 31
    D = 32
    E = 33
    F = 34
    G = 35
    H = 36
    I = 37
    J = 38
    K = 39
    L = 40
    M = 41
    N = 42
    O = 43
    P = 44
    Q = 45
    R = 46
    S = 47
    T = 48
    U = 49
    V = 50
    W = 51
    X = 52
    Y = 53
    Z = 54
    _0=7
    _1=8
    _2=9
    _3=10
    _4=11
    _5=12
    _6=13
    _7=14
    _8=15
    _9=16

class AdbHandler(object):


    def __int__(self, device_id, local_ptah=cur_path, device_path="sdcard", packname="", grammar="ls", times=1,
                video_name="demo",
                new_tcp=5000, old_tcp=8000, text="default" ,**kwargs,):
        """

        :param device_id: 设备ID
        :param local_ptah: 本地路径
        :param device_path: 设备路径
        :param packname: 包名
        :param grammar: 语法
        :param times: 时间
        :param video_name: 名字
        :param new_tcp: 新的ip
        :param old_tcp: 当前ip
        :param text: 文本
        :param keyevent: 设备按键
        :return:
        """
        self.devoce_id = device_id
        self.local_ptah = local_ptah
        self.device_path = device_path
        self.packname = packname
        self.grammar = grammar
        self.video_name = video_name
        self.times=times
        self.keyevent = keyevent



    @classmethod
    def get_device(cls):
        """
        查看连接设备
        :return:
        """
        devices = os.popen(r"adb devices")
        print(devices.read())
        return devices.read()

    def adb_install(self):
        """
        adb 安装apk
        :return:
        """
        install = os.popen(r"adb -s {} install  {}".format(self.devoce_id, self.packname))
        print(install.read())
        return install.read()

    def adb_uninstall(self):
        """
        adb 卸载apk
        :return:
        """
        uninstall = os.popen(r"adb -s {} uninstall  {}".format(self.devoce_id, self.packname))
        print(uninstall.read())
        return uninstall.read()


    def adb_shell(self):
        """
        out是执行成功返回0
        info是执行后控制面板输出
        :return:
        """
        out, info = subprocess.getstatusoutput("adb -s {} shell {}".format(self.devoce_id, self.grammar))
        print(out, info)
        return out, info


    def adb_video(self):
        """
        录制30秒视频
        :return:
        """
        video = subprocess.call("adb shell screenrecord --time-limit {}.mp4 ".format(self.times, self.device_path,
                                                                                     self.video_name),
                                shell=True)
        print(video)
        return video

    def adb_start_server(self):
        """
        ensure that there is a server running
        :return:
        """
        start_server = subprocess.call("adb start-server  ", shell=True)
        return start_server


    def adb_kill_server(self):
        """
        kill the server if it is running
        :return:
        """
        kill_server = subprocess.call("adb start-server  ", shell=True)
        return kill_server


    def adb_reboot(self):
        """
         reboots the device, optionally into the bootloader or recovery program
           :return:
           """
        reboot = subprocess.call("adb reboot ", shell=True)
        return reboot
    #
    # def adbKeyEvent(self):
    #     """执行adb keyevent事件  参数从keyevent类里面关联"""
    #     adb = "adb shell input keyevent {}".format(self.keyname)
    #     os.system(adb)

    # def adb_input_keyevent(self):
    #     """
    #     # adb input keyevent #
    #
    #     """
    #     input_keyevent = subprocess.call("adb shell input keyevent {}".format(self.keyevent), shell=True)
    #     # print(input_keyevent)
    #     return input_keyevent

    def LEFT_K(self):
        """向左按键"""
        left_keyevent=subprocess.call("adb shell input keyevent {}".format(keyevent.LEFT), shell=True)
        return left_keyevent

    def RIGHE_K(self):
        """向右按键"""
        right_keyevent=subprocess.call("adb shell input keyevent {}".format(keyevent.RIGHT), shell=True)
        return right_keyevent

    def UP_K(self):
        """向上按键"""
        up_keyevent=subprocess.call("adb shell input keyevent {}".format(keyevent.UP), shell=True)
        return up_keyevent

    def DOWN_K(self):
        """向下按键"""
        down_keyevent=subprocess.call("adb shell input keyevent {}".format(keyevent.DOWN), shell=True)
        return down_keyevent

    def OK_K(self):
        """ok按键"""
        ok_keyevent=subprocess.call("adb shell input keyevent {}".format(keyevent.OK), shell=True)
        return ok_keyevent

    def ENTER_K(self):
        """ENTER按键"""
        ENTER_keyevent=subprocess.call("adb shell input keyevent {}".format(keyevent.ENTER), shell=True)
        return ENTER_keyevent

    def BACK_K(self):
        """返回按键"""
        back_keyevent = subprocess.call("adb shell input keyevent {}".format(keyevent.BACK), shell=True)
        return back_keyevent

    def DEL_K(self):
        """删除按键"""
        del_keyevent = subprocess.call("adb shell input keyevent {}".format(keyevent.DEL), shell=True)
        return del_keyevent

    def N_K(self):
        """删除按键"""
        N_keyevent = subprocess.call("adb shell input keyevent {}".format(keyevent.N), shell=True)
        return N_keyevent

    def write_data(self,value=""):
        """输入文本"""
        vl=subprocess.call("adb shell input text {}".format(value), shell=True)
        return vl

if __name__=="__main__":
    adb=AdbHandler()
    adb.get_device()
    # i=1
    # while i<3:
    #     adb.RIGHE_K()
    #     i+=1
    # adb.BACK_K()
    # adb.OK_K()
    adb.write_data(value="nihao")















