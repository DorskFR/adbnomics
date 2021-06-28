from models import CleanedData
import os
import csv


class Saver:
    def __init__(self, data: CleanedData):
        self.data = data
        pass

    def to_csv(self, folder: str = "."):
        filename = (
            f"{self.data.provider}_{self.data.dataset_code}_{self.data.series_code}.csv"
        )
        file = os.path.join(folder, filename)
        with open(file, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Provider:", self.data.provider])
            csv_writer.writerow(["Dataset Code:", self.data.dataset_code])
            csv_writer.writerow(["Dataset Name:", self.data.dataset_name])
            csv_writer.writerow(["Frequency:", self.data.frequency])
        self.data.df.to_csv(file, mode="a")
