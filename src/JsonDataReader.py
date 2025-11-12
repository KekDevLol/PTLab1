import json
from TextDataReader import DataReader


class JsonDataReader(DataReader):

    def read(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return self._analyze_academic_debt(data)

    @staticmethod
    def _analyze_academic_debt(data: dict):
        debt_students = []
        for student, subjects in data.items():
            has_debt = any(score < 61 for score in subjects.values())
            if has_debt:
                debt_students.append(student)
        return debt_students
