
"""
Mini-Project: ASCII Art Generator
Tạo chương trình in hình ASCII đẹp từ tên người dùng.
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")
print("Tên của bạn là:", ten)

# Bước 2: Tính độ rộng khung
width = len(ten) + 2
print("Độ rộng khung:", width)

# Bước 3: In khung trên
print('╔' + '═' * width + '╗')

# Bước 4: In nội dung
print('║' + ten.center(width) + '║')

# Bước 5: In khung dưới
print('╚' + '═' * width + '╝')

# Gợi ý: Dùng str.center(width) để căn giữa
