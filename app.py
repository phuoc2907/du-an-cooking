# Đây là file app.py (Phiên bản 3.1 - Web App + Xếp Hạng)

import sqlite3
from flask import Flask, request

app = Flask(__name__)

def tim_mon_an(nguyen_lieu_cua_ban):
    """
    Hàm này sẽ tìm các món ăn và XẾP HẠNG chúng.
    Món nào dùng nhiều nguyên liệu bạn có nhất sẽ lên đầu.
    """
    print(f"Đang kiểm tra với các nguyên liệu: {nguyen_lieu_cua_ban}")
    
    if not nguyen_lieu_cua_ban:
        return []

    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    # 1. Xây dựng câu lệnh OR để lấy TẤT CẢ các món CÓ THỂ nấu
    query = "SELECT id, ten_mon, nguyen_lieu, cach_lam FROM recipes WHERE "
    dieu_kien_tim_kiem = []
    for nl in nguyen_lieu_cua_ban:
        # '%trứng%'
        dieu_kien_tim_kiem.append(f"nguyen_lieu LIKE '%{nl}%'")
        
    # Nối các điều kiện bằng "OR" thay vì "AND"
    query += " OR ".join(dieu_kien_tim_kiem)
    
    print(f"[DEBUG] Đang thực thi lệnh SQL: {query}")
    
    try:
        cursor.execute(query)
        # Lấy tất cả các món có chứa ít nhất 1 nguyên liệu
        tat_ca_mon_tim_thay = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Lỗi truy vấn SQL: {e}")
        conn.close()
        return []

    conn.close()

    # 2. Xếp hạng các món tìm được (Đây là phần "Data" của dự án)
    mon_an_xep_hang = []
    for mon in tat_ca_mon_tim_thay:
        # mon[0] = id, mon[1] = ten_mon, mon[2] = nguyen_lieu (chuỗi), mon[3] = cach_lam
        
        ten_mon = mon[1]
        cach_lam = mon[3]
        # Chuyển chuỗi "trứng,hành lá..." thành danh sách ['trứng', 'hành lá', ...]
        nguyen_lieu_cua_mon = mon[2].split(',') 
        
        # Đếm xem bạn có bao nhiêu % nguyên liệu cho món này
        so_nguyen_lieu_co = 0
        for nl_can_thiet in nguyen_lieu_cua_mon:
            # Kiểm tra xem có nguyên liệu nào bạn CÓ
            # khớp với nguyên liệu CẦN THIẾT không
            for nl_ban_co in nguyen_lieu_cua_ban:
                # Nếu 'thịt' (bạn có) nằm trong 'thịt ba chỉ' (cần)
                # Hoặc 'mắm' (bạn có) nằm trong 'nước mắm' (cần)
                if nl_ban_co in nl_can_thiet: 
                    so_nguyen_lieu_co += 1
                    break # Đã đếm, chuyển sang nguyên liệu cần thiết tiếp theo
        
        # Tính điểm
        # (ví dụ: 3/4 = 0.75 điểm)
        diem_so = so_nguyen_lieu_co / len(nguyen_lieu_cua_mon) 
        
        mon_an_xep_hang.append({
            "ten_mon": ten_mon,
            "cach_lam": cach_lam,
            "diem_so": diem_so, # % bạn có
            "chi_tiet": f"(Phù hợp: Có {so_nguyen_lieu_co} trên {len(nguyen_lieu_cua_mon)} nguyên liệu)"
        })

    # 3. Sắp xếp danh sách theo điểm số, từ cao xuống thấp
    mon_an_da_sap_xep = sorted(mon_an_xep_hang, key=lambda x: x['diem_so'], reverse=True)
    
    return mon_an_da_sap_xep

# 4. TẠO CÁC TRANG WEB (ROUTES) - Sửa lại phần hiển thị
@app.route('/')
def trang_chu():
    # Giữ nguyên
    return """
        <html>
            <body style="font-family: Arial, sans-serif; margin: 20px;">
                <h1>Bếp ăn thông minh (Phiên bản 3.1 - Xếp Hạng)</h1>
                <p>Hãy nhập các nguyên liệu bạn có, cách nhau bởi dấu phẩy (,):</p>
                <form action="/search" method="GET">
                    <input type="text" name="ingredients" size="50" style="padding: 5px;">
                    <input type="submit" value="Tìm kiếm" style="padding: 5px;">
                </form>
            </body>
        </html>
    """

@app.route('/search')
def trang_tim_kiem():
    input_cua_nguoi_dung = request.args.get('ingredients', '')
    
    danh_sach_nguyen_lieu = input_cua_nguoi_dung.split(',')
    danh_sach_nguyen_lieu_sach = []
    for nl in danh_sach_nguyen_lieu:
        sach_se = nl.strip()
        if sach_se:
            danh_sach_nguyen_lieu_sach.append(sach_se)
            
    # Gọi hàm logic SQL (PHIÊN BẢN MỚI)
    cac_mon_nau_duoc = tim_mon_an(danh_sach_nguyen_lieu_sach)
    
    # Xây dựng trang HTML kết quả
    html_ket_qua = f"""
        <html>
            <body style="font-family: Arial, sans-serif; margin: 20px;">
                <h2>Kết quả tìm kiếm cho: "{input_cua_nguoi_dung}"</h2>
                <a href="/">Quay lại trang chủ</a> <br><br>
    """

    if not cac_mon_nau_duoc:
        html_ket_qua += "<p>Tiếc quá! Không tìm thấy món nào có chứa nguyên liệu bạn nhập.</p>"
    else:
        html_ket_qua += f"<p>Tuyệt vời! Đây là các món được đề xuất, xếp hạng theo độ phù hợp:</p>"
        
        # In ra kết quả đã xếp hạng
        for mon in cac_mon_nau_duoc:
            ten_mon = mon["ten_mon"]
            cach_lam = mon["cach_lam"]
            chi_tiet = mon["chi_tiet"]
            
            html_ket_qua += f'<div style="border: 1px solid #ccc; padding: 10px; margin-top: 10px;">'
            html_ket_qua += f"<h3>--- Món: {ten_mon} ---</h3>"
            html_ket_qua += f"<b>{chi_tiet}</b>"
            html_ket_qua += f"<p>Cách làm: {cach_lam}</p>"
            html_ket_qua += f"</div>"

    html_ket_qua += "</body></html>"
    return html_ket_qua

# Dòng này để chạy server khi bạn bấm nút "Play" (▶️) trong VSCode
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')