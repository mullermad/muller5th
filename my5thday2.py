score=input("enter the scores of the student\n").split()

for i in range(0,len(score)):
    score[i] = int(score[i])
print(score)

max=score[0]
for n in score:
    if score[i]>max:
        max=score[i]

print(f"the heighest score is {max}")
total=0
for i in range(1,101):
    total += i
print(f"the sum is {total}")

