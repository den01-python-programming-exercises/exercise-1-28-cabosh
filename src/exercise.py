def main():
    #write your code below this line
    password = ("Caput Draconis")

    guess = input("What is the password? ")
    if guess == password:
        print("Welcome!")
    else:
        print("Off with you!")

if __name__ == '__main__':
    main()
