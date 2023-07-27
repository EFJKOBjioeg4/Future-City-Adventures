import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 100
        self.money = 1000
        self.inventory = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_status(player):
    print(f"\n{name}生命值：{player.health}  饥饿度：{player.hunger}  金币：{player.money}")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探险")
    print("4. 进行自由交易")
    print("5. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5）："))
            if 1 <= choice <= 5:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def explore(player):
    delay_print("\n你进入了未来城的街道，周围是高楼大厦和奇特的科技设施。")
    encounter = random.choice(["item", "danger", "nothing"])
    
    if encounter == "item":
        collect_item(player)
    elif encounter == "danger":
        danger_encounter(player)
    else:
        delay_print("这片区域看起来平静无事。")

def collect_item(player):
    item = random.choice(item_list)
    player.add_item(item)
    delay_print(f"你找到了{item.name}，{item.description}。")

def danger_encounter(player):
    damage = random.randint(10, 30)
    player.health = max(0, player.health - damage)
    delay_print("你遭遇了危险！")
    delay_print(f"你受到了{damage}点伤害，需要及时处理伤势。")

def trade_items(player, npc):
    print(f"\n欢迎来到交易所，{player.name}和{npc.name}！")
    show_inventory(player)
    show_inventory(npc)

    item_name = input(f"{player.name}，请输入你要交易的道具名字：")
    if item_name not in player.inventory:
        delay_print(f"{player.name}没有该道具，无法交易。")
        return

    quantity = int(input(f"{player.name}，请输入你要交易的{item_name}数量："))
    if player.inventory[item_name] < quantity:
        delay_print(f"{player.name}没有足够的{item_name}，无法交易。")
        return

    price = int(input(f"{npc.name}，请输入你愿意出售{item_name}的价格："))
    if price <= 0:
        delay_print(f"{npc.name}价格必须为正整数。")
        return

    total_cost = price * quantity
    if total_cost > player.money:
        delay_print(f"{player.name}没有足够的金币，无法交易。")
        return

    player.remove_item(Item(item_name, "", 0), quantity)
    player.money -= total_cost
    npc.add_item(Item(item_name, "", 0), quantity)
    npc.money += total_cost

    delay_print(f"交易完成！{player.name}交易了{quantity}个{item_name}，支付了{total_cost}个金币。")
    show_inventory(player)
    show_inventory(npc)

def show_inventory(player):
    print(f"\n{player.name}的背包：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name}: {quantity}个")

def interact_with_npc(player, npc):
    # 在这里添加与NPC的对话和交流功能
    pass

def play_game():
    player_name = input("请输入你的名字：")
    player = Player(player_name)
    
    item_list = [
        Item("药水", "恢复20点生命值", 50),
        Item("能量饮料", "恢复20点饥饿度", 30),
        Item("护身符", "提高10点生命值上限", 100),
        Item("技能书", "学习一种新技能", 200)
    ]

    npc_list = [
        Player("商贩1"),
        Player("商贩2"),
        Player("居民1"),
        Player("居民2"),
    ]

    delay_print(f"欢迎来到未来城生存游戏，{player_name}！")
    delay_print("你将在这座未来城市中展开冒险。")

    while True:
        show_status(player)
        action = choose_action()

        if action == 1:
            show_status(player)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            explore(player)
        elif action == 4:
            npc = random.choice(npc_list)
            trade_items(player, npc)
        elif action == 5:
            delay_print("谢谢你玩未来城生存游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()
