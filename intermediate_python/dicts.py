# Dictionary: key-value pairs, Unordered, Mutuble
mydict = {"name": "Amit", "age": 28, "city": "chhapra"}
print(mydict)
mydict["email"] = "amitoct9@gmail.com"
print(mydict)

#key   mydict.keys() or value    mydict.values()
for key, value in mydict.items():
    print(key, value)
mydict1 = dict(name="Amit", age= 28, city="chhapra")
print(mydict1)
