# #String: ordered, immutable, text representation
# my_string = "    Amit pratap singh"
#
# print("--------------------------------")
# print(my_string.split())
# print("################################")
# new_string = ' '.join(my_string)
# print(new_string)
# print("--------------------------------")
# print(my_string)
# print("--------------------------------")
# print(my_string.strip())
# print("--------------------------------")
# my_new_string = my_string[:: -1]
# print("--------------------------------")
# print(my_string.replace('singh', "Rajput"))
# print("--------------------------------")
# print(my_new_string)
# print("--------------------------------")
# print(my_string.find("s"))
# print("--------------------------------")
# for letter in my_string:
#     print(letter)

print("#####################################################")
# from timeit import default_timer as timer
#
# my_list = ['a'] * 1000000
#
# #bad coding
# start = timer()
# my_string_new = ''
# for i in my_list:
#     my_string_new += i
# stop = timer()
# print(stop-start)
#
# #good coding
#
# start = timer()
# my_string = ''.join(my_list)
# stop = timer()
# print(stop-start)


print("#####################################################")
#%, .format(), f-String
# var = "Amit"
# var1 = 28
# my_string = "the variable is %s" %var
# my_string1 = "the variable is %d" %var1
# print(my_string)
# print(my_string1)

var = 3.1234
my_string = "the variable is {:.2f}".format(var)
print(my_string)
my_string1 = f"the variable is {var}"
print(my_string1)
