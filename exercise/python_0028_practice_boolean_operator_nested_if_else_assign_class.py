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

# [Solution 1]
# elif math_score > 85 and average_score > 75 and math_score >= 70 and not science_score < 70 and english_score >= 70:
#     clas_name = 'Math Elite Class'
#
# elif science_score > 85 and average_score > 75 and math_score >= 70 and not science_score < 70 and english_score >= 70:
#     clas_name = 'Science Elite Class'
#
# elif english_score > 85 and average_score > 75 and math_score >= 70 and not science_score < 70 and english_score >= 70:
#     clas_name = 'English Elite Class'

# [Solution 2]
elif (math_score > 85 or science_score > 85 or english_score > 85) and average_score > 75 and math_score >= 70 and not science_score < 70 and english_score >= 70:
    if math_score > 85:
        class_name = 'Math Elite Class'
    elif science_score > 85:
        class_name = 'Science Elite Class'
    else:
        class_name = 'English Elite Class'

elif average_score > 75 and not math_score < 65 and science_score >= 65 and not english_score < 65:
    class_name = 'Express Class'

else:
    class_name = "Normal Class"

print(f"You are assigned to {class_name}")



