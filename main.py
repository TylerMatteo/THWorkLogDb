from log import Log

log = Log()

while True:
    option = input("Would you like to enter a [n]ew entry, "
                   "[l]ookup an existing one, or [q]uit? ")

    if option.upper() == "N":
        log.new()
    elif option.upper() == "L":
        log.lookup()
    elif option.upper() == "Q":
        break
    else:
        print("Invalid option, please try again.")
