# Bug count: ? (find them all)
# Topic: list/dict/set comprehensions, conditional comprehensions
# Give after: L05
#
# Scenario: A student grade processing system for a university.
#
# Expected output:
#   Passing students: ['Aziz', 'Barno', 'Kamola', 'Nilufar']
#   Failing students: ['Jasur', 'Malika']
#   Grade map: {'Aziz': 'B', 'Barno': 'A', 'Jasur': 'F', 'Kamola': 'A', 'Malika': 'F', 'Nilufar': 'B'}
#   Unique grades awarded: {'A', 'B', 'F'}
#   Scores above 70 doubled: [172, 180, 154, 160]

students = {
    "Aziz": 86,
    "Barno": 90,
    "Jasur": 45,
    "Kamola": 92,
    "Malika": 38,
    "Nilufar": 77,
}

# List of students who passed (score >= 60)
passing = [name for name, score in students.items() if score >= 60]
print("Passing students:", sorted(passing))

# List of failing students
failing = [name for name in students if students[name] < 60]
print("Failing students:", sorted(failing))

# Dict mapping name → letter grade
def get_grade(score):
    if score >= 90: return "A"
    elif score >= 75: return "B"
    elif score >= 60: return "C"
    else: return "F"

grade_map = {name: get_grade[score] for name, score in students.items()}  # BUG
print("Grade map:", grade_map)

# Set of unique grades
unique_grades = {grade for grade in grade_map.items()}  # BUG — .items() gives (key,value) tuples
print("Unique grades awarded:", unique_grades)

# Double all scores that are above 70
doubled = [score * 2 for score in students if students[score] > 70]  # BUG
print("Scores above 70 doubled:", doubled)

