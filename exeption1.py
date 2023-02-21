while True:
    try:
        answer = float(input("How many hour did you work?"))
        payrate = 10.0
        print("Paychek amount: $", answer * payrate)
        break
    except:
        print("there was an error")

# The example above creates a loop that only breaks when the program runs


try:
    answer = float(input("How many hour did you work?"))
    payrate = 10.0
    print("Paychek amount: $", answer * payrate)
except:
    print("there was an error")
