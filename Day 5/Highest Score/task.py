student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#Use Python's built in sum() function
total_exam_scores = sum(student_scores)
print(total_exam_scores)

#Look at how the sum function works by using a loop
sum_of_scores = 0
for score in student_scores:
    sum_of_scores += score

print(sum_of_scores)

#Find the max and min of a list using loops
list_of_numbers = [2, 4, 5, 8, 10, 12, 45, 36, 1, 62]
lowest = list_of_numbers[0]
highest = list_of_numbers[0]
for number in list_of_numbers:
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number

print(highest)
print(lowest)

#Find the max and min of the scores
lowest_score = student_scores[0]
highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

print(f"The lowest score is {lowest_score}")
print(f"The highest score is {highest_score}")
