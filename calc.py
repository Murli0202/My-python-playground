input1 = input ("Gib eine Zahl ein: ")
input2 = input ("Gib eine zweite Zahl ein: ")
input3 = input ("Gib ein Rechenzeichen ein: ")
if input3 == "+":
    print (int(input1) + int(input2))
elif input3 == "-":
    print (int(input1) - int(input2))
elif input3 == "*":
    print (int(input1) * int(input2))
elif input3 == "/":
    print (int(input1) / int(input2))
else:
    print ("Ungültiges Rechenzeichen")