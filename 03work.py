enter_hours = int(input("workhours:"))
enter_rate = int(input("rate:"))
if enter_hours <= 40:
    print("pay:", enter_hours * enter_rate)
else:
    print("pay", 400 + (enter_hours - 40) * 1.5 * enter_rate)

try:
    enter_hours = int(input("workhours:"))
    enter_rate = int(input("rate:"))
    if enter_hours <= 40:
        print("pay:", enter_hours * enter_rate)
    else:
        print("pay:", enter_rate * 40 + (enter_hours - 40) * 1.5 * enter_rate)
except:
    print("Error, please enter numeric input")


try:
    score = float(input("Enter score:"))
    if score < 6.0:
        print("E")
    elif score < 7.0:
        print("D")
    elif score < 8.0:
        print("C")
    elif score <9.0:
        print("B")
    elif score < 10:
        print("A")
    else:
        print("Bad score")
except:
    print("not a number")

