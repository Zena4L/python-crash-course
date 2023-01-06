print("----- List -----")
courses = ['calcus','algebra','oop']
print(courses[0])
print(courses[1])
print(courses[2])

print("Guess my fav course is not part")
courses.append('c++')
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])

print("Let's modify it a bit")
courses.insert(0,'python')
print('How about we remove something?')
courses.pop(2)
courses.insert(2,'c')
print(courses)
