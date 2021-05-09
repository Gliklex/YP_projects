# Класс очередь
import json


class queue:
    """Очередь представляется в качестве линейного списка,
     в котором добавление/удаление элементов идет строго с соответствующих его концов."""

    def __init__(self, list_elements):
        if isinstance(list_elements, list):
            self.list_elements = list_elements

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
        res = ""
        while len(self.list_elements) > 0:
            res += f'{self.list_elements.pop(0)} покинул очередь\n'
        return res

    def save(self, filename):
        """сохраняет объект в JSON-файл filename"""
        with open(filename, 'w', encoding='utf-8') as sv:
            sv.write(self.list_elements.__str__())

    def load(self, filename):
        """загружает объект из JSON-файла filename"""
        res = []
        with open(filename, 'r', encoding='utf-8') as ld:
            res = json.loads(ld.read())
        return queue(res)

