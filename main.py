#task_1
lst = [1, 2, 3, "a", "b", 4]
lst2 = []

def str(msv, msv2):
	for num in msv:
		if type(num) == int:
			lst2.append(num)
	print(msv2)

str(msv=lst, msv2=lst2)




#task_2
num = [5, 4, 3, 2, 1]
num2 = []

def solve(num, num2):
	for x in num:
		m = num.index(x)
		n = x + m
		num2.append(n)
	print(num2)


solve(num, num2)





#task_3
num = int(input("son kriting :"))
massiv = [7, 4, 17, 14, 12, 3]
massiv2 = []


def percent(num, massiv, massiv2):
	m = len(massiv)
	for x in massiv:
		if x > num or x == num:
			massiv2.append(x)
			v = len(massiv2)
			s = (v*100/m)
			print(s)


percent(num, massiv, massiv2)




#task_4

num = [1, 2, 3, 4, 5, 6]
num2 = int(input("son kriting: "))

def task_4(num, num2):
	del num[0]
	num.append(num2)
	print(num)


task_4(num, num2)




#task_5
get_budget = {
	'odam1': {'ism': 'John', 'byudjet': 5000},
	'odam2': {'ism': 'Jane', 'byudjet': 7000},
	'odam3': {'ism': 'Bob', 'byudjet': 6000}
}


def get_budget(get_budget):
	yigindi = 0
	for odam in get_budget.values():
		yigindi += odam.get('byudjet', 0)

	print(f"Odamalar byudjetlarining yig'indisi: {yigindi}")

get_budget(get_budget)




#task_6
a = [1, 1]
b = []

def task_6(a, b):
	clon = a.copy()
	b.append(a)
	b.append(clon)
	print(b)


task_6(a, b)




#task_7
lst = [1, 2, 3, 5, 53, "Hello world", "hello", "12321", 1, 2, 3.1]
lst2 = []

def task_7(lst, lst2):
	for num in lst:
		if type(num) == float:
			lst.remove(num)

		if type(num) == int:
			lst2.append(num)
	print(lst2)

task_7(lst, lst2)




#Task_8
users = ["dvdfvdfvdfs", "dsfvwfvsdfv", "dfcdsfcdf"]

def chatroom_status(users):
	if not users:
		return 'no one online'
	elif len(users) == 1:
		return users[0]+' online'
	elif (len(users) == 2):
		return users[0]+' and '+users[1]+' online'
	else:
		return users[0]+', '+users[1]+' and '+str(len(users)-2)+' more online'


print(chatroom_status(users))




#Task_9
x = int(input("enter first_parametr :"))
y = int(input("enter second_parametr :"))
n = int(input("enter third_parametr :"))
list = []

def find_divisible_num(first,second,third,lst):
    for numbers in range(first,second + 1):
        if numbers % third == 0:
            lst.append(numbers)
    return lst
print(find_divisible_num(x,y,n,list))





#Task_10
lst = [1, 2]
lst2 = [5, 1]

def comparison(msv, msv2):
    for x in msv:
        if x in msv2:
            print(True)
            break
        else:
            print(False)


comparison(msv=lst, msv2=lst2)






