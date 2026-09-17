users = [
    {"name": "Ali", "age": 19, "skills": ["Python", "Git"]},
    {"name": "Reza", "age": 16, "skills": ["HTML", "CSS"]},
    {"name": "Amir", "age": 22, "skills": ["Python", "FastAPI"]},
    {"name": "Sara", "age": 25, "skills": ["Python", "SQL"]},
    {"name": "Nima", "age": 17, "skills": ["JavaScript"]},
]


all_skills = {
    skill
    for user in users
    for skill in user["skills"]
}
print(all_skills)