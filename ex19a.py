def bhp_and_whp (break_horsepower, wheel_horsepower):
    print ("Your car stats are:")
    print(f"Breaking Horsepower: {break_horsepower}")
    print(f"Wheel Horsepower: {wheel_horsepower}")
    if break_horsepower == wheel_horsepower:
        print("Your stats are well balanced")

bhp_and_whp (250, 300)
print("This is probably some type of truck \n")

focus_rs_bhp = 350
focus_rs_whp = 350

bhp_and_whp (focus_rs_bhp, focus_rs_whp)