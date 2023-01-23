with open("CNAB.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome_loja = linha[60:81]
        print(nome_loja)
