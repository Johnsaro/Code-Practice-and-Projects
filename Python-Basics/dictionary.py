


def player_status(name, level, skills, inventory):
    
    
    print(f"Name: {name}")
    print(f"Level: {level}")
    print(f"Skills: {skills}")
    print(f"[Inventory]\n")
    print(inventory)
    
    
    
player_info = {
    "name": "Player1",
    "level": 12,
    "skills": 4,
    "inventory": ["sword", "potion", "100G"]
}
    
    
player_status(**player_info) # calling default value of player

player_status(name="player2", level=20, skills=5, inventory=["dagger", "900G"]) # a new player with deff inventory

print(dir(player_info))
print(help(player_info))

print("========================")
print(player_info)
print("========================\n")

# Method: get(key, default) 
print(player_info.get("name")) #  Returns the value for a specified key. If the key doesn't exist, it returns a default value (e.g., "Unknown").


default_skills = dict.fromkeys(["strength", "agility"], 0)
print(default_skills)

# Method: setdefault(key, default)
health = player_info.setdefault("health", 100) #  This is useful when you need to ensure that a key has a value before performing operations.
print(health)


print(player_info.get("inventory"))

# Method: update({key: value})
player_info.update({"name": "GameMaster"})  # Adds new key-value pairs or updates existing ones in the dictionary.
print(player_info)


player_info.clear() # when you want to reset the dictionary or release its memory. Ideal when re-initializing data or when you no longer need the data.
print(player_info)

keys = player_info.keys()
for keys in player_info.keys():
    print(keys) 
# """
# name
# level
# skills
# inventory
# """

# Method: values()                            
value = player_info.values() # Returns a view object of all the values in the dictionary.
print(value) # dict_values(['Player1', 12, 4, ['sword', 'potion', '100G']])

# Method: items()
items = player_info.items()
for key, value in player_info.items(): # Use items() for looping through both keys and values simultaneously.
    print(f"{key}: {value}")
    
    
    
backup_player_info = player_info.copy()
print(backup_player_info)

# Method: popitem()
last_item = player_info.popitem() # Removes and returns the last key-value pair added to the dictionary.
print(last_item)

# # Method: pop(key, default)
removed_item = player_info.pop("inventory", "Not found") # Removes the specified key and returns its value. If the key doesn't exist, the default value is returned.
print(removed_item)

