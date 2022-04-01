import os
from functools import partial
from random import choice
from sys import argv

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from ui import main, theory
from utils.models import Question, Answer
from utils.questions import questions
from utils.test_manager import TestManager


class TestApp(QMainWindow, main.Ui_MainWindow):
    """Главный класс приложения-теста"""

    def __init__(self):
        """Метод инициализации интерфейса"""
        super().__init__()
        QFontDatabase.addApplicationFont('fonts/circe.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-bold.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-extrabold.ttf')
        self.setupUi(self)

        # Создание менеджера работы с тестом
        self.test = TestManager(questions, shuffle=False)

        # Установка ограничения спинбокса до кол-ва вопросов
        self.current_question.setMinimum(1)
        self.current_question.setMaximum(len(self.test.questions))

        # Инициализация темы теста и текущего вопроса
        self.test_theme.setText(self.test.theme)
        self.set_question(self.test.current_question)

        # Подключение навигации по вопросам
        self.current_question.valueChanged.connect(self.spinbox_nav)
        self.btn_next_question.clicked.connect(self.next_question)
        self.btn_prev_question.clicked.connect(self.prev_question)

        # Подключение кнопок с ответами к функции
        self.answer_0.clicked.connect(partial(self.answered, 0))
        self.answer_1.clicked.connect(partial(self.answered, 1))
        self.answer_2.clicked.connect(partial(self.answered, 2))
        self.answer_3.clicked.connect(partial(self.answered, 3))

        # Подключение управления тестом
        self.finish_test_btn.clicked.connect(self.finish_test)
        self.show_unanswered.clicked.connect(self.select_unanswered)
        self.show_theory_btn.clicked.connect(self.show_theory)

        # Настройка таймера
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer_event)

        # Настройка окна с теорией
        self.theory_window = theory.Ui_Dialog()

    def show_theory(self):
        """Колбек для кнопки показа теории."""
        self.theory_window.show()

    def select_unanswered(self):
        """Колбек для перехода к неотвеченному вопросу."""
        self.set_question(
            choice(self.test.unanswered_questions)
        )

    def reset_time(self):
        """Сброс таймера"""
        self.time = QtCore.QTime(0, 0, 0)

    def spinbox_nav(self):
        """Колбек для навигации через спинбокс."""
        self.set_question(
            self.test.questions[self.current_question.value() - 1])

    def timer_event(self):
        """Триггер счётчика времени."""
        self.time = self.time.addSecs(1)
        self.test_time.setText(self.time.toString("mm:ss"))

    def answered(self, answer_index: int):
        """Колбек кнопок с ответами.

        Аргументы:
            `answer_index` (int): Индекс нажатой кнопки
        """
        self.test.check_answer(answer_index)
        self.answered_count.setText(str(len(self.test.answered_questions)))
        self.next_question(answered=True)

    def toggle_buttons(self, state: bool = None):
        """Метод для переключения состояния кнопок.

        Аргументы:
            `state` (bool, optional): Активировать кнопку. 
            Без указания — переключить кнопку.
        """
        if state is None:
            if self.answer_0.isEnabled():
                self.answer_0.setDisabled(True)
                self.answer_1.setDisabled(True)
                self.answer_2.setDisabled(True)
                self.answer_3.setDisabled(True)
            else:
                answer_index = self.test.answers[self.test.current_question_index]
                answer: QLabel = None
                eval(f'answer = self.answer_{answer_index}.setFont()')

                self.answer_0.setDisabled(False)
                self.answer_1.setDisabled(False)
                self.answer_2.setDisabled(False)
                self.answer_3.setDisabled(False)
        else:
            self.answer_0.setDisabled(state)
            self.answer_1.setDisabled(state)
            self.answer_2.setDisabled(state)
            self.answer_3.setDisabled(state)

    def set_question(self, question: Question):
        """Установить вопрос в активное состояние.

        Аргументы:
            `question` (Question): Экземляр класса вопроса, который нужно активировать
        """
        self.test.select_question(question)

        if question in self.test.answered_questions:
            self.answer_0.setDisabled(True)
            self.answer_1.setDisabled(True)
            self.answer_2.setDisabled(True)
            self.answer_3.setDisabled(True)
        else:
            self.answer_0.setDisabled(False)
            self.answer_1.setDisabled(False)
            self.answer_2.setDisabled(False)
            self.answer_3.setDisabled(False)

        self.question.setText(str(question))
        self.current_question.setValue(self.test.current_question_index + 1)

    def next_question(self, answered: bool = False):
        """Колбек для кнопки следующего вопроса"""

        if self.test.current_question_index != len(self.test.questions) - 1:
            # Если текущий вопрос не последний в списке
            self.set_question(
                self.test.questions[self.test.current_question_index + 1]
            )
        else:
            # Если текущий вопрос последний в списке
            self.toggle_buttons(True)

        if self.test.is_completed:
            # Если ответы есть на все вопросы
            # Если текущий вопрос последний без ответа
            self.set_question(
                self.test.questions[0]
            )
            print('test is completed...')
            self.finish_test()

    def prev_question(self):
        """Колбек для кнопки предыдущего вопроса"""
        if self.test.current_question_index != 0:
            # Если текущий вопрос не первый
            self.set_question(
                self.test.questions[self.test.current_question_index - 1]
            )

    def run_patricia(self, patricia_exe_path: str = 'run_patricia.exe'):
        """Вызов выполняемого файла для запуска демо PATRICIA дерева.

        Аргументы:
            `patricia_exe_path` (str, optional): Путь к .exe файлу. Стандартно — 'run_patricia.exe'.
        """
        patricia_exe_path = patricia_exe_path or 'run_patricia.exe'
        try:
            os.startfile(os.path.abspath(patricia_exe_path))
        except FileNotFoundError:
            msg = QtWidgets.QMessageBox()
            return msg.critical(
                msg.parent(),
                'Ошибка запуска!',
                f'Не найден файл {patricia_exe_path}.'
            )

    def summary_show(self):
        """Вывод информации о прохождении теста."""
        msg = QtWidgets.QMessageBox()
        correct_len = len(self.test.correct_questions)
        wrong_len = len(self.test.failed_questions)
        total_len = len(self.test.questions)
        rating = round(int(correct_len) / int(total_len), 2)
        msg.setIcon(msg.Icon.Information)
        msg.setWindowTitle('Тест завершён!')
        msg.setText(
            f'Потрачено времени: {self.time.toString("mm:ss")}\n'
            f'Количество правильных ответов: {correct_len}.\n'
            f'Количество ошибочных ответов: {wrong_len}.\n'
            f'Правильных ответов: {rating * 100}%.\n'
        )

        show_questions = msg.addButton(
            'К вопросам', QtWidgets.QMessageBox.NoRole
        )
        show_questions.clicked.disconnect()
        show_questions.clicked.connect(msg.close)

        # ! Название файла — run_patricia.exe
        run_patricia = msg.addButton(
            'Запуск', QtWidgets.QMessageBox.YesRole
        )
        run_patricia.clicked.disconnect()
        run_patricia.clicked.connect(self.run_patricia)

        exit_btn = msg.addButton(
            'Выход', QtWidgets.QMessageBox.ResetRole
        )
        exit_btn.clicked.disconnect()
        exit_btn.clicked.connect(partial(exit, 0))

        return msg.exec()

    def finish_test(self):
        """Колбек для кнопки завершения теста"""
        if self.test.is_completed:
            if self.timer.isActive():
                self.timer.stop()
            self.summary_show()
        else:
            msg = QtWidgets.QMessageBox()
            return msg.warning(
                msg.parent(),
                'Тест не завершён!',
                f'Ответов не найдено: {len(self.test.unanswered_questions)}.'
            )


def main():
    app = QApplication(argv)
    window = TestApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
