# Đây là file our_database.py

# Chúng ta định nghĩa một "cơ sở dữ liệu" giả
# bằng một biến Python.
DATABASE = {
    # Món ăn có ID là 1
    1: {
        "ten_mon": "Trứng chiên",
        "nguyen_lieu": ["trứng", "hành lá", "nước mắm", "dầu ăn"],
        "cach_lam": "Bước 1: Đập trứng vào bát, thêm hành lá, nêm nước mắm, đánh đều. Bước 2: Đun nóng dầu ăn, đổ trứng vào chiên vàng đều 2 mặt."
    },
    
    # Món ăn có ID là 2
    2: {
        "ten_mon": "Thịt kho trứng",
        "nguyen_lieu": ["thịt ba chỉ", "trứng", "nước dừa", "nước mắm", "đường"],
        "cach_lam": "Bước 1: Ướp thịt với nước mắm, đường. Bước 2: Luộc trứng, bóc vỏ. Bước 3: Cho thịt, trứng, nước dừa vào nồi kho nhỏ lửa cho đến khi thịt mềm."
    },
    
    # Món ăn có ID là 3
    3: {
        "ten_mon": "Canh rau ngót thịt băm",
        "nguyen_lieu": ["rau ngót", "thịt băm", "nước mắm", "hành tím"],
        "cach_lam": "Bước 1: Phi hành tím cho thơm. Bước 2: Cho thịt băm vào xào săn. Bước 3: Đổ nước vào đun sôi, cho rau ngót vào, nêm nước mắm. Nấu thêm 2 phút."
    },
    
    # Món ăn có ID là 4 (chỉ cần 1 nguyên liệu)
    4: {
        "ten_mon": "Rau muống luộc",
        "nguyen_lieu": ["rau muống"],
        "cach_lam": "Bước 1: Đun sôi nước. Bước 2: Cho rau muống vào luộc chín tới. Bước 3: Vớt ra đĩa."
    }
}