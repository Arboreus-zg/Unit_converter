print("Hello! This is unit converter. It will convert kilometers into miles. Just follow instruction on screen")

while True:

        kilometers = float(input("Enter a number in kilometers: "))
        conv_fac = 0.621371
        miles = kilometers * conv_fac
        print("Your kilometers converted into miles are: ", miles)

#Ovo dalje od 10-tog reda nisam znao sam rijesiti odnosno kopirao sam iz ponuđenog rješenja..

        choice = input("Would you like to do another conversion (y/n): ")

        if choice.lower() != "y" and choice.lower() != "yes":
            print("Thank you for using the converter")
            break






