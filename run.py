import sys
from PySide6.QtWidgets import QApplication
from login import LoginWindow
from main import mainWindow

def main():
    app = QApplication([])

    login = LoginWindow()
    main_refs = {}

    def open_main(account: str):
        win = mainWindow()
        win.show()
        # 保存引用
        main_refs['win'] = win
        login.close()

    # 成功登录后发射信号，打开主窗口
    login.login_success.connect(open_main)

    login.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
