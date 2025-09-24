student_name = "Christopher Early"
current_gpa = 3.25
study_hours = input()
social_points = input()
stress_level = input()
print(f"Welcome to my game, {student_name}!")
print("")
print(f" ----- Your current stats are: ----- ")
print(f" Current GPA: {current_gpa}")
print(f" Student Hours: {study_hours}")
print(f" Social Points: {social_points}")
print(f" Stress Level: {stress_level}")
print(f"------------------------------------")
print("")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = "B"
if choice == "A":
    if current_gpa >= 2.5:
        print("You can take a light load.")
        study_hours += "2"
        stress_level += "10"
    else:
        print("Your GPA is too low for a light load.")
elif choice == "B":
    if current_gpa >= 3.0:
        print("You can take a standard load.")
        study_hours += "4"
        stress_level += "15"
    else:
        print("Your GPA is too low for a standard load.")
elif choice == "C":
    if current_gpa >= 3.5:
        print("You can take a heavy load.")
        study_hours += "6"
        stress_level += "25"
    else:
        print("Your GPA is too low for a heavy load.")
else:
    print("Please enter A, B, or C.")
print(f" ----- Your current stats are: ----- ")
print(f" Current GPA: {current_gpa}")
print(f" Student Hours: {study_hours}")
print(f" Social Points: {social_points}")
print(f" Stress Level: {stress_level}")
print(f"------------------------------------")
