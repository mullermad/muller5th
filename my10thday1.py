def format_name(f_name,l_name):
   first=f_name.title()
   last=l_name.title()
   return f"{first} {last}"

print(format_name(input("what is tour first name?" ),input("what is your last name? ")))