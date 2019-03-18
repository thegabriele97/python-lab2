import sys

def main(argv):
    lst = []

    print("Welcome to note 3000 revolution!")
    if len(argv) > 1:
        print("Loading from %s.." % argv[1])
        load_file(lst, argv[1])
        print("Done!")

    while True:
        print()
        selected_int = int(show_prompt())
        selected_int -= 1

        if selected_int == 0:
            note = input("Note: ")

            if note == "":
                print("Error: insert a name.\n")
                continue
            
            lst.append(note)
        
        elif selected_int == 1:
            note = input("Note: ")

            if not note in lst:
                print("Error: note isn't present in your list.\n")
            
            lst.remove(note)
        
        elif selected_int == 2:
            lst.sort()
            print()
            print(*map(lambda e: "%d) %s" % (lst.index(e) + 1, e), lst), sep=";\n", end=".\n")
        
        elif selected_int == 3:
            if len(argv) > 1:
                print("Saving to %s.." % argv[1])
                save_file(lst, argv[1])
                print("Done!")
            
            break

def show_prompt():
    entries = [
        "insert a new task (a string of text)",
        "remove a task (by typing its content, exactly)",
        "show all existing tasks, sorted in alphabetic order",
        "close the program"]

    print(*map(lambda e: "%d. %s" % (entries.index(e) + 1, e), entries), sep=";\n", end=".\n")
    return input(" > ")

def load_file(list_obj, file_name):
    
    file_in = open(file_name, "r")

    for line in file_in.readlines():
        list_obj.append(line[0:len(line) - 1])
    
def save_file(list_obj, file_name):

    file_out = open(file_name, "w")

    for note in list_obj:
        file_out.write(note + "\n")


if __name__ == "__main__":
    main(sys.argv)