#Dados Ficticio E-commerce
import csv
import random
from datetime import datetime, timedelta

products = ['T-shirt', 'Pants', 'Shoes', 'Hat', 'Socks', 'Book', 'Laptop', 'Headphone', 'backpack', 'Mouse']
categories = {
    'T-shirt': 'Clothing',
    'Pants': 'Clothing',
    'Shoes': 'Clothing',
    'Hat': 'Clothing', 
    'Socks': 'Clothing',
    'Book': 'Books',
    'Laptop': 'Electronics',
    'Headphone': 'Electronics',
    'backpack': 'Accessories',
    'Mouse': 'Electronics'

}
sellers = ['Ana', 'Pedro', 'Maria', 'Joao', 'Jose', 'Mariana', 'Carlos', 'Julia', 'Lucas', 'Larissa']
payment_methods = ['Credit Card', 'Debit Card', 'Boleto', 'Paypal', 'Pix', 'Transfer']

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

with open('ecommerce_sales.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Sale ID', 'Date', 'Product', 'Category', 'Quantity', 'Price_Unitary', 'Total', 'Seller', 'Payment Method'])

    for i in range(1, 1001):
        date_sale = random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime('%Y-%m-%d')
        product = random.choice(products)
        category = categories[product]
        quantity = random.randint(1, 100)
        price_unitary = round(random.uniform(10, 580), 2)
        total = round(quantity * price_unitary, 2)
        seller = random.choice(sellers)
        payment_method = random.choice(payment_methods)

        writer.writerow([i, date_sale, product, category, quantity, price_unitary, total, seller, payment_method])