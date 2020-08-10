"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class PlatesClass:
    def __init__(self):
        self.plates = 0
        self.stack_count = 1

    def is_empty(self):
        return self.plates == 0

    def push_in(self):
        self.plates += 1

        if self.plates == 5:
            self.stack_count += 1
            self.plates = 0

    def pop_out(self):
        self.plates -= 1

        if self.plates == 0:
            self.stack_count -= 1
            self.plates = 5
        if self.stack_count <= 0:
            self.plates = 0
            self.stack_count = 1

    def get_val(self):
        print(f"количество тарелок в {self.stack_count}й стопке составляет {self.plates}")

cupboard = PlatesClass()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.push_in()
cupboard.get_val()
cupboard.pop_out()
cupboard.pop_out()
cupboard.pop_out()
cupboard.pop_out()
cupboard.pop_out()
cupboard.get_val()
cupboard.pop_out()
cupboard.pop_out()
cupboard.pop_out()
cupboard.pop_out()
cupboard.get_val()