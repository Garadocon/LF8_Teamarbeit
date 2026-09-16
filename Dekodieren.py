
def decoder(zeichenkette, verschiebung):
    dekodiert = ""

    zeichen = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in zeichenkette:
        index = zeichen.index(i)
        index -= verschiebung
        index = index % len(zeichen)
        dekodiert += zeichen[index]
    return dekodiert