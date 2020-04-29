from os import system
returnMenu = "press \"Enter\" to return main menu"
class Customer():
    def __init__(self,aID:str,password:str,name:str):
        self.aID = aID
        self.name = name
        self.password = password
        self.balance = 0

class Bank():
    def __init__(self):
        self.customersList = list()

    def add_customer(self,aID:str,password:str,name:str):
        self.customersList.append(Customer(aID,password,name))
        print("{} thanks for create account at our bank".format(name))

def main():
    bank = Bank()
    while True:
        system("cls")
        print("""
        [1] I have an account
        [2] I want to create an account
        """)

        choice = input("Enter a number: ")

        if choice == "1":
            id_list = [i.aID for i in bank.customersList]
            ID = input("ID :")
            if ID in id_list:
                for customer in bank.customersList:
                    if ID == customer.aID:
                        print("Welcome {}".format(customer.name))
                        password = input("Password: ")
                        if password == customer.password:
                            print("Success")
                            while True:
                                system("cls")
                                print("""
                                [1] Check Balance
                                [2] Add Money
                                [3] Transfer Money
                                [4] Take Money
                                [0] Exit
                                """)

                                choice2 = input("Enter a number: ")

                                if choice2 == "1":
                                    print("Balance: {}".format(customer.balance))
                                    input(returnMenu)

                                elif choice2 == "2":
                                    num0 = int(input("Enter amount: "))
                                    confirm = input("Do you confirm? : Y/N\n")
                                    if confirm == "Y" or confirm == "y":
                                        customer.balance += num0
                                        print("Added!")
                                        input(returnMenu)

                                    elif confirm == "N" or confirm == "n":
                                        print("Canceled !!!")
                                        input(returnMenu)

                                    else:
                                        print("Error")
                                        input(returnMenu)

                                elif choice2 == "3":
                                    otherID = input("Enter the ID of the account you want to send: ")
                                    if otherID in id_list:
                                        for otherCustomer in bank.customersList:
                                            if otherID == otherCustomer.aID:
                                                num1 = int(input("Enter amount: "))
                                                if num1 <= customer.balance:
                                                    confirm1 = input("Do you confirm? : Y/N\n")
                                                    if confirm1 == "Y" or confirm1 == "y":
                                                        otherCustomer.balance += num1
                                                        customer.balance -= num1

                                                    elif confirm == "N" or confirm == "n":
                                                        print("Canceled !!!")
                                                        input(returnMenu)

                                                    else:
                                                        print("Error")
                                                        input(returnMenu)
                                                else:
                                                    print("your balance is insufficient")
                                                    input(returnMenu)
                                    else:
                                        print("{} account not found".format(otherCustomer.aID))
                                        input(returnMenu)

                                elif choice2 == "4":
                                    num2 = int(input("Enter amount: "))
                                    if num2 <= customer.balance:
                                        customer.balance -= num2
                                        print("Success!")
                                    else:
                                        print("your balance is insufficient")
                                        input(returnMenu)

                                elif choice2 == "0":
                                    break

        elif choice == "2":
            aID = input("ID: ")
            name = input("Name: ")
            password = input("Password: ")
            bank.add_customer(aID,password,name)
            print("Success!")
            input(returnMenu)

        else:
            print("Error")
            input(returnMenu)


if __name__ == "__main__":
    main()