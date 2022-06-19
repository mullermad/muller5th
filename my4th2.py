row1 = ["xxx","yyy","zzz"]
row2 = ["mmm","kkk","lll"]
row3 = ["aaa","bbb","ccc"]
final_row = [row1 , row2 , row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("enter position to display\n")
hor = int(position[0])
ver = int(position[1])
x = final_row[hor-1]
x[ver-1]="muller"
print(f"{row1}\n{row2}\n{row3}\n")

