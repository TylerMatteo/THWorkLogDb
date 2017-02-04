from log import Log

log = Log()

while True:
    option = input("Would you like to enter a [n]ew entry, "
                   "[l]ookup an existing one, or [q]uit? ")

    if option.upper() == "N":
        username = input("What is your name? ")
        task_name = input("What would you like to name this task? ")
        minutes = input("How many minutes have you spent working on it? ")
        try:
            log.add_entry(username, task_name, minutes)
        except ValueError:
            print("Invalid input. Please enter a number of minutes.")
            continue
    elif option.upper() == "L":
        while True:
            option = input("Would you like to lookup by [d]ate, "
                               "[e]mployee, or [s]earch term? ")
            if option.upper() in ['D','E','S']:
                log.lookup(option)
            else:
                print("Invalid option, please try again.")
    elif option.upper() == "Q":
        break
    else:
        print("Invalid option, please try again.")
