import Dekodieren.py as dekodieren
import Kodieren.py as kodieren

zeichenkette = "hallo"
verschiebung = 4

print ("Originale Zeichenkette:", zeichenkette)
print ("Verschobene Zeichenkette:", kodieren.encoder(zeichenkette, verschiebung))
print ("Dekodierte Zeichenkette:", dekodieren.decoder(kodieren.encoder(zeichenkette, verschiebung), verschiebung))