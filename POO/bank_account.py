class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount,):
        if self.is_active:
            self.balance += amount
            print(f"Hola {self.account_holder} \n Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print(f"Hola {self.account_holder} \n No se puede depositar, Cuneta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Hola {self.account_holder} \n Se ha retirado {amount}. Saldo actual es: {self.balance}")
            else:
                print(f"Hola {self.account_holder} \n No se puede retirar, Cuneta inactiva")

    def desactivate_account(self):
        self.is_active = False
        print("Cuenta desactivada")

    def activate_account(self):
        self.is_active = True
        print("Cuenta activada")

#Crear Objetos.
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Mike", 1000)

#Llamda a los metodos

account1.deposit(200)
account2.deposit(100)
account1.desactivate_account()
account1.deposit(200)
