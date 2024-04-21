# try:
#     with open("a_file.txt") as file:
#         file.read()
# except FileNotFoundError as err_message:
#     print(f"There was an err: {err_message}")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldnt be over 3m")

bmi = weight / height ** 2
print(f"BMI: {bmi}")