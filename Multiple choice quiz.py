from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Blue/Orange\n(c) Purple\n\n",
    "what color is the sky?\n(a) Black\n(b) Orange\n(c) Blue\n\n" 
]

question = [
    Question(question_prompts[0], "a")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct")

run_test(questions)