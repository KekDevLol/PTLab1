import json
import tempfile
import os
import pytest
from src.JsonDataReader import JsonDataReader
from Types import DataType


class TestDataReader:
    def test_json_data_reader_valid_file(self):
        """Тест: корректный JSON-файл"""
        sample_data = {
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

        with tempfile.NamedTemporaryFile(
                mode='w',
                delete=False,
                suffix='.json',
                encoding='utf-8'
        ) as f:
            json.dump(sample_data, f)
            temp_path = f.name

        try:
            reader = JsonDataReader()
            result: DataType = reader.read(temp_path)

            assert result == sample_data
            assert "Иванов Иван Иванович" in result
            assert "математика" in result["Иванов Иван Иванович"]
            assert result["Иванов Иван Иванович"]["математика"] == 67
        finally:
            os.unlink(temp_path)

    def test_json_data_reader_invalid_json(self):
        """Тест: файл содержит некорректный JSON"""
        with tempfile.NamedTemporaryFile(
                mode='w',
                delete=False,
                suffix='.json',
                encoding='utf-8'
        ) as f:
            f.write("not a json")
            temp_path = f.name

        try:
            reader = JsonDataReader()

            with pytest.raises(json.JSONDecodeError):
                reader.read(temp_path)
        finally:
            os.unlink(temp_path)

    def test_json_data_reader_nonexistent_file(self):
        """Тест: файл не существует"""
        reader = JsonDataReader()

        with pytest.raises(FileNotFoundError):
            reader.read("/path/that/does/not/exist.json")

    def test_json_data_reader_invalid_structure_wrong_top_level(self):
        """Тест: JSon содержит массив вместо объекта"""
        wrong_data = ["wrong", "data", "format"]

        with tempfile.NamedTemporaryFile(
                mode='w',
                delete=False,
                suffix='.json',
                encoding='utf-8'
        ) as f:
            json.dump(wrong_data, f)
            temp_path = f.name

        try:
            reader = JsonDataReader()

            with pytest.raises(
                    ValueError,
                    match="JSON должен содержать объект"):
                reader.read(temp_path)
        finally:
            os.unlink(temp_path)

    def test_json_data_reader_invalid_structure_non_dict_value(self):
        """Тест: значение для студента не объект"""
        wrong_data = {
            "Иванов Иван Иванович": "not a dict"
        }

        with tempfile.NamedTemporaryFile(
                mode='w',
                delete=False,
                suffix='.json',
                encoding='utf-8'
        ) as f:
            json.dump(wrong_data, f)
            temp_path = f.name

        try:
            reader = JsonDataReader()

            with pytest.raises(
                    ValueError,
                    match="Значение для ключа 'Иванов Иван Иванович' "
                    "должно быть объектом"):
                reader.read(temp_path)
        finally:
            os.unlink(temp_path)

    def test_json_data_reader_invalid_structure_non_int_grade(self):
        """Тест: оценка не целое число"""
        wrong_data = {
            "Иванов Иван Иванович": {
                "математика": "not an int"
            }
        }

        with tempfile.NamedTemporaryFile(
                mode='w',
                delete=False,
                suffix='.json',
                encoding='utf-8'
        ) as f:
            json.dump(wrong_data, f)
            temp_path = f.name

        try:
            reader = JsonDataReader()

            with pytest.raises(
                    ValueError,
                    match="Оценка 'not an int' для предмета "
                    "'математика' должна быть целым числом"):
                reader.read(temp_path)
        finally:
            os.unlink(temp_path)
