Bếp ăn Thông minh - Recipe Finder
Đây là một dự án web application hoàn chỉnh, được xây dựng từ đầu, cho phép người dùng tìm kiếm công thức nấu ăn dựa trên các nguyên liệu họ có. Ứng dụng có một hệ thống xếp hạng thông minh để đề xuất các món ăn phù hợp nhất.

Dự án này là một hành trình đi từ một script Python đơn giản, nâng cấp dần qua các phiên bản:

V1.0: Script Python cơ bản (chạy trên Terminal).

V2.0: Nâng cấp lên CSDL SQLite (vẫn dùng logic LIKE đơn giản).

V3.0: Biến thành Web App (sử dụng Flask).

V4.0: Nâng cấp "bộ não" (Data Modeling) sang CSDL 3 bảng chuẩn hóa và "bộ não" SQL nâng cao (dùng JOIN/GROUP BY để xếp hạng).

V5.0: "Docker hóa" ứng dụng (sử dụng Dockerfile và docker-compose).

V6.0: Thiết lập CI/CD với GitHub Actions để tự động build và push lên Docker Hub.

*Tính năng chính
Giao diện Web: Giao diện web đơn giản, thân thiện được xây dựng bằng Flask.

Tìm kiếm thông minh: Người dùng nhập các nguyên liệu (cách nhau bởi dấu phẩy).

Hệ thống xếp hạng: Thay vì chỉ tìm các món "chính xác 100%", ứng dụng sử dụng một câu lệnh SQL nâng cao để xếp hạng tất cả các món có thể làm, ưu tiên các món phù hợp (dùng nhiều nguyên liệu của người dùng nhất).

CSDL chuẩn hóa: Dữ liệu được lưu trữ trong một CSDL quan hệ (3 bảng) để đảm bảo tính toàn vẹn và hiệu suất truy vấn cao.

* Công nghệ sử dụng
Backend: Python, Flask

Database: SQLite

Kỹ năng Data: Mô hình hóa Dữ liệu Quan hệ (Relational Data Modeling), SQL Nâng cao (Common Table Expressions, JOINs, GROUP BY, ORDER BY).

DevOps: Docker, Docker Compose, GitHub Actions (CI/CD)

Tools: Git, VSCode, Conda

*Hướng dẫn chạy dự án (với Docker)
Đây là cách chạy dự án được khuyến khích, vì nó đã bao gồm tất cả môi trường cần thiết.

Yêu cầu:
Git

Docker Desktop (Hãy đảm bảo nó đang chạy!)

Python (Chỉ cần để chạy script tạo CSDL 1 lần duy nhất)

Các bước:
Clone dự án:

Bash

git clone https://github.com/phuoc2907/du-an-cooking.git
cd du-an-cooking
Tạo Cơ sở dữ liệu (Quan trọng):

Bạn CẦN chạy script này MỘT LẦN để tạo file recipes.db.

Dockerfile của chúng ta được cấu hình để COPY file recipes.db này vào container.

Bash

python setup_database_v2.py
(Nó sẽ tạo ra file recipes.db chứa 15 món ăn).

Build và Chạy Container:

Bash

docker-compose up --build
Truy cập:

Mở trình duyệt (Chrome, Cốc Cốc...) và truy cập:

http://127.0.0.1:5000

*CI/CD (Tự động hóa)
Dự án này sử dụng một quy trình CI (Continuous Integration) cơ bản với GitHub Actions.

Kích hoạt (Trigger): Mỗi khi git push lên nhánh main.

Công việc (Job):

Tự động đăng nhập vào Docker Hub (sử dụng DOCKERHUB_USERNAME và DOCKERHUB_TOKEN đã lưu trong GitHub Secrets).

Tự động build (xây dựng) image Docker từ Dockerfile.

Tự động push (đẩy) image đó lên kho chứa Docker Hub:

phuoc04/du-an-cooking
