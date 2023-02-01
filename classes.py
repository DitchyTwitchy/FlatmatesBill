class MonthlyBill:
    """
    Class representing a bill for specific month
    params:
     - month: string(MM.YYYY)
     - total_amount: amount to be split between all tenants -> float rounded to 2 digits
     - list_of_tenants: list of names to split the bill -> [str]
     - days_per_tenant: days each tenant stayed at the apartment -> []
     - payment_split: fraction of the whole payment to be paid by each tenant -> []
     - amounts_to_pay: amount to be paid by each tenant -> []
     """
    def __init__(self, month: str, total_amount: float, list_of_tenants: list):
        self.total_amount = total_amount
        self.month = month
        self.list_of_tenants = list_of_tenants

    days_per_tenant = []
    payment_split = []
    amounts_to_pay = []

    def get_days_of_stay(self):
        days_per_tenant = []
        for tenant in self.list_of_tenants:
            print(f'Please enter the number of days {tenant} have stayed in {self.month}: ', end='')
            amount = input()
            days_per_tenant.append(int(amount))
        self.days_per_tenant = days_per_tenant

    def get_payment_split(self):
        total_days_of_stay = sum(self.days_per_tenant)
        self.payment_split = [day / total_days_of_stay for day in self.days_per_tenant]

    def get_amounts_to_pay(self):
        self.amounts_to_pay = [self.total_amount * split for split in self.payment_split]

    def process_bill(self):
        self.get_payment_split()
        self.get_amounts_to_pay()

    def __str__(self):
        data_representation = f'Total amount for {self.month}: {self.total_amount}$\n'
        for num, tenant in enumerate(self.list_of_tenants):
            tenant_data = {}
            if len(self.days_per_tenant) == len(self.list_of_tenants):
                tenant_data['days_of_stay'] = self.days_per_tenant[num]
            if len(self.payment_split) == len(self.list_of_tenants):
                tenant_data['percentage_of_bill'] = self.payment_split[num]
            if len(self.amounts_to_pay) == len(self.list_of_tenants):
                tenant_data['amount_to_pay'] = self.amounts_to_pay[num]
            data_representation += f'{tenant}: {tenant_data}\n'
        data_representation += '============================================'
        return data_representation
