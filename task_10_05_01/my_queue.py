# Класс очередь
import json


class Queue:
    """Очередь представляется в качестве линейного списка,
     в котором добавление/удаление элементов идет строго с соответствующих его концов."""

    def __init__(self, elem_source=None):
        if elem_source is None:
            self.list_elements = []
        elif isinstance(elem_source, list):
            self.list_elements = elem_source
        elif isinstance(elem_source, Queue):
            self.list_elements = elem_source.list_elements.copy()
        else:
            raise TypeError("Неверный тип")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """Строковое представление очереди"""
        if len(self.list_elements) > 0:
            return f'{self.list_elements} - очередь'
        else:
            return f'{self.list_elements} - пустая очередь'

    def enqueue(self, element):
        """Добавление элемента в очередь"""
        self.list_elements.append(element)
        return f'{element} добавлен в очередь'

    def dequeue(self):
        """Удаление из очереди"""
        return self.list_elements.pop(0)

    def save(self, filename):
        """сохраняет объект в JSON-файл filename"""
        with open(filename, 'w', encoding='utf-8') as sv:
            sv.write(self.list_elements.__str__())

    def load(self, filename):
        """загружает объект из JSON-файла filename"""
        res = []
        with open(filename, 'r', encoding='utf-8') as ld:
            res = json.loads(ld.read())
        return Queue(res)

