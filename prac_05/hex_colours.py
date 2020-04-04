
colour_to_hex = {"aliceblue": "#f0f8ff", "aquamarine1": "#7fffd4", "blue1": "#0000ff", "chartreuse1": "#7fff00",
                 "coral": "#ff7f50", "cyan1": "#00ffff", "darkorchid": "#9932cc", "firebrick": "#b22222",
                 "gold1": "#ffd700", "gray1": "#030303"}
print(colour_to_hex)

colour_code = input("Enter colour: ").lower()
while colour_code != "":
    if colour_code in colour_to_hex:
        print(colour_to_hex[colour_code])
    else:
        print("Invalid colour")
    colour_code = input("Enter colour: ")
