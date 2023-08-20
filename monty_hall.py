import random

total_tests = 100000
counter = total_tests
first_choice_sum = 0
second_choice_sum = 0

while counter > 0:
    counter -= 1

    # Creating a list of 3 items where one of them is correct 
    # (represented as number 1) and others are wrong
    items = [0, 0, 1]
    random.shuffle(items)

    # Taking a random choice from 3 items
    first_choice_index = random.randrange(0, 2)
    first_choice_sum += items[first_choice_index]

    # Finding an index of a wrong item that's not the first chosen item
    spoof_index = 0
    for i, item in enumerate(items):
        if i == first_choice_index:
            pass
        elif item == 0:
            spoof_index = i
            break

    # Finding the second item that which is not the spoof item, nor is it the first chosen item
    second_item_index = 0
    for i, item in enumerate(items):
        if i in [first_choice_index, spoof_index]:
            pass
        else:
            second_item_index = i
    second_choice_sum += items[second_item_index]

print(f"First choice is correct {first_choice_sum/total_tests*100}% of the time")
print(f"Second choice is correct {second_choice_sum/total_tests*100}% of the time")

    