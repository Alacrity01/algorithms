# # # # insert 0 5
# # # # insert 1 10
# # # # insert 0 6
# # # # print
# # # # remove 6
# # # # append 9
# # # # append 1
# # # # sort
# # # # print
# # # # pop
# # # # reverse
# # # # print

# # # # # for i in range(10):
# # # # # 	print(i)


# # # # # # if __name__ == '__main__':
# # # # # #     n = int(input())
# # # # # command_list = []

# # # # # Consider a list (list = []). You can perform the following commands:
# # # # # list = []
# # # # # comm_1 = list.insert(i, e)	#insert i e: Insert integer  at position .
# # # # # comm_2 = print(list)	#print: Print the list.
# # # # # comm_3 = list.remove(e) #remove e: Delete the first occurrence of integer .
# # # # # comm_4 = list.append(e) #append e: Insert integer  at the end of the list.
# # # # # comm_5 = list.sort() #sort: Sort the list.
# # # # # comm_6 = list.pop()#pop: Pop the last element from the list.
# # # # # comm_7 = list.reverse()#reverse: Reverse the list.
# # # # # Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# # # # # list = []
# # # # # commands = []


# # # # # list = []
# # # # # comm_1 =
# # # # # comm_2 =
# # # # # comm_3 =
# # # # # comm_4 =
# # # # # comm_5 =
# # # # # comm_6 =
# # # # # comm_7 =
# # # # # Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# # # # def list_operations(n,e):
# # # # 	list = []
# # # # 	commands = [
# # # # 		list.insert(1, e),
# # # # 		print(list),
# # # # 		list.remove(e),
# # # # 		list.append(e),
# # # # 		list.sort(),
# # # # 		list.pop(),
# # # # 		list.reverse()
# # # # 	]

# # # 	# for i in range(1,n+1):
# # # 	# 	commands[i]

# # # # list = []
# # # # commands = []

# # # # list_operations(6,1)

# # # list = [] # initialize list
# # # # n = int(input()) # read first line, input n
# # # # i = 1
# # # # for i in range(len(n)):


# # # # e = 1

# # # j, e = 0, 5

# # # input_val = input()
# # list = []
# # input_val = "insert 0 5"
# # input = input_val.split(" ")

# # comm_1 = input[0]

# # if len(input) > 1:
# # 	comm_2 = int(input[1])

# # 	if len(input) > 2:
# # 		comm_3 = int(input[2])


# # commands = {
# # 	"insert": list.insert(comm_2,comm_3),
# # 	"print": print(list),
# # 	# "remove": list.remove(comm_2),
# # 	"append": list.append(comm_2),
# # 	"sort": list.sort(),
# # 	"pop": list.pop(),
# # 	"reverse": list.reverse()
# # }

# # def run_list_commands(inputs):
# # 	list = []
# # 	commands = {
# # 		"insert": list.insert(comm_2,comm_3),
# # 		"print": print(list),
# # 		"remove": list.remove(comm_2),
# # 		"append": list.append(comm_2),
# # 		"sort": list.sort(),
# # 		"pop": list.pop(),
# # 		"reverse": list.reverse()
# # 	}

# # 	def parse_input(input):
# # 		commands = {}
# # 		parsed_input = inputs[i].split(" ")
# # 		comm_1 = input[0]
# # 		commands["print"] =  print(list)
# # 		commands["sort"] = list.sort()
# # 		commands["pop"] = list.pop()
# # 		commands["reverse"] = list.reverse()

# # 		if len(parsed_input) > 1:
# # 			comm_2 = int(parsed_input[1])
# # 			commands["remove"] = list.remove(comm_2)
# # 			commands["append"] = list.append(comm_2)
# # 			if len(parsed_input) > 2:
# # 				comm_3 = int(parsed_input[2])
# # 				commands["insert"] = list.insert(comm_2,comm_3)
# # 		commands[comm_1]


# # 	# 	"insert": list.insert(comm_2,comm_3),
# # 	# 	"print": print(list),
# # 	# 	"remove": list.remove(comm_2),
# # 	# 	"append": list.append(comm_2),
# # 	# 	"sort": list.sort(),
# # 	# 	"pop": list.pop(),
# # 	# 	"reverse": list.reverse()
# # 	# }


# # 		if len(input) > 1:
# # 			comm_2 = int(input[1])
# # 			if len(input) > 2:

# # 				comm_3 = int(input[2])
# # 		commands[comm_1]


# # 	n = inputs[0]
# # 	list = []
# # 	for i in range(1,n):
# # 		input = inputs[i].split(" ")
# # 		comm_1 = input[0]
# # 		if len(input) > 1:
# # 			comm_2 = int(input[1])
# # 			if len(input) > 2:
# # 				comm_3 = int(input[2])
# # 		commands[comm_1]

# # # print(type(input))

# # # print(commands["insert"])

# # inputs = [
# # 	"12",
# # 	"insert 0 5",
# # 	"insert 1 10",
# # 	"insert 0 6",
# # 	"print",
# # 	"remove 6",
# # 	"append 9",
# # 	"append 1",
# # 	"sort",
# # 	"print",
# # 	"pop",
# # 	"reverse",
# # 	"print"
# # ]


# # run_list_commands(inputs)


# # # inputs = ["insert", "print"]
# # # commands[inputs[0]]
# # # commands[inputs[1]]


# def parse_input(inputs, list=[], count=0, n=0):
# 	if count == 0:
# 		n = int(input)
# 	count += 1

# 	if count == n:
# 		print(list)
# 		return list
# 	else:
# 		parsed_input = inputs[count].split(" ")
# 		comm_1 = parsed_input[0]

# 		if comm_1 == "pop":
# 			list.pop()
# 		elif comm_1 == "reverse":
# 			list.reverse()
# 		elif comm_1 == "print":
# 			print(list)
# 		elif comm_1 == "remove":
# 			comm_2 = int(parsed_input[1])
# 			list.remove(comm_2)
# 		# commands["pop"] = list.pop()
# 		elif comm_1 == "append":
# 			comm_2 = int(parsed_input[1])
# 			list.append(comm_2)
# 		elif comm_1 == "insert":
# 			comm_2 = int(parsed_input[1])
# 			comm_3 = int(parsed_input[2])
# 			list.insert(comm_2,comm_3)
# 		elif comm_1 == "sort":
# 			list = sorted(list)
# 		parse_input(inputs,list,count,n)

# list = []
# n = int(input())
# count = 0

# for count in range(n):
# 	comms = input().split(" ")
# 	count += 1
# 	if comms[0] == "pop":
# 		list = list.pop()
# 	elif comms[0] == "reverse":
# 		list = list.reverse()
# 	elif comms[0] == "print":
# 		print(list)
# 	elif comms[0] == "remove":
# 		list = list.remove(int(comms[1]))
# 	elif comms[0] == "append":
# 		list = list.append(int(comms[1]))
# 	elif comms[0] == "insert":
# 		list = list.insert(int(comms[1]),int(comms[2]))
# 	elif comms[0] == "sort":
# 		list = sorted(list)


# hackerrank_list_commands(n,comms[0])

# def hackerrank_list_commands(n,comms[0],count = 0):#,list=[],count=0):#,inputs, list=[], count=0):
# 	# if count == 0:
# 		# n = int(input)
# 	# count += 1
# 	if count == n:
# 		return list
# 	else:
# 		comms[0] == input()
# 		if comms[0] == "pop":
# 			list.pop()
# 		elif comms[0] == "reverse":
# 			list.reverse()
# 		elif comms[0] == "print":
# 			print(list)
# 		elif comms[0] == "remove":
# 			# comms[1] = int(parsed_input[1])
# 			comms[1] = int(input())
# 			list.remove(comms[1])

# 		elif comms[0] == "append":
# 			# comms[1] = int(parsed_input[1])
# 			comms[1] = input()
# 			list.append(comms[1])
# 		elif comms[0] == "insert":
# 			# comms[1] = int(parsed_input[1])
# 			# comm_3 = int(parsed_input[2])
# 			comms[1] = input()
# 			comm_3 = input()
# 			list.insert(comms[1],comm_3)
# 		elif comms[0] == "sort":
# 			list = sorted(list)
# 		return hackerrank_list_commands(inputs,list,count,n)
# 	# commands["reverse"] = list.reverse()


# comms[0] = input()

# inputs = [
# 	"12",
# 	"insert 0 5",
# 	"insert 1 10",
# 	"insert 0 6",
# 	"print",
# 	"remove 6",
# 	"append 9",
# 	"append 1",
# 	"sort",
# 	"print",
# 	"pop",
# 	"reverse",
# 	"print()"
# ]
# # list = []

# # for i in range(1,int(inputs[0])):
# # 	parse_input(inputs[i],list)

# # print(list)
# parse_input(inputs)


# n = 12
i = 0

arr = [
    "12",
    "insert 0 5",
    "insert 1 10",
    "insert 0 6",
    "print",
    "remove 6",
    "append 9",
    "append 1",
    "sort",
    "print",
    "pop",
    "reverse",
    "print"
]
n = int(arr[i])
list = []

for i in range(n):
    comms = arr[i].split(" ")
    # comms = input.split(" ")
    if comms[0] == "pop":
        list.pop()
    elif comms[0] == "reverse":
        list.sort(reverse=True)
    elif comms[0] == "print":
        print(list)
    elif comms[0] == "remove":
        list.remove(int(comms[1]))
    elif comms[0] == "append":
        list.append(int(comms[1]))
    elif comms[0] == "insert":
        list.insert(int(comms[1]), int(comms[2]))
    elif comms[0] == "sort":
        list.sort()

print(list)
