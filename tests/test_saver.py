import pytest
from models import CleanedData
from saver import Saver
from cleaner import Cleaner
from mock_api_data import api_data
import csv


@pytest.fixture
def cleaner():
    return Cleaner(api_data)


@pytest.fixture
def saver(cleaner):
    return Saver(cleaner.result)


def test_saver_init(saver):
    assert isinstance(saver, Saver)
    assert isinstance(saver.data, CleanedData)


def test_saver_to_csv(saver):
    saver.to_csv(".")
    with open("test.csv", newline="") as csv_file:
        content = csv.reader(csv_file)
        for line in content:
            assert line[0] == "Provider:"
            break
