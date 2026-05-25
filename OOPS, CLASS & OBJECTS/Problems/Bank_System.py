# todo : create a Bank system (using OOPS concepts) where a person can register as a customer by opening an account and performing transactions on it like adding value, withdrawl, viewing balance etc

# todo : Create a system which also helps you to know all your current customers

class Bank:

    customers = [] #You should store customers as a class variable, because all bank objects should share the same customer list.

    # Both the below functions are class methods because they deal with a shared data and not object specific data, registering a customer is attached to a Bank in itself, so creating an object makes no sense if there is no point of differentiation

    @classmethod
    def getLatestId(cls):
        # if list is empty it returns False
        if not cls.customers:
            return 1
        latestId = cls.customers[-1]["id"]  # because it is a dict
        return latestId+1


    @classmethod
    def registerCustomer(cls,name,age,gender,bal):
        latestId = cls.getLatestId()
        customer = {
            "id": latestId,
            "name":name,
            "age":age,
            "gender":gender,
            "balance":bal
        }

        Bank.customers.append(customer)
        pass

    @classmethod
    def viewCustomers(cls):
        print('\nHere are all the customers : \n')
        for cust in cls.customers:
            print(cust)

    @classmethod
    def viewCustomerData(cls):
        cust_id = int(input('Enter your id : '))
        for cust in cls.customers:
            if cust["id"] == cust_id:
                print('Here is your data : ',cust)
        
        else:
            print('No data found')



# Now we will create a Bank object, NOT a customer object, so we don't have to create a new object for every customer
obj = Bank()

obj.registerCustomer('Srajan',21,'Male',20000)
obj.registerCustomer('John',18,'Male',14000)


# Both these function below give the same output
obj.viewCustomers()
Bank.viewCustomers()

obj.viewCustomerData()
