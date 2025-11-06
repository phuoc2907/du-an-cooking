# Đây là file main.py (Phiên bản 2.0 - Dùng SQL)
import sqlite3

def tim_mon_an(nguyen_lieu_cua_ban):
    """
    Hàm này bây giờ sẽ truy vấn CSDL SQLite
    """
    print(f"Đang kiểm tra với các nguyên liệu: {nguyen_lieu_cua_ban}")
    
    # 1. Kết nối tới CSDL
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # 2. ----------- LOGIC CỐT LÕI (Bằng SQL) -----------
    # Xây dựng câu lệnh truy vấn SQL
    # Logic: Tìm các món ăn mà cột 'nguyen_lieu'
    # CÓ CHỨA TẤT CẢ các nguyên liệu người dùng có.
    
    query = "SELECT ten_mon, cach_lam FROM recipes WHERE "
    
    # Tạo các điều kiện "LIKE" cho mỗi nguyên liệu
    # Ví dụ: WHERE nguyen_lieu LIKE '%trứng%' AND nguyen_lieu LIKE '%hành lá%'
    dieu_kien_tim_kiem = []
    for nl in nguyen_lieu_cua_ban:
        # '%trứng%' nghĩa là tìm bất cứ thứ gì có chứa chữ "trứng"
        dieu_kien_tim_kiem.append(f"nguyen_lieu LIKE '%{nl}%'")
        
    # Nối các điều kiện lại bằng "AND"
    query += " AND ".join(dieu_kien_tim_kiem)
    
    # Đây là dòng DEBUG để kiểm tra xem câu lệnh SQL có đúng không
    print(f"[DEBUG] Đang thực thi lệnh SQL: {query}")

    # 3. Thực thi truy vấn và lấy kết quả
    try:
        cursor.execute(query)
        # fetchall() lấy tất cả các dòng kết quả
        cac_mon_nau_duoc = cursor.fetchall() 
    except sqlite3.Error as e:
        print(f"Lỗi truy vấn SQL: {e}")
        cac_mon_nau_duoc = [] # Trả về danh sách rỗng nếu lỗi

    # 4. Đóng kết nối
    conn.close()

    # 5. Trả về kết quả
    return cac_mon_nau_duoc

# -------------------------------------------------------------------
# ---------------- PHẦN GIAO DIỆN (Giữ nguyên) ----------------
# -------------------------------------------------------------------

print("Chào mừng đến với Bếp ăn thông minh! (Phiên bản 2.0 - SQL)")
print("Hãy nhập các nguyên liệu bạn có, cách nhau bởi dấu phẩy (,) ")

input_cua_nguoi_dung = input("Nguyên liệu của bạn: ")
danh_sach_nguyen_lieu = input_cua_nguoi_dung.split(',')

# Làm sạch dữ liệu
danh_sach_nguyen_lieu_sach = []
for nl in danh_sach_nguyen_lieu:
    sach_se = nl.strip() # .strip() là hàm xóa dấu cách thừa ở 2 đầu
    if sach_se: # Chỉ thêm nếu nguyên liệu không phải là rỗng
        danh_sach_nguyen_lieu_sach.append(sach_se)

# Gọi "Người đầu bếp" phiên bản SQL
cac_mon_nau_duoc = tim_mon_an(danh_sach_nguyen_lieu_sach)

# In kết quả
if not cac_mon_nau_duoc:
    print("\n-------------------------------------------------")
    print("Tiếc quá! Bạn không đủ nguyên liệu để nấu món nào trong CSDL.")
else:
    print("\n-------------------------------------------------")
    print(f"Tuyệt vời! Bạn có thể nấu {len(cac_mon_nau_duoc)} món sau:")
    
    # Kết quả trả về giờ là một danh sách các cặp (ten_mon, cach_lam)
    for mon in cac_mon_nau_duoc:
        print(f"\n--- Món: {mon[0]} ---") # mon[0] là ten_mon
        print(f"Cách làm: {mon[1]}") # mon[1] là cach_lam