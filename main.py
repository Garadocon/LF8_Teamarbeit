from Dekodieren import decoder
from Kodieren import encoder

zeichenkette = "hallo"
verschiebung = 4

print ("Originale Zeichenkette:", zeichenkette)
print ("Verschobene Zeichenkette:", encoder(zeichenkette, verschiebung))
print ("Dekodierte Zeichenkette:", decoder(encoder(zeichenkette, verschiebung), verschiebung))