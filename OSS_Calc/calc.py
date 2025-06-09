import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")
        self.expression = ""

        # 입력창
        self.entry = tk.Entry(self.root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열 정의
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # 버튼 프레임과 버튼 생성
        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 20),
                    command=lambda c=char: self.on_click(c)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == "=":
            try:
                # 계산 결과
                result = str(eval(self.expression))
                self.expression = result
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception:
                # 오류 처리
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            # 숫자/연산자를 누를 때마다 expression에 추가
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
