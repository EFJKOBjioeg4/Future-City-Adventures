import time

def delay_print(text, delay=1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def introduction():
    delay_print("赛博朋克2088 - 欢迎来到未来的世界。")
    delay_print("你是一名赛博犯罪者，被通缉于全球。")
    delay_print("你的目标是生存下来，揭示这个黑暗的世界的秘密。")
    delay_print("你的冒险从一个陌生的赛博巷道开始...")
    time.sleep(1)

def cyberspace_alley():
    delay_print("你发现自己站在一个黑暗的赛博巷道中。")
    delay_print("在你的左边有一扇钢铁大门，右边是一条狭窄的小巷。")
    choice = input("你想要去哪里？（左/右）：").lower()
    if choice == "左":
        delay_print("你打开了钢铁大门，进入了一个地下夜总会。")
        night_club()
    elif choice == "右":
        delay_print("你选择了小巷，但很快发现它是一条死胡同。")
        delay_print("你觉得有点迷路，需要回去找另一条路。")
        cyberspace_alley()
    else:
        delay_print("无效的选择，请重新输入。")
        cyberspace_alley()

def night_club():
    delay_print("你进入了地下夜总会，音乐震耳欲聋，闪烁的霓虹灯光刺激着你的眼睛。")
    delay_print("你看到各种各样的人在这里，一些人在跳舞，一些人在交谈。")
    choice = input("你想要做什么？（跳舞/交谈/离开）：").lower()
    if choice == "跳舞":
        delay_print("你加入了舞池，与陌生人一起跳舞。")
        delay_print("一段时间后，你感到疲倦，决定离开。")
        cyberspace_alley()
    elif choice == "交谈":
        delay_print("你走到吧台旁，开始与陌生人交谈。")
        delay_print("你听到了一些关于未来世界的谣言和阴谋论。")
        delay_print("一位陌生人突然提到一个秘密的赛博地下组织，他们说他们能帮助你。")
        secret_organization()
    elif choice == "离开":
        delay_print("你离开了夜总会，回到了赛博巷道。")
        cyberspace_alley()
    else:
        delay_print("无效的选择，请重新输入。")
        night_club()

def secret_organization():
    delay_print("你决定追踪这个秘密组织的线索，看看他们是否能帮助你。")
    delay_print("你的旅程将在这里继续...")
    # 这里可以继续添加更多游戏情节和选择

if __name__ == "__main__":
    introduction()
    cyberspace_alley()
