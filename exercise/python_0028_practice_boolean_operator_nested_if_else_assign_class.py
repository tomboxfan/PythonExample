# We have some students, based on their math / science / english score, we will assign them to the following classes
# Elite Class - all 3 subjects should have score higher than 85
# Math Elite Class - Math score higher than 85 and 3 subjects average higher than 75 and no suject lower than 70
# Science Elite Class - Science score higher than 85 and 3 subjects average higher than 75 and no suject lower than 70
# English Elite Class - English score higher than 85 and 3 subjects average higher than 75 and no suject lower than 70
# Express Class - average higher than 75 and no subject lower than 65
# Normal Class - other students

math_score = float(input("Math score: "))
science_score = float(input("Science score: "))
english_score = float(input("English score: "))

# Step 1) calculate average score -----------------------------------------------
average_score = (math_score + science_score + english_score) / 3
print(f'Your score is: {math_score}, {science_score}, {english_score}. Average score: {average_score:.2f}')

# Step 2) Check eligibility for Elite Class
if math_score > 85 and science_score > 85 and english_score > 85:
    class_name = 'Elite Class'
else:
    class_name = "Normal Class"

print(f"You are assigned to {class_name}")



