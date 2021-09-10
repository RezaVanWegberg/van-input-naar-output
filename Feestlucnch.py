waardeC = float(input("geef de waarde van de crossaintjes "))
waardeS = float(input("geef de waarde van de stokbroden "))
waardeK = float(input("geef de waarde van de kortingsbonnen "))

croisantjes = waardeC
stokbroden = waardeS
kortingsbonnen = waardeK

print("De feestlunch kost je bij de bakker " +  (str(int( croisantjes * 17 + stokbroden * 2 - kortingsbonnen * 3) ) + " euro voor de crossaintjes en stokbroden als de kortingsbonnen nog geldig zijn")) 