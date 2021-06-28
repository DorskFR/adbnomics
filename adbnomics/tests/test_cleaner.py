import pytest
from pandas import DataFrame

from ..lib import CleanedData, Cleaner
from .mock_api_data import api_data


@pytest.fixture
def cleaner():
    return Cleaner(api_data)


def test_cleaner_init(cleaner):
    assert isinstance(cleaner, Cleaner)
    assert hasattr(cleaner, "data")
    assert isinstance(cleaner.data, list)
    assert isinstance(cleaner.data[0], dict)
    assert isinstance(cleaner.result, CleanedData)
    assert len(cleaner.data) == 38


def test_cleaner_parse_one_series_into_dataframe(cleaner):
    df = cleaner.parse_one_series_into_dataframe(cleaner.data[0])
    assert isinstance(df, DataFrame)
    assert df.columns == ["Argentina"]


def test_cleaner_parse_all_series_into_dataframe(cleaner):
    result = cleaner.parse_all_series_into_dataframe()
    assert isinstance(result, CleanedData)
    assert result.provider == "BIS"
    assert result.dataset_code == "cbpol"
    assert result.dataset_name == "Policy rates"
    assert result.frequency == "monthly"
    assert isinstance(result.df, DataFrame)
    assert len(result.df.columns) == 38
    assert result.df.index.name == "Date"
