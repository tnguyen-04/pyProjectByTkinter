import tkinter as tk
from tkinter import ttk

# Hàm lấy danh sách tên đạo diễn (giả định)
def getDirectorName():
    return ["Director 1", "Director 2", "Director 3"]

# Tạo cửa sổ chính
window = tk.Tk()
window.title("ComboBox Example")

# Hàm callback khi chọn đạo diễn
def on_director_select(event):
    selected_director = cbb_directorName.get()
    print(f"Selected director: {selected_director}")

# Lấy danh sách tên đạo diễn
directorNameList = getDirectorName()

# Tạo style cho ComboBox
style = ttk.Style()
style.theme_use('clam')  # Chọn theme phù hợp, ví dụ 'clam'

# Thiết lập thuộc tính font cho ComboBox (nhỏ hơn và mờ đi)
style.configure('Small.TCombobox', font=('Arial', 10), foreground='gray')

# Tạo ComboBox
cbb_directorName = ttk.Combobox(window, values=directorNameList, width=15, style='Small.TCombobox')
cbb_directorName.grid(row=0, column=1, pady=(10, 0))
cbb_directorName.set("Select a director")  # Thiết lập giá trị mặc định

# Liên kết sự kiện chọn với hàm callback
cbb_directorName.bind("<<ComboboxSelected>>", on_director_select)

# Hiển thị cửa sổ
window.mainloop()
