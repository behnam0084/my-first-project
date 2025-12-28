
def avg_num(grade):
    return sum(grade)/len(grade)
    

book = int(input("tedad dars  ra vared kon :"))

grades = []
for i in range(book):
    grade = int(input("nomarat : "))
    grades.append(grade)

avg = avg_num(grades)

if 20>avg>17:
    sta ="great"

elif 17>=avg >=12:
    sta = "ghabool"

else :
    sta = "mashroot"

print(f"avg = {avg}")
print( sta )