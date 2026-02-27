a = 200
b = 33
x = "Hello"
y = 15
z = 200

print(10 > 9)
print(10 == 9)
print (10 < 9)

if b> a:
    print("b is greater then a")
else:
    print("b is not greater than a")


print(bool("Hello"))
print(bool(15))


print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True
print(myFunction())

if myFunction():
  print("YES!")
else:
  print("NO!")

print(isinstance(z, int))