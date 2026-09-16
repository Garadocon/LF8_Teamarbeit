
def encoder(zeichenkette, verschiebung):
    kodiert = ""
    zeichen = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in zeichenkette:
        if i.isupper():
            i = i.lower()
            index = zeichen.index(i)
            index += verschiebung
            index = index % len(zeichen)
            kodiert += zeichen[index].upper()
        else:
            index = zeichen.index(i)
            index += verschiebung
            index = index % len(zeichen)
            kodiert += zeichen[index]
    return kodiert  