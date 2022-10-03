"""list order of objects"""
cars=["honda","bmw","mercedes"]
cars=[0(-3),1(-2),2(-1)]
print(cars[1:]) >>> #"bmw","mercedece" 

"""list functions"""
cars=["bmw","mercedes","honda","ferrari"]
speed=[10,15,20,100,300]
cars.extend(speed)
print(cars)>>> #['bmw', 'mercedes', 'honda', 'ferrari', 10, 15, 20, 100, 300]

cars.append("kia")
print(cars)>>> #['bmw', 'mercedes', 'honda', 'ferrari', 'kia']

cars.insert(2,"kia")
print(cars)>>> #['bmw', 'mercedes', 'kia', 'honda', 'ferrari']

cars[0]="bently"
print(cars)>>> #['bently', 'mercedes', 'honda', 'ferrari']

cars.remove("bmw")
print(cars)>>> #['mercedes', 'honda', 'ferrari']

cars.clear()
print(cars)>>> #[]

cars.pop()
print(cars)>> #["bmw","mercedes","honda"]

del(cars[0])
print(cars)>>> #['mercedes', 'honda', 'ferrari']

b_index=cars.index("bmw")
print(b_index)>>> #0

counting = cars.count("bmw")
print(counting)>>> #1

cars.sort()
print(cars)>>> #['bmw', 'ferrari', 'honda', 'mercedes']

cars2=sorted(cars)
print(cars2)>>> #['bmw', 'ferrari', 'honda', 'mercedes']
print(cars)>>> #['bmw', 'mercedes', 'honda', 'ferrari']
#sorted doesn't change the original list order in the opposite to sort
speed.reverse()
print(speed)>>> #[300, 100, 20, 15, 10]

cars2=cars.copy()
print(cars2)>>> #['bmw', 'mercedes', 'honda', 'ferrari']
"""list comprehension"""
c={"a":20,"c":10,"b":30}
print(sorted([(k,v) for k,v in c.items()]))>>> #[('a', 20), ('b', 30), ('c', 10)]
print(sorted([(v,k) for k,v in c.items()]))>>> #[(10, 'c'), (20, 'a'), (30, 'b')]


"""string functions"""
fruit=" banana "
pos=fruit.find("na")>>> #2

pos=fruit.upper()>>> #BANANA

pos=fruit.replace("na","mo")>>> #bamomo

pos=fruit.lstrip()>>> #"banana " 

pos=fruit.rstrip()>>> #" banana"

pos=fruit.strip()>>> #"banana"

fruit.startswith()

"""dictionary"""
jjj={"chuck":1,"fred":42,"jan":100}

values=jjj.values()>>> #[1,42,100]

keys=jjj.keys()>>> #["chuck","fred","jan"]

items=jjj.items()>>> #[("chuck",1),("fred",42),("jan",100)]

jjj={"chuck":1,"fred":42,"jan":100}
for i,j in jjj.items():
    print(i,j)>>> #chuck 1
                    fred 42
                    jan 100

d=dict()
d["chev"]=5
d["sam"]=6
for k,v in d.items():
    print(k,v)>>> #chev 5
                    sam 6

d={"a":10,"b":11, "C":12}
d_new=sorted(d.items()) #sorted takes a list and here it takes a tuple of list(d.items())
for k,v in d_new:
    print(k,v)>>> #C 12
                    a 10
                    b 11                    

week={    "sat":"saturday",
    "sun":"sunday"
}
print(week["sat"])>>> #"saturday"
print(week.get("Sun","Try Again"))>>> #Try Again
#idiom for using get with 0 defult if python didn't find the data requested
counts=dict()
names=["csev","cwen","zqian","cwen"]
for name in names:
    #the KEY=the Value
    counts[name]=counts.get(name,0)+1
    print(counts)

counts=dict()
line=input("Enter words: ")
words=line.split()
for word in words:
    counts[word]=counts.get(word,0)+1
print(f"Counts: {counts}")>>> #Counts: {'the': 2, 'small': 1, 'one': 2, 'beat': 1, 'bigger': 1}

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()
  
!
"""fuctions"""


def nour(name, position):
    print(f"hello {name}, and you'r positon is {position}")
nour("mostafa","programmer")>>> #hello mostafa, and you'r positon is programmer

def cube(num):
    return num*num*num #python don't work for any order after return
print(cube(3))

def days_to_units(num_of_days):
    calculation_to_units=24
    while True:
        try:
            num_of_days=int(input("what is the number of days? "))
            if (num_of_days)>0:
                print(f"{num_of_days} days are {num_of_days*calculation_to_units} hours \nall good")
            elif(num_of_days)<0:
                print("Error!")    
            else:
                print("Error!")
        
        except ValueError: # we can stop using (ValueError) and leave it black to catch any error
            print("Error!")
     
    days_to_units("num_of_days")

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days = user_input.split(", ")
    for num_of_days_element in set(list_of_days):
        validate_and_execute()

"""if statment"""
def max(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3
print(max(3,8,10))>>> #10

largest_so_far=0
for num in [9,41,12,3,74,15]:
    if num>largest_so_far:
        largest_so_far=num
print(largest_so_far)

def calculator(num1,operator,num2):
    num1=float(input("Enter Ther First Number: "))
    operator=input("What's The Operator: ")
    num2=float(input("what is the second number: "))
    if (operator== "+"):
        print(num1+num2)
    elif (operator == "-"):
        print(num1-num2)
    elif (operator == "/"):
        print(num1/num2)
    elif (operator == "*"):
        print(num1 *num2)
    else:
        print("THE OPERATOR IS NOT RIGHT!")
calculator('num1', 'operator','num2')

num=[]
while True:
    inp=input("Enter the number: ")
    if inp=="done":
        break
    else:
        num.append(float(inp))

average=sum(num)/len(num)
print(f"the Average is {average}")


"""for loop"""

cars=["honda","merceds","bmw"]
for i,f in enumerate(cars):
    print(i,f)>>> #0 honda
                    1 merceds
                    2 bmw

for num in range(len(cars)):
    print(cars[num])>>> #honda
                        merceds
                        bmw


"""while loop"""

i=1
while i <10:
    print("too little")
    i+=1
if (i >10) and (i== 10):
    print("too much")
else:
    print(f"i is {i} and it's good")

#creating password with 3 trials

pass_word="mostafa"
word=input("what is the pass_word? ")
count=0
out=False
while (word!= pass_word) and (out==False):
    if count <2:
        word=input("Error, Enter Another Word: ")
        count+=1
    else:
        out=True

if out==True:
    print("out of trials!")
else:
    print("correct!")

"""open file with context manger"""

with open("documentations/new.txt","r") as file1:
    file2=file1.read()
print(file2)

with open("documentations/new.txt","r") as file1:
    file2=file1.readlines()
print(file2) >>> #['i come.. \n', 'i see..\n', 'i conquer.']

# for bigger files we use loop to control the size of the memory
with open("documentations/new.txt","r") as file1:
    for line in file1:
        print(line, end="")>>> #i come.. 
                                i see..
                                i conquer.

with open ("documentations/new.txt","r") as rf:
    with open("copy_text.txt", "w") as wf:
        for line in rf:
            wf.write(line)

