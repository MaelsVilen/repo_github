class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Делаю записи')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Зарисовываю скетчи')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Выделяю полезную информацию')

p1 = Pen('Parker')
p1.draw()

p2 = Pencil('H2')
p2.draw()

p3 = Handle('Highlighter')
p3.draw()