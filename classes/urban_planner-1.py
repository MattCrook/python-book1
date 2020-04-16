class Bank:

    def __init__(self, name):
        self.business_name = name
        self.customers = list()


first_tennessee = Bank("First Tennessee")


class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


mo = Customer("Mo", "Silvera")
warner = Customer("Warner", "Carpenter")
ken = Customer("Ken", "Perkerwicz")

# add the object references to the customers list on the bank.
first_tennessee.customers.append(mo)
first_tennessee.customers.append(warner)
first_tennessee.customers.append(ken)

# Now the object have a relationship with each other. If you want to view all the customers of a bank,
# just iterate the customers list.

for customer in first_tennessee.customers:
    print(f'{customer.first_name} {customer.last_name} is a customer of {first_tennessee.business_name}')
'''
Mo Silvera is a customer of First Tennessee
Warner Carpenter is a customer of First Tennessee
Ken Perkerwicz is a customer of First Tennessee
'''

# *************************************** #
 # Practice Employee Departments


class Employee:
    def __init__(self, name, title):
        self._name = name
        self._title = title
        self._start_date = ""

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def set_start_date(self, date):
        self.start_date = date


class Company:
    def __init__(self, name, address, industry):
        self._name = name
        self._address = address
        self._industry = industry
        self.employees = list()

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_industry(self):
        return self.industry


raf = Employee("raf", "staff member")
raf.set_start_date("4/1/2020")

joe = Employee("joe", "engineer")
joe.set_start_date("1/1/2020")

bob = Employee("Bob", "software guy")
joe.set_start_date("9/1/2020")

company_1 = Company("NSS", "123 street", "computers")
company_2 = Company("BMG", "456 street", "other stuff")

company_1.employees.append(raf)
company_1.employees.append(joe)

company_2.employees.append(bob)


def employee_names():
    for employee in company_1.employees:
      return employee._name


print(f'{company_1._name} is in the {company_1._industry} industry and has the following employees {employee_names()}')
