txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = [get_price_with_tax(txn) for txn in txns]
print(final_prices)

"""
The only distinction between this implementation and map() is that the list comprehension in Python returns a list, not a map object.
"""
