import questions
q_list = ['q1', 'q2', 'q3', 'q4', 'q5','q6', 'q7', 'q8', 'q9', 'q10']


def main():
    file_to_list()
    play_game()


def file_to_list():
    f = open('trivia.txt', 'r')

    for i in range(10):
        q_list[i] = questions.Questions(0, 0, 0, 0, 0, 0)
        q_list[i].get_question = f.readline()
        q_list[i].get_op1 = f.readline()
        q_list[i].get_op2 = f.readline()
        q_list[i].get_op3 = f.readline()
        q_list[i].get_op4 = f.readline()
        q_list[i].get_answer = f.readline()

    f.close()


def play_game():
    score1 = 0
    score2 = 0
    for i in range(10):
        print(q_list[i].get_question, end='')
        print(q_list[i].get_op1, end='')
        print(q_list[i].get_op2, end='')
        print(q_list[i].get_op3, end='')
        print(q_list[i].get_op4, end='')
        player1_answer = int(input("Player 1 enter your answer(1,2,3,or 4): "))
        player2_answer = int(input("Player 2 enter your answer(1,2,3,or 4): "))
        if player1_answer == int(q_list[i].get_answer):
            score1 += 1
        if player2_answer == int(q_list[i].get_answer):
            score2 += 1
        print("Player 1's score is ", score1, "out of ", i + 1)
        print("Player 2's score is ", score2, "out of ", i + 1)
    print("Player 1's final score is ", score1, "out of 10")
    print("Player 2's final score is ", score2, "out of 10")
    if score1 == score2:
        print("It's a tie.")
    elif score1 > score2:
        print("Player 1 wins")
    else:
        print("Player 2 wins")


main()
