import sys  # 导入 sys 模块，用于处理程序的退出和命令行参数
# QApplication：用于创建应用程序。QMainWindow：主窗口类。QVBoxLayout：垂直布局管理器。QLabel：标签组件，用于显示页面内容。QHBoxLayout,水平布局管理。QMenuBar，创建菜单栏。
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout, QMenuBar
from PyQt5.QtCore import Qt # 包含了 PyQt5 的核心功能，如窗口标志、对齐方式
from PyQt5.QtGui import QIcon, QPixmap  # QIcon，管理图标。QPixmap，加载和操作图像。


class CustomTitleBar(QWidget):  # 自定义的标题栏类
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)  # 标题栏的高度固定
        self.layout = QHBoxLayout(self)  # 创建一个水平布局，并将其设置为标题栏的布局管理器
        # 设置布局的边距和部件间的间距为 0，以确保紧凑排列
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 创建一个水平布局用于放置图标和标题
        title_layout = QHBoxLayout()  # 创建一个内部的水平布局用于放置图标和标题文本
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.setSpacing(1)

        # 创建并添加图标
        icon_label = QLabel(self)  # 创建一个 QLabel 部件，用于显示图标
        icon = QPixmap("icons/bnb_crypto_icon_264371.ico")  # 使用 QPixmap 从文件加载图标，需要将路径替换为实际图标文件的路径
        icon = icon.scaled(24, 24, Qt.KeepAspectRatio)  # 图标缩放到 24x24 像素，同时保持其原始宽高比
        icon_label.setPixmap(icon)  # 将缩放后的图标设置到 icon_label 中
        icon_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 左对齐且垂直居中
        title_layout.addWidget(icon_label)  # 将图标标签添加到内部的水平布局中

        self.title_label = QLabel("Custom Title Bar", self)  # 创建一个显示标题的 QLabel 部件
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 左对齐且垂直居中
        title_layout.addWidget(self.title_label)  # 将标题标签添加到内部水平布局中

        self.layout.addLayout(title_layout)  # 将内部的水平布局添加到主标题栏的水平布局中

        self.minimize_button = QPushButton(self)  # 创建一个最小化按钮
        minimize_icon = QIcon("icons/ethereum_crypto_icon_264380.ico")  # 使用 QIcon 从文件加载最小化按钮的图标，需替换为实际路径
        # 获取最小化图标的 QPixmap 并缩放
        minimize_pixmap = minimize_icon.pixmap(24, 24)
        self.minimize_button.setIcon(QIcon(minimize_pixmap))  # 将缩放后的 QPixmap 转换为 QIcon 并设置为最小化按钮的图标。
        self.minimize_button.clicked.connect(self.minimize_parent)  # 将最小化按钮的点击事件连接到 minimize_parent 方法。
        self.layout.addWidget(self.minimize_button)  # 将最小化按钮添加到主标题栏的水平布局中

        self.maximize_button = QPushButton(self)
        maximize_icon = QIcon("icons/polkadot_dot_crypto_icon_264383.ico")  # 替换为你的图标文件路径
        # 获取最大化图标的 QPixmap 并缩放
        maximize_pixmap = maximize_icon.pixmap(24, 24)
        self.maximize_button.setIcon(QIcon(maximize_pixmap))
        self.maximize_button.clicked.connect(self.maximize_parent)
        self.layout.addWidget(self.maximize_button)
        # 创建关闭按钮并设置图标
        self.close_button = QPushButton(self)
        close_icon = QIcon("icons/xrp_crypto_icon_264372.ico")  # 替换为你的图标文件路径
        # 获取关闭图标的 QPixmap 并缩放
        close_pixmap = close_icon.pixmap(24, 24)
        self.close_button.setIcon(QIcon(close_pixmap))
        self.close_button.clicked.connect(self.close_parent)
        self.layout.addWidget(self.close_button)

    def close_parent(self):  # close_parent 方法：调用父部件的 close 方法，关闭窗口
        self.parent().close()

    def minimize_parent(self):  # minimize_parent 方法：调用父部件的 showMinimized 方法，将窗口最小化
        self.parent().showMinimized()

    def maximize_parent(self):  # maximize_parent 方法：根据父部件是否最大化，切换窗口的显示状态。如果已经最大化，调用 showNormal 恢复正常大小；否则调用 showMaximized 进行最大化。
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()


class MainWindow(QMainWindow):  # 主窗口类，继承自 QMainWindow
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)  # 设置主窗口的初始位置和大小
        self.setWindowTitle("Custom Title Bar Window")  # 设置主窗口的标题

        # 设置窗口标志，隐藏默认标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 创建自定义标题栏实例并将其作为主窗口的一部分
        self.title_bar = CustomTitleBar(self)

        # 创建一个中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)  # 将中央部件设置为主窗口的中央部件

        # 为中央部件创建一个垂直布局
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.title_bar)  # 直接将自定义标题栏添加到布局中
        layout.addWidget(QLabel("This is the page content", self))


def main():  # 程序入口函数
    app = QApplication(sys.argv)  # 创建 QApplication 实例，初始化 PyQt5 应用程序
    window = MainWindow()  # 创建主窗口实例
    window.show()  # 显示主窗口
    sys.exit(app.exec_())  # 进入应用程序的事件循环，直到程序退出


if __name__ == "__main__":
    main()
