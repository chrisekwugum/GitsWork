def petfunct():
    petnames = []
    while True:
        petname = input("Enter your pet name (or type 'q' to quit): ")
        if petname.lower() == 'q':
            break
        else:
            petnames.append(petname)
    print(petnames)


petfunct()