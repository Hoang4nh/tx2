#Đoạn code sau để tạo và thực hiện các phép toán trên hai ma trận a và b
import numpy as np
a=np.array([[1, 2],
            [3, 4]])
b=np.array([[4, 3],
            [2, 1]])

print("Array sum:\n",a+b)
print("Array multiplication:\n",a*b)
print("Matrix multiplication:\n",a.dot(b))

#Đoạn code sau khi đã cải thiện
#ý tưởng tạo giao diện nhập 2 ma trận chỉnh được số hàng và cột theo ý muốn và tính các phép tính ma trận
#thêm button xóa dữ liệu và thoát chương trình

import numpy as np
import tkinter as tk

def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def create_matrix(entry_matrix, rows, cols, frame):
    # Kiểm tra xem ma trận cũ có giá trị hay không
    if entry_matrix:
        # Lấy giá trị từ ô nhập liệu cũ và lưu vào ma trận mới
        for i, row in enumerate(entry_matrix):
            for j, entry in enumerate(row):
                value = entry.get()
                entry.destroy()
                entry = tk.Entry(frame)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.insert(0, value)
                entry_matrix[i][j] = entry
    else:
        # Tạo ô nhập liệu cho ma trận mới
        for i in range(rows):
            entry_row = []
            for j in range(cols):
                entry = tk.Entry(frame)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry_row.append(entry)
            entry_matrix.append(entry_row)

def clear_data():
    entry_rows_a.delete(0, tk.END)
    entry_cols_a.delete(0, tk.END)
    entry_rows_b.delete(0, tk.END)
    entry_cols_b.delete(0, tk.END)

    for entry_row in entry_a:
        for entry in entry_row:
            entry.delete(0, tk.END)

    for entry_row in entry_b:
        for entry in entry_row:
            entry.delete(0, tk.END)

    result_text.set("")

def perform_operation(operation):
    try:
        rows_a = int(entry_rows_a.get())
        cols_a = int(entry_cols_a.get())
        rows_b = int(entry_rows_b.get())
        cols_b = int(entry_cols_b.get())

        create_matrix(entry_a, rows_a, cols_a, frame_a)
        create_matrix(entry_b, rows_b, cols_b, frame_b)

        matrix_a = np.array([[int(entry_a[row][col].get()) if is_valid_integer(entry_a[row][col].get()) else 0 for col in range(cols_a)] for row in range(rows_a)])
        matrix_b = np.array([[int(entry_b[row][col].get()) if is_valid_integer(entry_b[row][col].get()) else 0 for col in range(cols_b)] for row in range(rows_b)])

        if operation == "Tổng":
            result = matrix_a + matrix_b
        elif operation == "Hiệu":
            result = matrix_a - matrix_b
        elif operation == "Nhân phần tử":
            result = matrix_a * matrix_b
        elif operation == "Nhân ma trận":
            result = np.dot(matrix_a, matrix_b)
        else:
            result = "Lựa chọn không hợp lệ."

        result_text.set(f"Kết quả {operation}:\n{result}")

    except ValueError:
        result_text.set("Nhập không hợp lệ. Vui lòng nhập số nguyên hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy Tính Ma Trận")

# Đặt kích thước của cửa sổ
root.geometry("700x600")

# Tạo khung cho ma trận A và B
frame_a = tk.Frame(root)
frame_b = tk.Frame(root)

frame_a.grid(row=5, column=0, columnspan=2, pady=5)
frame_b.grid(row=5, column=2, columnspan=2, pady=5)

# Tạo ô nhập liệu cho số hàng và cột của ma trận A và B
label_rows_a = tk.Label(root, text="Số hàng của ma trận A:")
label_cols_a = tk.Label(root, text="Số cột của ma trận A:")
label_rows_b = tk.Label(root, text="Số hàng của ma trận B:")
label_cols_b = tk.Label(root, text="Số cột của ma trận B:")
entry_rows_a = tk.Entry(root)
entry_cols_a = tk.Entry(root)
entry_rows_b = tk.Entry(root)
entry_cols_b = tk.Entry(root)
label_rows_a.grid(row=0, column=0, padx=5, pady=5)
label_cols_a.grid(row=1, column=0, padx=5, pady=5)
label_rows_b.grid(row=2, column=0, padx=5, pady=5)
label_cols_b.grid(row=3, column=0, padx=5, pady=5)
entry_rows_a.grid(row=0, column=1, padx=5, pady=5)
entry_cols_a.grid(row=1, column=1, padx=5, pady=5)
entry_rows_b.grid(row=2, column=1, padx=5, pady=5)
entry_cols_b.grid(row=3, column=1, padx=5, pady=5)
# Tạo nút để tạo ma trận
create_matrix_button_a = tk.Button(root, text="Tạo Ma Trận A", command=lambda: create_matrix(entry_a, int(entry_rows_a.get()), int(entry_cols_a.get()), frame_a))
create_matrix_button_b = tk.Button(root, text="Tạo Ma Trận B", command=lambda: create_matrix(entry_b, int(entry_rows_b.get()), int(entry_cols_b.get()), frame_b))
create_matrix_button_a.grid(row=4, column=0, columnspan=2, pady=10)
create_matrix_button_b.grid(row=4, column=2, columnspan=2, pady=10)
# Tạo nhãn cho ma trận A và B
label_a = tk.Label(root, text="Ma trận A:")
label_b = tk.Label(root, text="Ma trận B:")
# Đặt nhãn trên lưới
label_a.grid(row=6, column=0, columnspan=2, pady=5)
label_b.grid(row=6, column=2, columnspan=2, pady=5)
# Tạo ô nhập liệu cho ma trận A và B
entry_a = []
entry_b = []
# Tạo nút để tính toán
operations = ["Tổng", "Hiệu", "Nhân phần tử", "Nhân ma trận"]
buttons = []
for i, operation in enumerate(operations):
    button = tk.Button(root, text=operation, command=lambda op=operation: perform_operation(op))
    button.grid(row=7, column=i, padx=5, pady=10)
    buttons.append(button)
# Hiển thị kết quả
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=8, column=0, columnspan=4, pady=10)
# Tạo nút để xóa kết quả và dữ liệu
clear_button = tk.Button(root, text="Xóa Kết Quả và Dữ Liệu", command=clear_data)
clear_button.grid(row=9, column=0, columnspan=4, pady=10)
# Tạo nút để thoát
exit_button = tk.Button(root, text="Thoát", command=root.destroy)
exit_button.grid(row=10, column=0, columnspan=4, pady=10)
# Chạy vòng lặp sự kiện Tkinter
root.mainloop()