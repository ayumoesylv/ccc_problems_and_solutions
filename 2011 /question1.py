input_antennas = int(input("How many antennas?"))
input_eyes = int(input("How many eyes?"))

if input_antennas >= 3 and input_eyes <= 4:
    print("TroyMartian")

if input_antennas <= 6 and input_eyes >= 2:
    print("VladSaturnian")

if input_antennas <= 2 and input_eyes <= 3:
    print("GraemeMercurian")

