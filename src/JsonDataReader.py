import json
from TextDataReader import DataReader
from Types import DataType


class JsonDataReader(DataReader):
    """
    Читает JSON-файл, содержащий оценки студентов.
    Пример формата:
    {
     "Иванов Иван Иванович": {
     "математика": 67,
     "литература": 100,
     "программирование": 91
     },
     "Петров Петр Петрович": {
     "математика": 78,
     "химия": 87,
     "социология": 61
     }
    }
    """
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict) верхнего уровня.")

        for key, value in data.items():
            if not isinstance(value, dict):
                raise ValueError(f"Значение для ключа "
                                 f"'{key}' должно быть объектом (оценки).")

            for subject, grade in value.items():
                if not isinstance(grade, int):
                    raise ValueError(f"Оценка '{grade}' для предмета "
                                     f"'{subject}' должна быть целым числом.")
        return data
