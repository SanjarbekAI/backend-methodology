# Bug count: ? (find them all)
# Topic: lists, list methods, list slicing, tuples
# Give after: L10
#
# Scenario: A school system managing a student waitlist for a popular course.
# Expected output:
#   Waitlist: ['Aziz', 'Barno', 'Jasur', 'Kamola', 'Malika']
#   First 3 students: ['Aziz', 'Barno', 'Jasur']
#   Last enrolled: Malika
#   After removing Jasur: ['Aziz', 'Barno', 'Kamola', 'Malika']
#   Total on waitlist: 4
#   Sorted: ['Aziz', 'Barno', 'Kamola', 'Malika']
#   Course info: ('Python Basics', 'Dr. Yusupov', 30)
#   Max seats: 30

waitlist = ["Aziz", "Barno", "Jasur", "Kamola"]
waitlist.append["Malika"]  # BUG

print("Waitlist:", waitlist)
print("First 3 students:", waitlist[0:3])
print("Last enrolled:", waitlist[-1])

waitlist.remove("Jasur")
print("After removing Jasur:", waitlist)
print("Total on waitlist:", len[waitlist])  # BUG

waitlist.sort()
print("Sorted:", waitlist)

course_info = ("Python Basics", "Dr. Yusupov", 30)
course_info[2] = 35  # BUG  (think about what type this is)
print("Course info:", course_info)
print("Max seats:", course_info[2])

