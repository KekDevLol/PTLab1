import pytest
from src.StudentAnalyzer import StudentAnalyzer
from src.Types import DataType

class TestStudentAnalyzer:

    def test_no_students_with_debt(self):
        """Тест: все студенты с оценками >= 61"""
        data: DataType = {
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
        analyzer = StudentAnalyzer(data)
        result = analyzer.count_students_with_academic_debt()
        assert result == 0

    def test_some_students_with_debt(self):
        """Тест: часть студентов с оценками < 61"""
        data: DataType = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 58,
                "химия": 87,
                "социология": 61
            },
            "Сидоров Сидор Сидорович": {
                "физика": 90,
                "история": 60
            }
        }
        analyzer = StudentAnalyzer(data)
        result = analyzer.count_students_with_academic_debt()
        assert result == 2

    def test_all_students_with_debt(self):
        """Тест: все студенты имеют хотя бы одну оценку < 61"""
        data: DataType = {
            "Иванов Иван Иванович": {
                "математика": 50,
                "литература": 100
            },
            "Петров Петр Петрович": {
                "математика": 58,
                "химия": 87
            }
        }
        analyzer = StudentAnalyzer(data)
        result = analyzer.count_students_with_academic_debt()
        assert result == 2

    def test_empty_data(self):
        """Тест: пустые данные"""
        data: DataType = {}
        analyzer = StudentAnalyzer(data)
        result = analyzer.count_students_with_academic_debt()
        assert result == 0

    def test_student_with_no_subjects(self):
        """Тест: один из студентов не имеет оценок"""
        data: DataType = {
            "Иванов Иван Иванович": {},
            "Петров Петр Петрович": {
                "математика": 78
            }
        }
        analyzer = StudentAnalyzer(data)
        result = analyzer.count_students_with_academic_debt()
        assert result == 0