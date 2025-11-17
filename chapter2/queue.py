'''
    Author: Constantine Lekkos
    Created Date: 16/11/2025
    Purpose: Implementation of Queue Data Structure similarly to Stack implementation using list
'''

import re
from clear_console import cls

cls()

queue = [] # Empty queue
num = 0 # Variable to store

# Insert an item onto the queue
def right_push(queue_list: list[int], item: int) -> None:
    """
    A method to insert the first element at the right of the list. FIFO approach.

    Args:
        queue_list (list[int]): A list to manipulate.
        item (int): The number to handle.
    Returns:
        None
    """
    queue_list.append(item)

# Pop an item from the queue
def left_pop(queue_list: list[int]) -> int | None:
    """
    A method to pop the first element at the left of the list. FIFO approach.

    Args:
        queue_list (list[int]): A list to manipulate.
    Returns:
        int or None
    """
    return queue_list.pop(0) if queue_list else print(f"Queue is empty {queue_list}")

# Prints the Queue
def print_queue(queue_list: list[int]) -> None:
    """
    A method to print the current state of the Queue.

    Args:
        queue_list (list[int]): A list to print.
    Returns:
        None
    """
    print(f"Current Queue: {queue_list}") if queue_list else print(f"Queue is empty {queue_list}")

# Menu
def print_menu() -> None:
    """
    A method to print the current menu of the Queue Operations providing choices for the user.

    Returns:
        None
    """
    print()
    print("1. Insert right wise")
    print("2. Get from left")
    print("3. Print queue's current state")
    print("4. q\Q\-uit\e\E\-xit for Quit")
    print()

def get_choice():
    """
    A method to let the user to choose with an input() method.

    Returns:
        None
    """
    return input("Please, provide a choice:\n")

def main() -> None:
    """
    Main entry point of the current logic

    Returns:
        None
    """
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue
        
        if choice in ("q", "Q", "e", "E", "Quit", "quit", "Exit", "exit"):
            break
        
        # r: Raw string literal
        # ^: Asserts position at the start of the string
        # \d: Matches any digit (0-9)
        # \d+: Mathces any digit (0-9). These digits can be 1 or more
        # $: Asserts position at the end of the string
        pattern = r"^\d$"

        valid = re.match(pattern, choice)

        if not valid:
            print("Error in choice")
            continue
        
        choice = int(choice)
        match choice:
            case 1:
                num = input("Please, insert a number: ")
                pattern = r"^\d+$"
                valid = re.match(pattern, num)

                if not valid:
                    print("Error")
                    continue
                
                num = int(num)
                right_push(queue, num)
                print(str(num) + " inserted")
            case 2:
                out_num = left_pop(queue)
                if out_num is not None:
                    print(f"You got: {out_num}")
            case 3:
                print_queue(queue)
            case _:
                print("Not valid choice")

if __name__ == "__main__":
    main()
