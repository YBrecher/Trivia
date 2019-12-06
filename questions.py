class Questions:
    def __init__(self, question, option1, option2, option3, option4, answer):
        self.__question = question
        self.__option1 = option1
        self.__option2 = option2
        self.__option3 = option3
        self.__option4 = option4
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_op1(self, option1):
        self.__option1 = option1

    def set_op2(self, option2):
        self.__option2 = option2

    def set_op3(self, option3):
        self.__option3 = option3

    def set_op4(self, option4):
        self.__option4 = option4

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_op1(self):
        return self.__option1

    def get_op2(self):
        return self.__option2

    def get_op3(self):
        return self.__option3

    def get_op4(self):
        return self.__option4

    def get_answer(self):
        return self.__answer
