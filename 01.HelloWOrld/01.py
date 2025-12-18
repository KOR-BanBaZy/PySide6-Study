import sys
# 파이썬 표준 라이브러리
# 프로그램 실행 인자, 종료 코드 처리 등에 사용됨


from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
# PySide6에서 GUI 사용을 위한 위젯 클래스들을 가져옴
# QApplication      : 앱 전체 관리자 (유니티의 Application 개념)
# QWidget           : 가장 기본적인 창/컨테이너
# QVBoxLayout       : 세로 레이아웃
# QLineEdit         : 한 줄 입력창
# QPushButton       : 버튼
# QLabel            : 텍스트 표시용 라벨


app = QApplication(sys.argv)
# Qt 애플리케이션 객체 생성

w = QWidget()
layout = QVBoxLayout(w)

edit = QLineEdit()
edit.setPlaceholderText("여기에 입력")
label = QLabel("")

btn = QPushButton("적용")

def apply():
    label.setText(f"입력값: {edit.text()}")

btn.clicked.connect(apply)

layout.addWidget(edit)
layout.addWidget(btn)
layout.addWidget(label)

w.show()
sys.exit(app.exec())