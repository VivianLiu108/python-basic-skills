from random import randint

dice = [0]*7                # dice[0] = 0, dice[1] = 0, ... , dice[6] = 0
for i in range(10):         # i = 0, 1, ... ,9
    print(randint(1, 6))    # 1~6數字隨機取10次


for i in range(100):
    j = randint(1, 6)
    dice[j] += 1            # 當 j = 1, dice[1] + 1, ... , 計算1~6各自共選到幾次

for j in range(1,7):        # j = 1, 2, ... , 6    7為最後一個的後面一個, 並非 j
    print(dice[j])          # dice[0] = 0, 沒用到, 所以不需要顯示
