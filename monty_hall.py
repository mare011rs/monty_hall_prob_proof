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
    # This has 1/3 chance to be correct
    first_choice_index = random.randrange(0, 2)
    first_choice_sum += items[first_choice_index]

    # Remaining items that weren't chosen have 2/3 chance to have a correct answer

    # Finding an index of a wrong item that's not the first chosen item
    # First encountered wrong item is marked by taking its index
    wrong_choice_index = 0
    for i, item in enumerate(items):
        if i == first_choice_index:
            pass
        elif item == 0:
            wrong_choice_index = i
            break
    
    # Now that we found the wrong choice out of the remaining two we will remove it
    # This makes the only remaining item have the 2/3 chance to be correct

    # Finding the second item that which is not the wrong item, nor is it the first chosen item
    second_item_index = 0
    for i, item in enumerate(items):
        if i in [first_choice_index, wrong_choice_index]:
            pass
        else:
            second_item_index = i
    second_choice_sum += items[second_item_index]

print(f"First choice is correct {first_choice_sum/total_tests*100}% of the time")
print(f"Second choice is correct {second_choice_sum/total_tests*100}% of the time")

    