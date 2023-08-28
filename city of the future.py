import time

class Character:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

class Player:
    def __init__(self, name):
        self.name = name

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def explore_city(player):
    characters = [
        Character("机器人助手", "欢迎来到未来城市，我可以为你提供导航和信息。"),
        Character("科学家", "你是新来的吗？这个城市充满了科技和创新。"),
        Character("商人", "想要购买一些未来科技产品吗？我这里有最新的VR眼镜。"),
        Character("抵抗组织成员", "小心，这个城市背后隐藏着许多不为人知的秘密。"),
        Character("市民", "未来城市生活方便又舒适，我很喜欢这里。")
    ]

    delay_print(f"欢迎来到未来城市，{player.name}！")
    delay_print("你将在这个游戏中探索未来城市，与各种角色进行对话，完成任务和冒险。")

    while True:
        print("\n你遇到了以下角色：")
        for idx, character in enumerate(characters, start=1):
            print(f"{idx}. {character.name}")

        choice = input("请选择要与哪个角色对话（输入角色编号）：")
        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            selected_character = characters[int(choice) - 1]
            delay_print(f"\n{selected_character.name}: {selected_character.dialogue}")
        else:
            delay_print("无效的选择。")

        continue_choice = input("是否继续探索城市？(是/否): ").strip().lower()
        if continue_choice != "是":
            delay_print(f"谢谢参与未来城市冒险对话游戏！再见。")
            exit()

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    explore_city(player)

if __name__ == "__main__":
    main()
