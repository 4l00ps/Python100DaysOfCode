print("Hello"[4])
print("Hello"[0:4])  # 0 is inclusive and 4 is exclusive
print("Hello"[:3])
print("Hello"[3:])  # 3 is inclusive

# integer
myInt = 19
# float
myfloat = 3.141592653589793
myfloat2 = 734_529.355
#the _ is used to make the number more readable
print(myfloat2)
#printing 3 numbers after decimal
print("{:.3f}".format(myfloat))
# printing 3 numbers after decimal
print(f"{myfloat:.3f}")
# printing 3 numbers after decimal



# List
myList = [1, 2, 3, 4, 5]
#dict
myDict = {
    "name": "Muhammad Ali",
    "age": 19,
    "isStudent": True
}

#type check
if type(myList) == list:
    print("myList is a list")
if type(myDict) == dict:
    print("myDict is a dict")

if type(myInt) == int:
    print(f"myInt is a {type(myInt)}")


#type conversion
myInt = 19
myInt = str(myInt)
print(f"int value is: {myInt}, type is: {type(myInt)})")
myInt = int(myInt)
print(f"int value is: {myInt}, type is: {type(myInt)})")
myInt = float(myInt)
print(f"int value is: {myInt}, type is: {type(myInt)})")
myInt = bool(myInt)
print(f"int value is: {myInt}, type is: {type(myInt)})")

int("42")        # 42
float("3.14")    # 3.14
str(123)         # "123"
list("abc")      # ['a', 'b', 'c']
tuple([1, 2, 3]) # (1, 2, 3)
set([1, 2, 2])   # {1, 2}
dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}

# implode and explode in  python
# implode is used to convert a list to a string
myList = [1, 2, 3, 4, 5]
myList = [str(i) for i in myList]
myList = ",".join(myList)
print(myList)
# explode is used to convert a string to a list
myList = myList.split(",")
print(myList)


#from -> to , allowed?, Example.

#str ->int, yes(if numeric), int("123") -> 123
#str -> float, yes(if numeric), float("3.14") -> 3.14
#float ->int, yes(truncates), int(3.14) -> 3
#float -> str, yes, str(3.14) -> "3.14"
#int -> str, yes, str(123) -> "123"
#int -> float, yes, float(123) -> 123.0
#list -> tuple, yes, tuple([1, 2, 3]) -> (1, 2, 3)
#list -> set , yes, set([1, 2, 2]) -> {1, 2}    (removes duplicates)
#bool -> int, yes, int(True) -> 1

for x in range(int(input("Enter a number: ")), 0, -2):
    print("even" if x % 2 == 0 else "odd")

