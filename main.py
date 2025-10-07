from mainUi import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
import pandas as pd
import os

gradesFile = os.path.join(os.path.dirname(__file__), 'data', 'grades.csv')

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.record_grade)
        self.query_button.clicked.connect(self.query_single_subject)
        self.average_score_query_button.clicked.connect(self.query_class_subject_average)
        self.total_score_query_button.clicked.connect(self.query_total_score)
        self.rank_query_button.clicked.connect(self.query_class_rank)

    def record_grade(self):
        name = self.name.text().strip()
        student_id = self.student_id.text().strip()
        class_name = self.className.currentText().strip()
        subject = self.input_choice.currentText().strip()
        score_text = self.score.text().strip()

        if not (name and student_id and class_name and subject and score_text):
            QMessageBox.warning(self, "警告", "姓名、学号、班级、科目和成绩不能为空")
            return

        try:
            score = float(score_text)
        except ValueError:
            QMessageBox.warning(self, "警告", "成绩必须是数字")
            return

        if not (0 <= score <= 100):
            QMessageBox.warning(self, "警告", "成绩需在0-100之间")
            return

        # 确保数据目录存在，若不存在，则创建
        os.makedirs(os.path.dirname(gradesFile), exist_ok=True)

        # 加入数据
        if not os.path.exists(gradesFile) or os.path.getsize(gradesFile) == 0:
            df = pd.DataFrame(columns=["student_id", "name", "class", "subject", "score"])
        else:
            try:
                df = pd.read_csv(gradesFile)
            except pd.errors.EmptyDataError:
                df = pd.DataFrame(columns=["student_id", "name", "class", "subject", "score"])

        new_row = {
            "student_id": student_id,
            "name": name,
            "class": class_name,
            "subject": subject,
            "score": score
        }
        df.loc[len(df)] = new_row
        df.to_csv(gradesFile, index=False)

        QMessageBox.information(self, "信息", "成绩录入成功")
        self.score.clear()

    def query_single_subject(self):
        name = self.name.text().strip()
        student_id = self.student_id.text().strip()
        subject = self.query_choice.currentText().strip()

        if not (name or student_id):
            QMessageBox.warning(self, "警告", "必须提供姓名或学号至少一个")
            return

        if (not os.path.exists(gradesFile)) or os.path.getsize(gradesFile) == 0:
            QMessageBox.information(self, "信息", "暂无成绩数据")
            return

        try:
            df = pd.read_csv(gradesFile)
        except pd.errors.EmptyDataError:
            QMessageBox.information(self, "信息", "暂无成绩数据")
            return

        query_df = df[df['subject'] == subject]
        # 如果同时提供了学号和名字，按照学号查询
        if student_id and name:
            QMessageBox.information(self, "信息", "同时提供了姓名和学号\n按照学号查询")
        if student_id:
            query_df = query_df[query_df['student_id'] == student_id]
        if name:
            query_df = query_df[query_df['name'] == name]

        if query_df.empty:
            QMessageBox.information(self, "信息", "未找到该科目成绩")
            return

        # 如果有多条记录，显示最新的一条记录
        latest_row = query_df.iloc[-1]
        QMessageBox.information(
            self,
            "信息",
            f"姓名: {latest_row['name']}\n学号: {latest_row['student_id']}\n班级: {latest_row['class']}\n科目: {latest_row['subject']}\n成绩: {latest_row['score']}"
        )

    def query_class_subject_average(self):
        class_name = self.className.currentText().strip()
        subject = self.query_choice.currentText().strip()

        if (not os.path.exists(gradesFile)) or os.path.getsize(gradesFile) == 0:
            QMessageBox.information(self, "信息", "暂无成绩数据")
            return

        try:
            df = pd.read_csv(gradesFile)
        except pd.errors.EmptyDataError:
            QMessageBox.information(self, "信息", "暂无成绩数据")
            return

        subset = df[(df['class'] == int(class_name)) & (df['subject'] == subject)] # 注意 class_name 转为 int
        if subset.empty:
            QMessageBox.information(self, "信息", "未找到该班级该科目成绩")
            return

        avg_score = subset['score'].mean()
        QMessageBox.information(
            self,
            "信息",
            f"{class_name}班级的{subject}科目平均成绩为: {avg_score:.2f}"
        )

    def _load_grades(self) -> pd.DataFrame:
        if (not os.path.exists(gradesFile)) or os.path.getsize(gradesFile) == 0:
            return pd.DataFrame(columns=["student_id", "name", "class", "subject", "score"])

        try:
            return pd.read_csv(
                gradesFile,
                dtype={"student_id": str, "name": str, "class": str, "subject": str, "score": float}
            )
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=["student_id", "name", "class", "subject", "score"])

    def query_total_score(self):
        name = self.name.text().strip()
        student_id = self.student_id.text().strip()
        if not (name or student_id):
            QMessageBox.warning(self, "警告", "必须提供姓名或学号至少一个")
            return
        df = self._load_grades()
        if df.empty:
            QMessageBox.information(self, "信息", "暂无成绩数据")
            return

        # 选出选中的那一行
        # 如果同时提供了学号和名字，按照学号查询
        if student_id and name:
            QMessageBox.information(self, "信息", "同时提供了姓名和学号\n按照学号查询")
        if student_id:
            df = df[df['student_id'] == student_id]
        if name:
            df = df[df['name'] == name]
        if df.empty:
            QMessageBox.information(self, "信息", "未找到该学生成绩")
            return
        # 保留每个科目最新成绩
        latest_per_subject = df.groupby('subject', as_index=False).last()
        total = latest_per_subject['score'].sum()
        lines = "\n".join(f"{row.subject}: {row.score}" for row in latest_per_subject.itertuples())
        QMessageBox.information(
            self,
            "信息",
            f"姓名: {latest_per_subject.iloc[-1]['name']}\n学号: {latest_per_subject.iloc[-1]['student_id']}\n总分: {total:.2f}\n\n科目明细:\n{lines}"
        )

    def query_class_rank(self):  # NEW
        class_name = self.className.currentText().strip()
        df = self._load_grades()
        if df.empty:
            QMessageBox.information(self, "信息", "暂无成绩数据")
            return
        df_class = df[df['class'] == class_name]
        if df_class.empty:
            QMessageBox.information(self, "信息", "该班级暂无成绩")
            return
        # 保留每个学生每门课最新成绩
        latest = (df_class
                  .sort_index() # 保证选择最后一个
                  .groupby(['student_id', 'subject'], as_index=False) # 分组
                  .last())
        # 汇总总分
        totals = (latest
                  .groupby('student_id', as_index=False)
                  .agg(total_score=('score', 'sum'),
                       name=('name', 'last')))
        totals = totals.sort_values('total_score', ascending=False, kind='stable')
        totals['rank'] = range(1, len(totals) + 1)
        lines = "\n".join(f"{row.rank}. {row.name}({row.student_id}) 总分: {row.total_score:.2f}" for row in totals.itertuples())
        QMessageBox.information(
            self,
            "信息",
            f"{class_name} 班级排名(按总分):\n\n{lines}"
        )


if __name__ == "__main__":
    app = QApplication([])
    win = mainWindow()
    win.show()
    app.exec()
