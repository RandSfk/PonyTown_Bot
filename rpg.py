import json,random

def read_usernames():
    with open('name.txt', 'r') as file:
        usernames = [line.strip() for line in file]
    return usernames

def load_data():
    try:
        with open('database.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        with open('database.json', 'w') as file:
            json.dump(data, file)
    return data

def save_data(data):
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_player(username):
    data = load_data()
    if username not in data:
        data[username] = {"gold": 0, "experience": 0, "inventory": {}}
        save_data(data)

def get_player_info(username):
    data = load_data()
    return data.get(username, {})

def update_player_info(username, gold_change=0, exp_change=0, inventory_change=None):
    data = load_data()
    player_data = data.get(username, {})
    player_data["gold"] = max(0, player_data.get("gold", 0) + gold_change)
    player_data["experience"] = max(0, player_data.get("experience", 0) + exp_change)
    player_data["inventory"] = player_data.get("inventory", {})
    if inventory_change:
        for item, quantity in inventory_change.items():
            player_data["inventory"][item] = max(0, player_data["inventory"].get(item, 0) + quantity)
    data[username] = player_data
    save_data(data)

def hunt(username):
    data = load_data()
    player = data.get(username)
    if player:
        if player["health"] > 0:
            loot_crates_obtained = random.choices([0, 1], [0.8, 0.2])[0] 
            if loot_crates_obtained:
                player["inventory"].setdefault("Loot Crate", 0)
                player["inventory"]["Loot Crate"] += 1
            
            # Mendapatkan reward
            rewards = ["Gold", "Experience", "Sword", "Shield", "Potion"]
            reward = random.choice(rewards)
            if reward == "Gold":
                gold_amount = random.randint(10, 50)
                update_player_info(username, gold_change=gold_amount)
                message = f"{username}, you got 💎{gold_amount} gold!"
            elif reward == "Experience":
                exp_amount = random.randint(20, 50)
                update_player_info(username, exp_change=exp_amount)
                message = f"{username}, you got ⚪ an experience boost of {exp_amount}!"
            elif reward in ["Sword", "Shield", "Potion"]:
                update_player_info(username, inventory_change={reward: 1})
                message = f"{username}, you got a {reward}!"
            else:
                message = ""
            damage_taken = random.randint(5, 15)
            damage_taken_after_reduction = max(0, damage_taken - player.get("damage_reduction", 0))
            player["health"] = max(0, player["health"] - damage_taken_after_reduction)
            attack_damage_stat = player["attack_damage"]

            save_data(data)

            return f"{username}, you went hunting and obtained {loot_crates_obtained} loot crates. You took {damage_taken_after_reduction} damage. Your attack damage: {attack_damage_stat}. {message}"
        else:
            return "You cannot hunt because your health is too low."
    else:
        return "Player not found."

    
def use(username, item):
    data = load_data()
    player = data.get(username)
    if player:
        inventory = player["inventory"]
        if item in inventory and inventory[item] > 0:
            if item == "Shield":
                damage_reduction = random.randint(1, 5)
                player["damage_reduction"] = damage_reduction
                update_player_info(username, inventory_change={item: -1})
                return f"{username} used {item} and will receive {damage_reduction}% less damage during hunting."
            elif item == "Sword":
                attack_bonus = round(player["attack_damage"] * 0.03)
                player["attack_bonus"] = attack_bonus
                update_player_info(username, inventory_change={item: -1})
                return f"{username} used {item} and gained {attack_bonus}% additional attack damage."
            elif item == "Potion":
                health_recovered = random.randint(20, 50)
                player["health"] = min(100, player["health"] + health_recovered)
                update_player_info(username, inventory_change={item: -1})
                return f"{username} used {item} and recovered {health_recovered} health points."
            else:
                return f"{username} cannot use {item}."
        else:
            return f"{username} does not have {item} in their inventory."
    else:
        return "Player not found."

def gacha(username):
    rewards = ["Sword", "Shield", "Potion", "Gold", "Experience Boost"]
    reward = random.choice(rewards)
    if reward == "Gold":
        gold_amount = random.randint(10, 50)
        update_player_info(username, gold_change=gold_amount)
        return f"{username}, you got {gold_amount} gold!"
    elif reward == "Experience Boost":
        exp_amount = random.randint(20, 50)
        update_player_info(username, exp_change=exp_amount)
        return f"{username}, you got an experience boost of {exp_amount}!"
    else:
        update_player_info(username, inventory_change={reward: 1})
        return f"{username}, you got a {reward}!"

def view_inventory(username):
    player_info = get_player_info(username)
    inventory = player_info.get("inventory", {})
    if inventory:
        items = ", ".join([f"{item}🍷: {quantity}" for item, quantity in inventory.items()])
        return f"{username}'s Inventory: {items}"
    else:
        return f"{username}'s Inventory is empty."
    
def buy(username, item):
    prices = {"Sword": 50, "Shield": 40, "Potion": 20}
    player_info = get_player_info(username)
    gold = player_info.get("gold", 0)

    if item in prices:
        if gold >= prices[item]:
            update_player_info(username, gold_change=-prices[item], inventory_change={item: 1})
            return f"{username} has purchased {item}."
        else:
            return f"{username} doesn't have enough gold to buy {item}."
    else:
        return f"Item {item} is not available for purchase."

def sell(username, item, quantity):
    prices = {"Sword": 30, "Shield": 20, "Potion": 10}
    player_info = get_player_info(username)
    inventory = player_info.get("inventory", {})
    gold = player_info.get("gold", 0)

    if item in inventory and inventory[item] >= quantity:
        update_player_info(username, gold_change=prices[item]*quantity, inventory_change={item: -quantity})
        return f"{username} has sold {quantity} {item}(s) for {prices[item]*quantity} 💎gold."
    else:
        return f"{username} doesn't have enough {item} to sell."

def exchange_items(sender, receiver, sender_item, receiver_item):
    sender_info = get_player_info(sender)
    receiver_info = get_player_info(receiver)
    sender_inventory = sender_info.get("inventory", {})
    receiver_inventory = receiver_info.get("inventory", {})

    if sender_item in sender_inventory and receiver_item in receiver_inventory:
        sender_quantity = sender_inventory[sender_item]
        receiver_quantity = receiver_inventory[receiver_item]

        sender_inventory[sender_item] = receiver_quantity
        receiver_inventory[receiver_item] = sender_quantity

        update_player_info(sender, inventory_change={sender_item: -sender_quantity, receiver_item: receiver_quantity})
        update_player_info(receiver, inventory_change={receiver_item: -receiver_quantity, sender_item: sender_quantity})

        return f"{sender} has exchanged {sender_quantity} {sender_item}(s) with {receiver}'s {receiver_quantity} {receiver_item}(s)."
    else:
        return f"Either {sender} or {receiver} doesn't have enough of the specified items to exchange."

def view_status(username):
    player_info = get_player_info(username)
    gold = player_info.get("gold", 0)
    exp = player_info.get("experience", 0)
    health = player_info.get("health", 0)
    attack_damage = player_info.get("attack_damage", 0)
    return f"{username} Stats = Gold:{gold}, Exp:{exp}, Hp:{health}, Attack:{attack_damage}"


def travel(username, location):
    if location == "forest":
        return f"{username} is traveling to the forest..."
    elif location == "town":
        return f"{username} is traveling to the town..."
    else:
        return f"{location} is not a valid travel destination."

