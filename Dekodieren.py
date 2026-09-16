input_string = input("Geben Sie den zu dekodierenden String ein: ")
dekodiert = ""

zeichen = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in input_string:
    index = zeichen.index(i)
    index -= 3
    index = index % len(zeichen)
    dekodiert += zeichen[index]



print("Der dekodierte String lautet: " + dekodiert)