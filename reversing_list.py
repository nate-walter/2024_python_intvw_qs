# Practice with reversing a list for interview prep

if __name__ == "__main__":
    
    def get_user_list():
        while True:
            user_input = input("Enter a list of elements. Get creative, just septerate them with spaces: ")
            user_list = user_input.split()
            if user_list:
                return user_list
            else:
                print("""\nPlease enter a valid list.\nDid you check if they had spaces between them?\nNo you didn't did you. I can't do this all myself can I.\nDid you even enter anything at all?\n""")

    def reverse_list(lst):
        return lst[::-1]
    
    user_list = get_user_list()
    reversed_list = reverse_list(user_list)
    print("\n===============================\n****Here's your reversed list: ", reversed_list, "\n===============================\n\n"
          "Anything else I can do for you. Maybe change your diaper?")

