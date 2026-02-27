a = "Hello, World!"
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
c = "Hello, World!"
d = "Hello, World!"
e = "Hello"
f = "World"
g = e + " " +f
txt = "The best things in life are free!"
age = 36
price = 59
txt2 = f"My name is John, I am {age}"
txt3 = f"The price is {price:.2f} dollars"
txt4 = f"The Price is {20 * 59}"
txt5 = "We are the so-called \"Vikings\" from the north."


print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print(a)
print(b)
print(a[1])

for a in "Hello":
 print(a)

print(len(b))


print("free" in txt)

if "free" in txt:
 print("Yes, 'free' is present.")

 print("expensive" not in txt)

 if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

  print("Start of Slicing Strings")

  
  print(c[:5])
  print(c[2:])
  print(c[-5:-2])

print("Start of Modify Strings")
print(d.upper())
print(d.lower())
print(d.strip())
print(d.replace("H", "J"))
print(d.split(","))


print("Start of Concatenate Strings")
print(g)

print("Start of Format Strings")
print(txt2)
print(txt3)
print(txt4)

print("Start of Escape Characters")
print(txt5)