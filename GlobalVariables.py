x = "British"
X = "British"

def myfunc():
  print("Being", x, "is a crime")

myfunc()

def myfunc():
  global f
  f = "American"
myfunc()

print("Being", f, "is a crime")

def myfunc():
  X = "Polish"
  print("Being", X, "is a crime")
myfunc()