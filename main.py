import sys #导入 sys 模块，用于处理程序的退出和命令行参数
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel#QApplication：用于创建应用程序。QMainWindow：主窗口类。QVBoxLayout：垂直布局管理器。QLabel：标签组件，用于显示页面内容。
from PyQt5.QtCore import Qt#处理鼠标事件


class MainWindow(QMainWindow):#定义一个继承自 QMainWindow 的主窗口类
    def __init__(self):#构造函数
        super().__init__()#调用父类的构造函数
        self.setGeometry(100, 100, 800, 600)#设置窗口
        self.setWindowTitle("My Window")#设置窗口标题

        # 创建一个中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)#设置中央部件main.py

        # 创建一个垂直布局
        layout = QVBoxLayout(central_widget)

        # 创建一个标签作为页面内容
        self.label = QLabel("This is the page content", self)#创建一个标签并添加到布局中
        layout.addWidget(self.label)

    def mousePressEvent(self, event):#重写鼠标点击事件处理方法
        if event.button() == Qt.LeftButton:#判断是否是左键点击
            title_bar_rect = self.rect().adjusted(0, 0, 0, -self.height() + self.menuBar().height() if self.menuBar() else 0)#计算标题栏的矩形区域，考虑是否有菜单栏
            if title_bar_rect.contains(event.pos()):#判断点击位置是否在标题栏区域
                self.update_page()#如果在标题栏点击，调用更新页面的方法

    def update_page(self):
        # 更新页面的逻辑，这里简单修改标签的文本
        self.label.setText("Page updated after clicking title bar")


def main():
    app = QApplication(sys.argv)#创建应用程序实例
    window = MainWindow()#创建主窗口实例
    window.show()#显示窗口
    sys.exit(app.exec_())#运行应用程序的主事件循环并处理退出


if __name__ == "__main__":
    main()