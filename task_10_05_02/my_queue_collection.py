from task_10_05_01.my_queue import Queue
import json


class QueueCollection:
    """класс-контейнер содержит набор объектов из my_queue"""

    def __init__(self, list_queue=None):
        """Создает пустой контейнер для очередей"""
        if list_queue is None:
            self.list_queue = []
        elif all(isinstance(q, Queue) for q in list_queue):
            self.list_queue = list_queue
        else:
            raise TypeError("Может содержать только очереди")

    def __str__(self):
        """Строковое представление очереди"""
        return f'!{self.list_queue}!'

    def __getitem__(self, item):
        """Получение среза"""
        return self.list_queue[item]

    def add(self, value):
        """Добавляет очередь в конец контейнера"""
        if isinstance(value, Queue):
            self.list_queue.append(value)
        else:
            raise TypeError("Может содержать только очереди")

    def remove(self, index):
        """Удаляет очередь по индексу из контейнера"""
        self.list_queue.pop(index)

    def save(self, filename):
        """сохраняет объект в JSON-файл filename"""
        with open(filename, 'w', encoding='utf-8') as sv:
            sv.write(self.list_queue.__str__())

    def load(self, filename):
        """загружает объект из JSON-файла filename"""
        res = []
        with open(filename, 'r', encoding='utf-8') as ld:
            res = json.loads(ld.read())
        return QueueCollection(res)


art = QueueCollection([Queue([1, 2, 3])])
art.add(Queue([1]))
print(art)