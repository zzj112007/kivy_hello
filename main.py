#python3.7  安装完kivy 运行报错:libjpg16-16.dll无法定位入口
#D:\Python37-32\share\sdl2\bin\libjpg16-16.dll
#D:\Python37-32\share\gstreamer\bin\libjpg16-16.dll
#发现用后边的版本替换前面的都可以
#缺省路径是找到前面的
#替换dll解决问题
#2019-02-16

from kivy.app import App
from kivy.uix.label import Label


class StandaloneApp(App):
    def build(self):
        return Label(text='Hello, Kivy')

if __name__ == '__main__':
    StandaloneApp().run()
