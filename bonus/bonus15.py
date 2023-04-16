import json

with open("../files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user choice"] = user_choice


score = 0


for index, question in enumerate(data):
    if question["user choice"] == question["correct answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{index + 1} {result} - Your answer is: {question['user choice']}, " \
              f"Correct answer is: {question['correct answer']}"
    print(message)

print(score, "/", len(data))
