available_lst = []
required_lst = []
free_lst = []
number_of_process = int(input("Enter the number of process: "))
number_of_resources = int(input("Enter the number of resource: "))
count = 1
for i in range(number_of_process):
    available_lst.append(list(map(int, list(input("Enter available: ").split()))) + [count])
    count += 1
for i in range(number_of_process):
    required_lst.append(list(map(int, list(input("Enter required: ").split()))))
free_lst = list(map(int, list(input("Enter free: ").split())))

needed_lst = []
step = []
for i, lst in enumerate(required_lst):
    process = []
    for ii, n in enumerate(lst):
        process.append(n - available_lst[i][ii])
    needed_lst.append(process)

print(needed_lst)

answer = True
while answer:
    for y, lst in enumerate(needed_lst):
        can = True
        possible = False
        for i, n in enumerate(lst):
            if n > free_lst[i] and can is True:
                can = False
            # print(can)
            if can is True and i == len(lst) - 1:
                possible = True
                step.append(available_lst[y][-1])
                needed_lst.pop(y)
            # print(possible)
            if possible is True:
                for ii, x in enumerate(lst):
                    free_lst[ii] += available_lst[y][ii]
                available_lst.pop(y)
    if len(needed_lst) == 0:
        answer = False
print("Step:", step)

