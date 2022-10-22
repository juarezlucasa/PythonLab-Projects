def recorrer_lista(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)
