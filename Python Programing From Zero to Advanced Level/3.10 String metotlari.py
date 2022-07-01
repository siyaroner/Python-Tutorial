text="      Hello There, I'm Şiyar 7"
a=text.strip()
print(a)
r="Wooeah!".strip("Woe")
print(r)
print("  Wooah!    ".strip())
print("  Woah!".rstrip())
print("  Woah!   ".lstrip())
print(a.split())
print("-".join(a))
print(a.find("Şiyar")) # if we type something that is not in string then it will return -1 which meaning False
print(a.rfind("Şiyar")) # if we type something that is not in string then it will return -1 which meaning False
print(a.index("Hello"))
print(a.startswith("H")) # it's retrun True or False
print(a.endswith("H")) # it's retrun True or False
print(a.replace("There,","There!"))
print(a.replace("Ş","S"))
print(a.center(50,"#"))
print(a.count("e"))
print(a.count("e",5,20))
print(a.isalpha())
print("233".isdigit())
print("what".rjust(30,"*"))