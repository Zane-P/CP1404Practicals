import random

MIN_NUM = 1
MAX_NUM = 45
AMOUNT_OF_NUM = 6

num_picks = int(input("How many quick picks? "))
picks = []

for i in range(num_picks):
    picks.append([])
    for n in range(AMOUNT_OF_NUM):
        picks[i].append(random.randint(MIN_NUM, MAX_NUM))
        while picks[i][n] in picks[i][:n]:
            picks[i][n] = random.randint(MIN_NUM, MAX_NUM)
    picks[i].sort()
    print(" ".join("{}".format(pick) for pick in picks[i]))

