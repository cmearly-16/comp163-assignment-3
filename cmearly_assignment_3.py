student_name = "Christopher Early"
current_gpa = 3.25
study_hours = 10
social_points = 50
stress_level = 20

print(f"Welcome to my game, {student_name}!")
print(f" ----- Your current stats are: ----- ")
print(f" Current GPA: {current_gpa:.2f}")
print(f" Student Hours: {study_hours}")
print(f" Social Points: {social_points}")
print(f" Stress Level: {stress_level}")
print(f"------------------------------------")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input()
if choice == "A":
    if current_gpa >= 2.5:
        print("You have chosen a light course load.")
        study_hours += 2
        stress_level += 10
    else:
        print("Your GPA is too low for a light load.")
elif choice == "B":
    if current_gpa >= 3.0:
        print("have chosen a standard load.")
        study_hours += 4
        stress_level += 15
    else:
        print("Your GPA is too low for a standard load.")
elif choice == "C":
    if current_gpa >= 3.5:
        print("You have chosen a heavy course load.")
        study_hours += 6
        stress_level += 25
    else:
        print("Your GPA is too low for a heavy load.")
else:
    print("Invalid choice. Defaulting to light load.")
    study_hours += 4
    stress_level += 15

print(f" ----- Stats after Decision 1 ----- ")
print(f" Current GPA: {current_gpa:.2f}")
print(f" Student Hours: {study_hours}")
print(f" Social Points: {social_points}")
print(f" Stress Level: {stress_level}")
print(f"------------------------------------")