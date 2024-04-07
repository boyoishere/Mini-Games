import random

degarr = [0, 22.5, 45, 67.5]
zedarr = [0, 22.5, 45, 67.5]

while True:
    cmd = input("Press Enter to continue, press q to quit: ")
    if cmd == 'q':
        break
    deg = random.choice(degarr)
    zed = random.choice(zedarr)

    print(deg, "degrees right and", zed, "degrees down\n")