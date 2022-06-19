print("############################")
age = int(input("enter your age in year\n"))
#assume u are live on this fucking earth for 90 years
year_left=90-age
day = int(year_left * 365)
week = int(year_left * 52)
month = int(year_left * 12)
message = f"the number of day left is  ,{day} days ,and the number of week left is  ,{week}, weeks and the number of month left is  ,{month} months"
print(message)