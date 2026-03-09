
questions = {
                1:{
                    "question": "What is called as the 'Roof of the World'?",
                    "options": ["Indira Point", "Kanchenjunga", "Pamir Knot", "Indira Col"],
                    "answer": 2
                },
                2:{
                    "question": "What is the seventh planet from the sun?",
                    "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                    "answer": 2
                },
                3:{
                    "question": "Who directed the Lord of the Rings trilogy?",
                    "options": ["Peter Jackson", "Steven Spielberg", "James Cameron", "Martin Scorsese"],
                    "answer": 0
                },
                4:{
                    "question": "Who was Henry VIII's first wife?",
                    "options": ["Catherine of Aragon", "Anne Boleyn", "Jane Seymour", "Catherine Howard"],
                    "answer": 0
                },
                5:{
                    "question": "Which country has the bigger population, Scotland or Ireland?",
                    "options": ["Scotland", "Ireland", "Both have the same population", "Neither has a population"],
                    "answer": 0
                },
                6:{
                    "question": "In a website browser address bar, what does “www” stand for?",
                    "options": ["World Wide Web", "Web World Wide", "Wide World Web", "Web Wide World"],
                    "answer": 0
                }
            }

counter = 0
for key in questions:
    print(f"Q{key}: {questions[key]['question']}")
    for i, option in enumerate(questions[key]['options']):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == questions[key]['answer']:
        print("Correct!\n")
        counter = counter + 1
    else:
        print("Wrong!\n")

print(f"Your scored {counter} out of {len(questions)}")