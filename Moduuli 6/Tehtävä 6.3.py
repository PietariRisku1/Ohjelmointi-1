def muuntaja():
    while True:
        gallonit = float(input("Anna gallonien määrä: "))
        if gallonit < 0:
            print("Negatiivinen summa, ei hyväksytä")
            break
        litrat = gallonit * 3.785
        print(f"{gallonit} gallonit on {litrat} litraa.")

muuntaja()



