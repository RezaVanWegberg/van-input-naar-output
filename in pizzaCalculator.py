print("---------------------------")
print("| Pizza small is 5        |")
print("| Pizza medium is 8       |")
print("| Pizza large is 12       |")
print("---------------------------")

keuzepizza = input ("Kies uw afmeting ")

if keuzepizza == "small":
    prijspizza = float(5.00)
    hoeveelpizza = int(input("hoeveel pizza's wil u? "))
elif keuzepizza == "medium": 
    prijspizza = float(10.00)
    hoeveelpizza = int(input("hoeveel pizza's wil u? "))
elif keuzepizza == "large":
    prijspizza = float(15.00)
    hoeveelpizza = int(input("hoeveel pizza's wil u? "))
else:
    print ("no")

berekeningpizza = prijspizza * hoeveelpizza
print("Bedankt, het totale bedrag is dan " + str(berekeningpizza) + " euro. ")
