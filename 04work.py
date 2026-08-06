def computepay_hours_rate():
    if enter_hours <= 40:
        print("pay:", enter_hours * enter_rate)
    else:
        print("pay:", enter_rate * 40 + (enter_hours - 40) * 1.5 * enter_rate)
try:
    enter_hours = int(input("workhours:"))
    enter_rate = int(input("rate:")) 
    computepay_hours_rate()
except:
    print("Error, please enter numeric input") # 典型为用而用的函数，没有复用的价值

def core():
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
try:
    score = float(input("Enter score:"))
    core()
except:
    print("not a number")
