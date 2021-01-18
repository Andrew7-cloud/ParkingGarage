""" Dictionaries: Unordered, Changeable, Duplicate keys not allowed """

# GENERAL #

# 1 Calcuate Dictionary Length
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}
dict_length = len(this_dict)
print(f"GENERAL #1 Calculate Dictionary Length: {dict_length}")


# ACCESING #

# 1 Access value of key using the format: dictionary_name[key]:
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict[selected_key]
print(
    f"ACCESSING #1 Access value of key using the format: dictionary_name[key]: {x}")


# 2 Access the value of -a- key using the dictionary_name.get(key_name) method:
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.get(selected_key)
print(
    f"ACCESSING #2 Access the value of -a- key using the dictionary_name.get(key_name) method: {x}")


# 3 Access -all- dictionary keys using the dictionary_name.key() method:
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.keys()
print(
    f"ACCESSING #3 Access -all- dictionary keys using the dictionary_name.key() method: {x}")


# 4 Access -all- dictionary values using the dictionary_name.values() method:
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.keys()
print(f"ACCESSING #3 Access -all- dictionary values using the dictionary_name.values() method: {x}")












# 2 accessing the value of a key, then treatment (.get method)
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict[selected_key]
print(x)


new_dict = {}

for x in range(1, 11):
    str_x = str(x)
    y = "False"
    new_dict.fromkeys(str_x, y)

    print(new_dict)


# test to change first key value pair that meets the condition (.items method)
thisdict = {1: "False", 2: "False", 3: "False", 4: "True"}

# .items pulls key value pairs
for x, y in thisdict.items():
    if y == "False":
        y = "True"
        print(x, y)

        # break ensures the first instance a value meets the "True" criteria, the code stops
        break


"""
x = ('key1','key2','key3')
y=0
dicta = dict.fromkey(x,y)
"""


car = {
    "lot1": "False",
    "lot2": "False",
    "lot3": "False"
}
print(f"Original car dictionary: {car}")

# returns each value in the car dictionary
x = car.values()
print(f"Printing the values of the dictionary: {x}")  # prints each value

# loop through values, find met criteria and edit value
for item in x:
    if item == "False":
        item = "True"
        break

print(f"Revised car dictionary: {car}")


# assess if key name exists among keys and then treatment
lot_dict = {
    "lot1": "False",
    "lot2": "False",
    "lot3": "False"
}

selected_lot = "lot3"

if selected_lot in lot_dict:
    # how do I change the value
    print("Yes, 'selected_lot' is one of the keys in the dictionary")
