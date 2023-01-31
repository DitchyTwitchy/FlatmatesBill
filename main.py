from classes import MonthlyBill


def bill_app():
    print(f'Please enter the month of the bill: ', end='')
    input_month = input()

    print(f'Please enter the total amount to be payed in {input_month}: ', end='')
    total_amount = float(input())

    list_of_tenants = ['John', 'Mary']
    print(f'-- The list of tenants is {list_of_tenants}')

    bill = MonthlyBill(input_month, total_amount, list_of_tenants)
    bill.get_days_of_stay()
    bill.process_bill()
    print(bill)


if __name__ == '__main__':
    bill_app()
