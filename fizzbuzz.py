# Skill sharpening for python interview question

# Create a function that will only run if the file is imported as a module
def outside_scripts():
    print("This function only runs if the file is imported as a module.")

if __name__ == "__main__":

    # Get user input for fizzbuzz limit while making sure it's secure
    def get_limit():
        while True:
            try:
                limit = int(input("Enter a number for the fizzbuzz upper limit: "))
                return limit
            except ValueError:
                print("Please enter a valid integer.")

    # Write a program that prints the numbers from 1 to the user's upper limit.
    def fizzbuzz(limit):
        for i in range(1, limit + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    
    limit = get_limit() 
    fizzbuzz(limit)

