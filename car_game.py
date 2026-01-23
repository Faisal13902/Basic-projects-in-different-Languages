data = input(">")

while True:
    if data == "start":
        print("Car started...Ready to go!")
    elif data == "stop":
        print("Car Stopped.")
    elif data == "help":
        print("start to start the car" \
        "\nstop to stop the car" \
        "\nquit to exit")
    elif data == "exit" or data == "quit":
        break
    else:
        print("I don't understand that command")
    
    data = input(">")