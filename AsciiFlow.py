import os
import sys
import time

# Predefined shapes for animation
goshapes = [
     # Step 1
    "|_  ______________________| \n"
    "  \/ \n"
    "\n"
    " ( ') \n"
    "  | \n"
    "  | \n"
    "  | \n"
    "  |_ ",

     # Step 2
    "|___  ____________________| \n"
    "    \/ \n"
    "\n"
    "   ( ') \n"
    "   ||| \n"
    "   ||| \n"
    "   /\ \n"
    "  /_ |_ ",

     # Step 3
    "|___  ____________________| \n"
    "    \/ \n"
    "\n"
    "   ( ') \n"
    "   /|\ \n"
    "  / | \ \n"
    "   / \ \n"
    "  /_  \_ ",

     # Step 4
    "|_____  __________________| \n"
    "      \/ \n"
    "\n"
    "     ( ') \n"
    "     /|\ \n"
    "    / | \ \n"
    "     /| \n"
    "    /_|_ ",

     # Step 5
    "|_____  __________________| \n"
    "      \/ \n"
    "\n"
    "     ( ') \n"
    "     /|\ \n"
    "     ||| \n"
    "      | \n"
    "     /|_ "
]

backshapes = [
     # Step 1
    "|_____  __________________| \n"
    "      \/ \n"
    "\n"
    "     (' ) \n"
    "       | \n"
    "       | \n"
    "       | \n"
    "      _| ",

     # Step 2
    "|___  ____________________| \n"
    "    \/ \n"
    "\n"
    "   (' ) \n"
    "    ||| \n"
    "    ||| \n"
    "     /\ \n"
    "   _| _\ ",

     # Step 3
    "|___  ____________________| \n"
    "    \/ \n"
    "\n"
    "   (' ) \n"
    "    /|\ \n"
    "   / | \ \n"
    "    / \ \n"
    "  _/  _\ ",

     # Step 4
    "|_  ______________________| \n"
    "  \/ \n"
    "\n"
    " (' ) \n"
    "  /|\ \n"
    " / | \ \n"
    "   |\ \n"
    "  _|_\ ",

     # Step 5
    "|_  ______________________| \n"
    "  \/ \n"
    "\n"
    " (' ) \n"
    "  /|\ \n"
    "  ||| \n"
    "   | \n"
    "  _|\ "
]

def clear_screen():
    """Clears the console screen using the best method for the os."""
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS and Linux
        os.system('clear')

def print_text_in_box(text, spaces, line_length=26):
    """
    Prints text within a graphical box with margins adjusted.

    Args:
    text (str): The text to display inside the box.
    spaces (int): Number of spaces to indent the box from the left side.
    line_length (int): The length of each line within the box, default is 26.
    """
    words = text.split()
    formatted_text = ""
    line = " " * spaces + "| "
    print(" " * spaces + " _________________________ ")
    for word in words:
        if len(line) + len(word) + 1 - spaces <= line_length:
            line += word + " "
        else:
            formatted_text += line.ljust(line_length + spaces) + "|\n"
            line = " " * spaces + "| " + word + " "
    if line:
        formatted_text += line.ljust(line_length + spaces) + "|"
    print(formatted_text)

def add_spaces_to_shapes(shapes, spaces):
    """
    Adjusts the shapes by adding spaces to the beginning of each line.

    Args:
    shapes (list of str): A list of shape strings.
    spaces (int): The number of spaces to add to the beginning of each line.

    Returns:
    list of str: The modified list of shapes with added spaces.
    """
    return ['\n'.join((' ' * spaces + line) for line in shape.split('\n')) for shape in shapes]

def animate_shapes(shapes, text, spaces, delay=0.2):
    """
    Sequentially animates a series of ASCII art shapes.

    Args:
    shapes (list of str): List of shape strings to animate.
    text (str): Text to display above the shapes.
    spaces (int): Number of spaces to indent the text and shapes.
    delay (float): Time delay in seconds between each shape, default is 0.2 seconds.
    """
    for shape in shapes:
        clear_screen()
        print_text_in_box(text, spaces)
        print(shape)
        time.sleep(delay)

def perform_animation(text, initial_spaces, speed):
    for _ in range(10):  # Animate forwards
        initial_spaces += 4
        modified_goshapes = add_spaces_to_shapes(goshapes, initial_spaces)
        animate_shapes(modified_goshapes, text, initial_spaces, speed)
    for _ in range(10):  # Animate backwards
        modified_backshapes = add_spaces_to_shapes(backshapes, initial_spaces)
        animate_shapes(modified_backshapes, text, initial_spaces, speed)
        initial_spaces -= 4

def show_menu():
    print("\nMenu:")
    print("1. Start Animation")
    print("2. Change Text")
    print("3. Set Speed")
    print("4. Exit")
    return input("Enter your choice: ")

def main_loop():
    initial_spaces = 0
    text = "Welcome to AsciiFlow!"
    speed = 0.2  # Default speed
    running = True
    while running:
        choice = show_menu()
        if choice == '1':
            perform_animation(text, initial_spaces, speed)
        elif choice == '2':
            text = input("Enter new text: ")
            perform_animation(text, initial_spaces, speed)  # Show animation with new text
        elif choice == '3':
            try:
                speed = float(input("Enter new speed (Default 0.2 sec): "))
                perform_animation(text, initial_spaces, speed)  # Show animation with new speed
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_loop()
