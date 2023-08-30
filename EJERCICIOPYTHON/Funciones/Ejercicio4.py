def invoice(amount, vat=21):
    return amount + amount+vat/100
print(invoice(1000,10))
print(invoice(1000))