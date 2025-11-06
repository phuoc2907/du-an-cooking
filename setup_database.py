# Đây là file setup_database.py
import sqlite3

# 1. Kết nối (hoặc tạo mới) file database
# File 'recipes.db' sẽ tự động được tạo ra
conn = sqlite3.connect('recipes.db')

# 2. Tạo một "con trỏ" (cursor) để thực thi lệnh
cursor = conn.cursor()

# 3. Tạo Bảng (TABLE)
# Đây là lệnh SQL để định nghĩa cấu trúc của CSDL
# LƯU Ý: Chúng ta sẽ lưu nguyên liệu dưới dạng 1 chuỗi văn bản, 
# ngăn cách bởi dấu phẩy (ví dụ: "trứng,hành lá,nước mắm")
cursor.execute('''
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_mon TEXT NOT NULL,
    nguyen_lieu TEXT NOT NULL,
    cach_lam TEXT
)
''')

# 4. Thêm dữ liệu (INSERT) vào Bảng
# Đây là dữ liệu chúng ta có từ trước
cac_mon_an = [
    # (Tên món, Nguyên liệu, Cách làm)
    ("Trứng chiên", "trứng,hành lá,nước mắm,dầu ăn", "Bước 1: Đập trứng..."),
    ("Thịt kho trứng", "thịt ba chỉ,trứng,nước dừa,nước mắm,đường", "Bước 1: Ướp thịt..."),
    ("Canh rau ngót thịt băm", "rau ngót,thịt băm,nước mắm,hành tím", "Bước 1: Phi hành..."),
    ("Rau muống luộc", "rau muống", "Bước 1: Đun sôi nước...")
]

# cursor.executemany() cho phép chèn nhiều dòng cùng lúc
# Các dấu ? sẽ được thay thế bởi dữ liệu trong 'cac_mon_an'
try:
    cursor.executemany("INSERT INTO recipes (ten_mon, nguyen_lieu, cach_lam) VALUES (?, ?, ?)", cac_mon_an)
except sqlite3.Error as e:
    print(f"Lỗi khi chèn dữ liệu: {e} (Có thể dữ liệu đã tồn tại, không sao cả)")

# 5. Lưu các thay đổi (commit) và đóng kết nối
conn.commit()
conn.close()

print("Database 'recipes.db' đã được tạo và chèn dữ liệu thành công!")