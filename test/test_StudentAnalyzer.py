import pytest
from src.StudentAnalyzer import StudentAnalyzer
from src.Types import DataType


class TestStudentAnalyzer:
    @pytest.fixture()
    def data_no_students_with_debt(self):
        """Данные для теста без долгов"""
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
        return data

    @pytest.fixture()
    def data_some_students_with_debt(self):
        """Данные для теста:
         некоторыеы студенты с долгом"""
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
        return data

    @pytest.fixture()
    def data_all_student_with_debt(self):
        """
        Данные для теста:
        Все студенты с долгом
        """
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
        return data

    @pytest.fixture()
    def data_with_no_subjects(self):
        """
        Данные для теста:
        Один из студентов без предметов
        """
        data: DataType = {
            "Иванов Иван Иванович": {},
            "Петров Петр Петрович": {
                "математика": 78
            }
        }
        return data

    def test_no_students_with_debt(self, data_no_students_with_debt):
        """Тест: все студенты с оценками >= 61"""
        analyzer = StudentAnalyzer(data_no_students_with_debt)
        result = analyzer.count_students_with_academic_debt()
        assert result == 0

    def test_some_students_with_debt(self, data_some_students_with_debt):
        """Тест: часть студентов с оценками < 61"""
        analyzer = StudentAnalyzer(data_some_students_with_debt)
        result = analyzer.count_students_with_academic_debt()
        assert result == 2

    def test_all_students_with_debt(self, data_all_student_with_debt):
        """Тест: все студенты имеют хотя бы одну оценку < 61"""
        analyzer = StudentAnalyzer(data_all_student_with_debt)
        result = analyzer.count_students_with_academic_debt()
        assert result == 2

    def test_empty_data(self):
        """Тест: пустые данные"""
        data: DataType = {}
        analyzer = StudentAnalyzer(data)
        result = analyzer.count_students_with_academic_debt()
        assert result == 0

    def test_student_with_no_subjects(self, data_with_no_subjects):
        """Тест: один из студентов не имеет оценок"""
        analyzer = StudentAnalyzer(data_with_no_subjects)
        result = analyzer.count_students_with_academic_debt()
        assert result == 0
