from .models import CleanedData
import pandas
from .utils import parse_code


class Cleaner:
    def __init__(self, data):
        self.data: dict = data.get("series").get("docs")
        self.result = CleanedData(
            provider=self.data[0].get("provider_code"),
            dataset_code=self.data[0].get("dataset_code"),
            dataset_name=self.data[0].get("dataset_name"),
            series_code=parse_code(self.data[0].get("series_code")),
            frequency=self.data[0].get("@frequency"),
        )
        self.parse_all_series_into_dataframe()

    def parse_one_series_into_dataframe(self, series: dict):
        series_name = series.get("series_name").split(chr(8211))[1].strip()
        index = series.get("period_start_day")
        values = [None if v == "NA" else v for v in series.get("value")]
        return pandas.DataFrame(index=index, data=values, columns=[series_name])

    def parse_all_series_into_dataframe(self):
        all_dfs = [self.parse_one_series_into_dataframe(series) for series in self.data]
        self.result.df = pandas.concat(all_dfs, axis=1)
        self.result.df.index.name = "Date"
        return self.result
