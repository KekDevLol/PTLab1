from Types import DataType


class StudentAnalyzer:

    def __init__(self, data: DataType):
        self.data = data

    def count_students_with_academic_debt(
            self,
            passing_grade: int = 61
    ) -> int:
        """
        :return: Количество студентов с академическими задолженностями.
        """
        count = 0
        for student_name, subjects in self.data.items():
            if any(grade < passing_grade for grade in subjects.values()):
                count += 1
        return count
