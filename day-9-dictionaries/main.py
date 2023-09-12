# {Key: Value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}

# Edit and item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Execeeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"

print(student_grades)


# Nesting Dictionaries in Lists
#######################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]


def add_new_country(key1, key2, list):
    new_country = {}
    new_country["country"] = key1
    new_country["total_visited"] = key2
    new_country["cities_visited"] = list
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
