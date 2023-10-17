# hackerrank challenge 
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__': 
    list = []
    n = int(input())
    count = 1

    for count in range(n):
		
        comms = input().split(" ")
        count += 1
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
            list.insert(int(comms[1]),int(comms[2]))
        elif comms[0] == "sort":
            list.sort()