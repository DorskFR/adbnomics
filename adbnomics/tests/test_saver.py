import pytest
from ..lib import Cleaner, CleanedData, Saver
from .mock_api_data import api_data
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
    saver.to_csv("test.csv", "adbnomics/tests")
    with open("adbnomics/tests/test.csv", newline="") as csv_file:
        content = csv.reader(csv_file)
        for line in content:
            assert line[0] == "Provider:"
            break
