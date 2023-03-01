"""A program to calculate the final grade for Econ 410.""" 

recitation_grade: float = 1.0
poll_grade: float = 1.0
homework_grade: float = 0.90
higher_grade: float = 0.95
lower_grade: float = 0.0
final_grade: float = 0.0

# track 1
recitation_weight: float = 2.0
poll_weight: float = 5.0
homework_weight: float = 20.0
higher_weight: float = 25.0
lower_weight: float = 15.0
final_weight: float = 33.0

x: float = (recitation_weight * recitation_grade) + (poll_weight * poll_grade) + (homework_weight * homework_grade) + (lower_weight * lower_grade) + (higher_weight * higher_grade) + (final_weight * final_grade)
print(x)

# track 2
recitation_weight = 0.0
poll_weight = 0.0
homework_weight = 20.0
higher_weight = 27.0
lower_weight = 17.0
final_weight = 36.0

x = (recitation_weight * recitation_grade) + (poll_weight * poll_grade) + (homework_weight * homework_grade) + (lower_weight * lower_grade) + (higher_weight * higher_grade) + (final_weight * final_grade)
print(x)