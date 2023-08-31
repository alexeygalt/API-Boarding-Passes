import unittest

import pytest

from src.utils import validate_row_data, validate_to_json


class TestRowData(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def input_row_data_fixture(self, input_row_data):
        self.input_row_data = input_row_data

    @pytest.fixture(autouse=True)
    def output_row_data_fixture(self, output_row_data):
        self.output_row_data = output_row_data

    def test_validate_row_data_success(self):
        actual = validate_row_data(self.input_row_data)
        self.assertEqual(actual, self.output_row_data)


class TestValidateTojson(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def input_fixture(self, output_row_data):
        self.input_data = output_row_data

    @pytest.fixture(autouse=True)
    def expected_data(self, output_validate_to_json):
        self.expected = output_validate_to_json

    def test_validate_to_json_success(self):
        actual = validate_to_json(self.input_data)
        self.assertEqual(actual, self.expected)
