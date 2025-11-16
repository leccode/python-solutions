import os

def cls() -> None:
    """
    This method is used to clear the console of the current running .py file.

    Args:
        None
    """
    os.system("cls" if os.name == "nt" else 'clear')

if __name__ == "__main__":
    cls()
