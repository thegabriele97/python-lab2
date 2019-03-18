def main():
    print()
    show_prompt()

def show_prompt():
    entries = [
        "insert a new task (a string of text)",
        "remove a task (by typing its content, exactly)",
        "show all existing tasks, sorted in alphabetic order",
        "close the program"]

    print(*map(lambda e: "%d. %s" % (entries.index(e) + 1, e), entries), sep=";\n", end=".\n")
    return input(" > ")


if __name__ == "__main__":
    main()