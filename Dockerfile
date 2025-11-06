# Đây là file Dockerfile

# Bước 1: Bắt đầu từ một "hình ảnh" (image) có sẵn Python
# Chúng ta dùng bản 'slim' (siêu nhẹ) để container nhỏ gọn
FROM python:3.10-slim

# Bước 2: Đặt thư mục làm việc bên trong container
# Thay vì làm việc ở 'D:\...', trong container sẽ là '/app'
WORKDIR /app

# Bước 3: Sao chép các file cần thiết TỪ máy của bạn VÀO container
# Chép file 'app.py' và 'recipes.db' vào thư mục '/app'
COPY app.py .
COPY recipes.db .

# Bước 4: Cài đặt các thư viện (giống như 'conda install')
# Chúng ta dùng 'pip', trình quản lý gói mặc định của Python
# --no-cache-dir giúp container nhẹ hơn
RUN pip install --no-cache-dir flask

# Bước 5: Báo cho Docker biết, khi chạy, container này sẽ
# mở cổng 5000 (cổng mặc định của Flask)
EXPOSE 5000

# Bước 6: Lệnh cuối cùng để chạy ứng dụng khi container khởi động
# Tương đương với việc bạn gõ 'python app.py'
CMD ["python", "app.py"]