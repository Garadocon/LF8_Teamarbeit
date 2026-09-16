from Dekodieren import decoder
from Kodieren import encoder

zeichenkette = "Hallo"
verschiebung = -5

print ("Originale Zeichenkette:", zeichenkette)
print ("Verschobene Zeichenkette:", encoder(zeichenkette, verschiebung))
#print ("Dekodierte Zeichenkette:", decoder(encoder(zeichenkette, verschiebung), verschiebung))


def brute_force(verschobene_zeichenkette):
    for i in range(1, 26):
        print("Verschiebung:", i, "Dekodierte Zeichenkette:", decoder(verschobene_zeichenkette, i))

brute_force(encoder(zeichenkette, verschiebung))
