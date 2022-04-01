from utils.models import Question, Answer
from random import shuffle


class TestManager:
    """Менеджер по работе с тестом.

    Аргументы:
        `question_list` (list): Список вопросов
        `test_theme` (str, optional): Тема теста. Стандартно - None.
        `shuffle` (bool, optional): Случайный порядок вопросов. Стандартно - False.
        `shuffle_answers` (bool, optional): Случайный порядок ответов. Стандартно - False.
    """

    def __init__(
            self,
            question_list: list,
            test_theme: str = None,
            shuffle: bool = False,
            shuffle_answers: bool = False) -> None:
        """Конструктор менеджера.

        Аргументы:
            `question_list` (list): Список вопросов
            `test_theme` (str, optional): Тема теста. Стандартно - None.
            `shuffle` (bool, optional): Случайный порядок вопросов. Стандартно - False.
            `shuffle_answers` (bool, optional): Случайный порядок ответов. Стандартно - False.
        """

        self.question_list = question_list
        self.questions = self.__parse_question_list(question_list)
        self.current_question = self.questions[0]
        self.theme = test_theme or 'PATRICIA-деревья'
        self.answered_questions: list[Question] = []
        self.answers_dict = {}
        self.failed_questions: list[Question] = []
        self.correct_questions: list[Question] = []

        if shuffle:
            self.__shuffle_questions()
        if shuffle_answers:
            self.__shuffle_answers()

    @property
    def answers(self):
        """Словарь вида `{question_index: answer_index}`"""
        return self.answers_dict

    @property
    def unanswered_questions(self) -> list[Question]:
        """Список неотвеченных вопросов.

        Возвращает:
            `list[Question]`: список экземпляров класса вопросов, 
            на которые ещё не приведён ответ. 
        """
        questions = self.questions.copy()
        for answered_question in self.answered_questions:
            if answered_question in questions:
                questions.pop(questions.index(answered_question))

        return questions

    @property
    def is_completed(self):
        """Является ли тест завершённым (все вопросы имеют ответы)"""
        return len(self.answered_questions) == len(self.questions)

    @property
    def current_question_index(self):
        """Индекс текущего вопроса"""
        return self.questions.index(self.current_question)

    def check_answer(self, answer_index: int):
        """Обратный колбек кнопки с ответом.

        Аргументы:
            `answer_index` (int): Индекс кнопки с ответом

        Returns:
            (bool): Правильный ли ответ 
        """
        self.answered_questions.append(self.current_question)
        self.answers_dict.update({self.current_question_index: answer_index})
        if answer_index == self.current_question.correct_answer_index:
            self.correct_questions.append(self.current_question)
            return True
        else:
            self.failed_questions.append(self.current_question)
            return False

    def __parse_question_list(self, question_list: list) -> list[Question]:
        """Принимает список вопросов с определённым синтаксисом (в конце docstring'а).

        Аргументы:
            `question_list` (list): _description_

        Возвращает:
            `list[Question]`: Список экземпляров модели вопроса

        Синтаксис списка вопросов:
        ```
        [
            { # Тело вопроса №1
                "text": 'Текст вопроса №1',
                "answers": [ # Список ответов вопроса №1
                    { # Тело ответа №1
                        "text": 'Текст правильного ответа 4',
                        "is_correct": True
                    },
                    { # Тело ответа №2
                        "text": 'Текст ответа 4',
                        "is_correct": False
                    },
                    { # Тело ответа №3
                        "text": 'Текст ответа 4',
                        "is_correct": False
                    },
                    { # Тело ответа №4
                        "text": 'Текст ответа 4',
                        "is_correct": False
                    }
                ]
            }, ...
        ]

        ```
        """
        questions: list[Question] = []
        for question in question_list:
            text: str = question.get('text')
            answer_list: list[dict] = question.get('answers')
            answers: list[Answer] = []

            for answer in answer_list:
                answers.append(Answer(**answer))

            questions.append(Question(text, answers))

        return questions

    def __shuffle_questions(self):
        """Перемешивание списка вопросов"""
        shuffle(self.questions)

    def __shuffle_answers(self):
        """Перемешивание ответов на все вопросы"""
        for question in self.questions:
            shuffle(question.answers)

    def select_question(self, question: Question = None, question_index: int = None):
        """Выбор текущего вопроса.

        Аргументы:
            `question` (Question, optional): Экземпляр класса вопроса для выбора.
            `question_index` (int, optional): Индекс вопроса для выбора.
        """
        if question:
            self.current_question = question
        elif question_index:
            self.current_question = self.questions[question_index]
