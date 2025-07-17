chai_types = {
    "masala": "spicy",
    "ginger": "zesty",
    "green":"refreshing",
    "black": "bold",
}

for tea in chai_types:
    print(tea, chai_types[tea])

masala spicy
ginger zesty
green refreshing
black bold

for key , value in chai_types.items():
    print(key, value)

#output
masala spicy
ginger zesty
green refreshing
black bold

if "masala" in chai_types:
    print("Masala chai is available.")
else:
    print("Masala chai is not available.")
#output
Masala chai is available.

len(chai_types)  # returns the number of items in the dictionary
#output
4   

# Adding a new item to the dictionary
chai_types["cardamom"] = "aromatic"
print(chai_types)
#output
{'masala': 'spicy', 'ginger': 'zesty', 'green':
    'refreshing', 'black': 'bold', 'cardamom': 'aromatic'}

# Removing an item from the dictionary
# it delete referance from memery for the key "black"

del chai_types["black"]
print(chai_types)
#output
{'masala': 'spicy', 'ginger': 'zesty', 'green': 'refreshing', 'cardamom': 'aromatic'}
# Checking if a key exists in the dictionary
if "ginger" in chai_types:
    print("Ginger chai is available.")
else:
    print("Ginger chai is not available.")
#output
Ginger chai is available. 

chai_types.clear()  # removes all items from the dictionary
>>> chai_types.clear()
>>> chai_types
{}

chai_types.pop("ginger")  # removes the item with key "ginger"
# will return the value "zesty"
print(chai_types)
#output 
{'masala': 'spicy', 'green': 'refreshing', 'cardamom': 'aromatic'}


>>> chai_types
{'masala': 'spicy', 'ginger': 'zesty', 'green': 'refreshing', 'black': 'bold'}
chai_types.popitem()  # removes and returns the last inserted item
# will return ('black', 'bold')
print(chai_types)
#output
{'masala': 'spicy', 'ginger': 'zesty', 'green': 'refreshing'}

tea_shop = {
    "chai:{
        "masala": "spicy",
        "ginger": "zesty",
        "green": "refreshing",
        "black": "bold"
    },
    "Tea":{
        "oolong": "smooth",
        "white": "delicate",
        "herbal": "calming"
    },
}

print(tea_shop)
#output
{'chai': {'masala': 'spicy', 'ginger': 'zesty', 'green': 'refreshing', 'black': 'bold'}, 'Tea': {'oolong': 'smooth', 'white': 'delicate', 'herbal': 'calming'}} 


>>> sq= {x :x*2 for x in range(6)}
>>> sq
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
>>> sq_list = [x**2 for x in range(1,10)]
>>> sq_list
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 

keys =["masala", "ginger", "green", "black"]
default_values = "delicious"

new_dict = dict.fromkeys(keys, default_values)
print(new_dict)
#output
{'masala': 'delicious', 'ginger': 'delicious', 'green': 'delicious', 'black': 'delicious'}

