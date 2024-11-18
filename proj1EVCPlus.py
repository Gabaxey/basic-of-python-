pin = 2354
furo = '*770#'
balance = 100

# Akhri furo ka isticmaalaha
user_furo = input()

if user_furo != furo:
    print("Hab khaldan ayaa isticmaalay!")
else:
    user_pin = int(input("Fadlan gali Pinkaaga: "))  # Akhri lambarka PIN-ka isticmaalaha.
    if user_pin == pin:

        print("1: Itus Haraaga \n2: Kaarka hadalka \n3: Bixi Biil \n4: U wareeji EVCPlus"
              + "\n5: Warbixin kooban \n6: Salaam Bank \n7: Maareyn \n8: Bill Payment")
        choice = input("fadlan dooro ")
        if choice == 1:
            print(f'Haraagaagu waa {balance}')
        else:
            print("Dooro")


# else:
#         print("PIN khaldan!")
       