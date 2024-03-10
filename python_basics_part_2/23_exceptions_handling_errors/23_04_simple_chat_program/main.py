# Simple Chat Program
# This script simulates a basic chat application, allowing a user to view messages, send messages, and exit.

def display_chat() -> None:
    """
    Displays the current chat messages from a log file.
    """
    try:
        with open("chat_log.txt", "r") as file:
            chat_messages = file.read()
            print("\n=== Current Chat Text ===")
            print(chat_messages)
            print("==========================\n")
    except FileNotFoundError:
        print("Chat file not found. No messages yet.\n")
    except Exception as e:
        print(f"Error reading the chat: {e}\n")


def send_message(username: str) -> None:
    """
    Prompts the user to send a message and appends it to the chat log file.

    Args:
        username (str): The name of the user sending the message.
    """
    try:
        message = input("Enter your message: ")
        if not message:
            raise ValueError("Message cannot be empty.")

        formatted_message = f"{username}: {message}"

        with open("chat_log.txt", "a") as file:
            file.write(formatted_message + "\n")

        print("Message sent!\n")
    except ValueError as ve:
        print(f"Error: {ve}\n")
    except Exception as e:
        print(f"Error sending message: {e}\n")


def chat_program() -> None:
    """
    The main function of the chat program.
    """
    username = input("Enter your name: ")
    print(f"Hello, {username}!")

    while True:
        print("Choose an action:")
        print("1. View current chat text")
        print("2. Send a message")
        print("3. Exit the chat")

        choice = input("Your choice: ")

        if choice == '1':
            display_chat()
        elif choice == '2':
            send_message(username)
        elif choice == '3':
            print("Exiting the chat. Goodbye!")
            break
        else:
            print("Incorrect choice. Please choose 1, 2, or 3.\n")


# Running the chat program
chat_program()
