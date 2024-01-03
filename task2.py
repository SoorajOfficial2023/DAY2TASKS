data = [
    {
        "name": "Alice",
        "courses": [
            {"course_name": "Math", "grade": 95},
            {"course_name": "Science", "grade": 88},
            {"course_name": "History", "grade": 92},
        ],
    },
    {
        "name": "Bob",
        "courses": [
            {"course_name": "Math", "grade": 90},
            {"course_name": "Science", "grade": 76},
            {"course_name": "History", "grade": 85},
        ],
    },
    {
        "name": "Charlie",
        "courses": [
            {"course_name": "Math", "grade": 78},
            {"course_name": "Science", "grade": 92},
            {"course_name": "History", "grade": 88},
        ],
    },
]
average_grade = []
for i in data:
    grades = [x["grade"] for x in i["courses"]]
    average_grades = sum(grades) / len(grades)
    average_grade.append(average_grades)
    print(f"{i['name']}: {average_grades}")
    
print(max(average_grade))

