file_name = "techcrunch.csv"

# lines = (line for line in open(file_name))
# print(lines)
# list_line = (s.rstrip().split(",") for s in lines)

file_name = "techcrunch.csv"

lines = (line for line in open(file_name))

list_line = (s.rstrip().split(",") for s in lines)

cols = next(list_line)
