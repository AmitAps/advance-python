"""
map() provides an alternative approach that’s based in functional programming.
 You pass in a function and an iterable, and map() will create an object. This object contains
 the output you would get from running each iterable element through the supplied function.
"""
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = map(get_price_with_tax, txns)
print(list(final_prices))
