started = False
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car is sarted...")

    elif command == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car is stopped...")
    elif command == "help":
        print("""start - to start the car
stop  - to stop the car
exit  - to exit
        """)
    elif command == "exit":
        break
    else:
        print("I don't understand what are you saying!")

