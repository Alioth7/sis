import sys

import pandas as pd

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox
from loginUi import Ui_Form

import os
userFile = os.path.join(os.path.dirname(__file__), 'data', 'students.csv')

class LoginWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.registerButton.clicked.connect(self.registerFn)
        self.loginButton.clicked.connect(self.loginFn)

    def registerFn(self):
        # 拿到账号和密码
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # 处理输入为非法的情况
        isValid, reason = self.validate_input(account, password)
        if not isValid:
            QMessageBox.warning(self, "警告", reason)
            return

        # 读取csv文件
        # 查看是否已被注册
        try:
            df = pd.read_csv(userFile)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=['account', 'password'])

        if account in df['account'].values:
            QMessageBox.warning(self, "警告", "账号已被注册")
            return

        # 将账号密码写入csv文件
        new_user = pd.DataFrame({'account': [account], 'password': [password]})
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(userFile, index=False)

        QMessageBox.information(self, "信息", "注册成功")

    def loginFn(self):
        # 拿到账号和密码
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        isValid, reason = self.validate_input(account, password)
        if not isValid:
            QMessageBox.warning(self, "警告", reason)
            return

        if not self.validate(account, password):
            QMessageBox.warning(self, "警告", "账号或密码错误")
            return

        # 登录成功
        QMessageBox.information(self, "信息", "登录成功")
        # TODO: 打开主窗口


    def validate(self, account, password):
        # 读取csv文件
        try:
            df = pd.read_csv(userFile)
        except pd.errors.EmptyDataError:
            return False

        # 检查账号和密码是否匹配
        user = df[(df['account'] == account) & (df['password'] == password)]

        if not user.empty:
            return True
        else:
            return False

    def validate_input(self, account: str, password: str):
        """
        Return (True, "") if valid else (False, reason).
        Rules:
          - 不为空
          - 没有非法字符(仅允许字母、数字、下划线)
          - 长度大于6(密码)
        """
        if not account or not password:
            return False, "账号或密码不能为空"
        import re
        pattern = re.compile(r'^[A-Za-z0-9_]+$')
        if not pattern.fullmatch(account):
            return False, "账号包含非法字符(仅允许字母、数字、下划线)"
        if not pattern.fullmatch(password):
            return False, "密码包含非法字符(仅允许字母、数字、下划线)"
        if len(password) <= 6:
            return False, "密码长度必须大于6"
        return True, ""

if __name__ == "__main__":
    app = QApplication([])
    windows = LoginWindow()
    windows.show()
    app.exec()