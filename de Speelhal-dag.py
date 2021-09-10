waardeP = float(input("waarde van koste voor persoon ")) #origineel 3 euro
waardeT = float(input("waarde toegangsticket ")) #origineel 7.45 euro
waardeVt = float(input("aantal minuten ")) #origineel 45 minuten
waardeVk = float(input("Koste per 5 minuyen ")) #euro, het kost 0.37 per 5 minuten

persoon = waardeP
toegangsticket = waardeT
VIPVRtijd = waardeVt
VIPVRkoste = waardeVk

print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar " + (str(int( persoon * toegangsticket + VIPVRtijd / 5 * VIPVRkoste)) + " euro."))