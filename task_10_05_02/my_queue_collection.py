from task_10_05_01.my_queue import Queue


class QueueCollection:
    """класс-контейнер содержит набор объектов из my_queue"""

    def __init__(self):
        self.list_queue = []

    def __str__(self):
        """Строковое представление очереди"""
        if len(self.list_queue) > 0:
            return f'{self.list_queue}'
        else:
            return None

    def __getitem__(self, item):
        pass


