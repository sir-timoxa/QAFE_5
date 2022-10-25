
#обычный класс
class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print(self.name, self.balance, self.passport)


account1 = BankAccount('Tony', 3371144, 12121212)
account1.print_data()
print(account1.name)
print(account1.balance)
print(account1.passport)
print()

#protected класс
class ProtBankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)


account2 = ProtBankAccount('Mike', 148821, 373737)
account2.print_protected_data()
print(account2._name)# доступ к переменным всё еще есть, и можно к ним обратиться
print(account2._balance)# одно_ обозначает что к данным переменным лучше обращаться внутри класса, но доступ если нужно к ним имеем
print(account2._passport)
print()

#protected класс
class PrivateBankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

    def setAccountData(self,name,balance,passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    def getAccountData(self):
        return  self.__name, self.__balance,self.__passport


account3 = PrivateBankAccount('Pablo', 355, 545454)
account3.print_private_data()
# print(account3.__name) # уже обратиться к переменным нельзя - ошибка, но внутри класса можно создать фкнцию, которая будет иметь к ним доступ см строки. 48-56
# print(account3.__balance)
# print(account3.__passport)


account3.setAccountData('NEwname',000,32132132)
account3.print_private_data()
print(account3.getAccountData())