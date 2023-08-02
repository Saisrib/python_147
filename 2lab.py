#1
a=[2,3,4,5,7,9,3]

newlist=[x for x in a if x%3==0]
print(newlist)

newlist=[x**2 for x in a if x%2==0]
print(newlist)

newlist=[x for x in a if x%2==0]
print(sum(newlist))

print(set(a))
#2
employees={"ravi":"2 april 1998","ram":"2 may 2000","sai":"2 march 1999"}
def birthDay(value):
    return employees.get(value,"employee not found")
print(birthDay("ram"))