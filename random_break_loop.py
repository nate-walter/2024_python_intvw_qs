# Practice problem for python intervews Using the `if __name__ == "__main__":` statement, break the loop in the `get_user_list()` function.
import random

if __name__ == "__main__":
    numbers = list(range(1, 11)) # Create a list of numbers 1-10
    random.shuffle(numbers) # Shuffle the list
    for num in numbers:
        if num == 5:
            break
        print(num)