import json
import pytest
import tempfile
import os
from src.JsonDataReader import JsonDataReader


class TestJsonDataReader:

    def setup_method(self):
        """Подготовка общих данных или объектов перед каждым тестом """
        self.reader = JsonDataReader()

    def _create_temp_json(self, data):
        """Вспомогательный метод для создания временного JSON-файла """
        temp_file = tempfile.NamedTemporaryFile(
            mode='w',
            delete=False,
            suffix='.json',
            encoding='utf-8'
        )
        json.dump(data, temp_file)
        temp_file.close()
        return temp_file.name

    def test_json_with_debt(self):
        data = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 50
            },
            "Петров Петр Петрович": {
                "математика": 78,
                "химия": 87,
                "социология": 61
            }
        }
        temp_path = self._create_temp_json(data)
        result = self.reader.read(temp_path)
        assert result == ["Иванов Иван Иванович"]
        os.remove(temp_path)

    def test_json_no_debt(self):
        data = {
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
        temp_path = self._create_temp_json(data)
        result = self.reader.read(temp_path)
        assert result == []
        os.remove(temp_path)

    def test_json_all_have_debt(self):
        data = {
            "Иванов Иван Иванович": {
                "математика": 60,
                "литература": 55
            },
            "Петров Петр Петрович": {
                "физика": 40,
                "химия": 50
            }
        }
        temp_path = self._create_temp_json(data)
        result = self.reader.read(temp_path)
        assert set(result) == {"Иванов Иван Иванович", "Петров Петр Петрович"}
        os.remove(temp_path)

    def test_json_empty(self):
        data = {}
        temp_path = self._create_temp_json(data)
        result = self.reader.read(temp_path)
        assert result == []
        os.remove(temp_path)

    def test_json_missing_score(self):
        data = {
            "Иванов Иван Иванович": {},
            "Петров Петр Петрович": {
                "физика": 60
            }
        }
        temp_path = self._create_temp_json(data)
        result = self.reader.read(temp_path)
        assert result == ["Петров Петр Петрович"]
        os.remove(temp_path)

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            self.reader.read("nonexistent.json")
