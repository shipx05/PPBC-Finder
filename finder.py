import tkinter as tk
import webbrowser
from PIL import Image , ImageTk

def open_url():
    code = entry.get()  # 获取输入框中的内容
    full_url = f"ppbc.iplant.cn/tu/{code}"
    webbrowser.open(full_url)  # 在浏览器中打开拼接后的网址


root = tk.Tk()
root.title("PPBC查询工具")
root.geometry("300x200+600+300")

#创建一个画布
canvas = tk.Canvas(root, width = 200, height = 100)
canvas.pack(fill = "both",expand = True)

#导入图片
image = Image.open("ppbcbiglogo_h.png")
new_image = image.resize((200, 100))
photo = ImageTk.PhotoImage(new_image)
canvas.create_image(50,0,image = photo,anchor = "nw")

# 文字提示
label = tk.Label(root,text=("输入图片编号"))
label.pack()

# 创建一个输入框
entry = tk.Entry(root)
entry.pack(pady=10)

# 创建一个确定按钮，点击按钮时调用open_url函数
button = tk.Button(root, text="确定", command=open_url)
button.pack(pady=5)

root.mainloop()