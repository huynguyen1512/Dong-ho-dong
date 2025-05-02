import random
# Hàm mô phỏng 1 ván đấu súng
def simulate_game():
    # Xác suất bắn trúng của từng người
    accuracy = {'X': 0.5, 'Y': 0.4, 'Z': 0.3}
    # Trạng thái sống/chết của từng người (True = còn sống)
    alive = {'X': True, 'Y': True, 'Z': True}
    # Thứ tự bắn: Z -> Y -> X
    order = ['Z', 'Y', 'X']
    # Mỗi ván đấu có 3 vòng
    for _ in range(3): 
        for shooter in order: 
            if alive[shooter] ==True: #kiểm tra xem shooter còn sống không, nếu không thì qua người tiếp theo
                # Tìm danh sách đối thủ còn sống để chọn bắn và phải khác shooter
                targets = [p for p in alive if alive[p] and p != shooter]
                target = random.choice(targets)  # Chọn ngẫu nhiên đối thủ
                if random.random()<accuracy[shooter]:
                    alive[target] = False  # Đối thủ bị loại
        if list(alive.values()).count(True) == 1: #Nếu chỉ còn 1 người sống và chưa hết 3 vòng thì kết thúc game sớm
            break
    return alive['Z'] 
# Hàm mô phỏng nhiều lần và tính xác suất Z sống sót
def countZ(trials=100000):
    count_z = 0
    for _ in range(trials):
        if simulate_game()==True:
            count_z += 1
    return count_z / trials*100
a=countZ(trials=100000)
print("Xác suất Z sống là: " +str(a)+"%")
