inp_speed_lim = int(input("Enter the speed limit: "))
inp_recorded_spd = int(input("Enter the recorded speed of the car: "))

amount_over = inp_recorded_spd - inp_speed_lim

if amount_over <= 0:
    print("Congratulations, you are within the speed limit!")


elif 1 <= amount_over <= 20:
    print("You are speeding and your fine is $100")


elif 21 <= amount_over <= 30:
    print("You are speeding and your fine is $270")


elif amount_over >= 31:
    print("You are speeding and your fine is $500")