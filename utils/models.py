from dataclasses import dataclass


@dataclass
class Answer:
    """Объект ответа (датакласс).

    Поля:
        `text` (str): Текст ответа
        `is_correct` (bool): Является ли правильным
    """
    text: str
    is_correct: bool


@dataclass
class Question:
    """Объект вопроса (датакласс).

    Поля:
        `text` (str): Текст вопроса
        `answers` (list[Answer]): Список экземлпяров ответов
    """
    text: str
    answers: list[Answer]

    @property
    def correct_answer(self) -> Answer:
        """Правильный ответ на вопрос"""
        for answer in self.answers:
            if answer.is_correct:
                return answer

    @property
    def correct_answer_index(self) -> int:
        """Индекс правильного ответа на вопрос"""
        return self.answers.index(self.correct_answer)

    def __str__(self) -> str:
        text = self.text + '\n\n'
        letters = ['а)', 'б)', 'в)', 'г)']
        index = 0

        for answer in self.answers:
            text += f"{letters[index]} {answer.text}\n"
            index += 1

        return text.rstrip()
