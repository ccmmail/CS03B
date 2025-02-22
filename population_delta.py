"""Class to read/write CSV files for CS3B project 4."""

import csv

class Population:
    """Create object to read file, calc deltas, and write to new file."""
    def __init__(self):
        self.file_import = []
        self.annual = {}
        self.biannual = {}

    def import_csv(self, file_name: str) -> None:
        """Read csv file and store content as list of dictionaries."""
        try:
            csv_file = open(file_name, "r")
        except FileNotFoundError:
            print("File not found.")
        else:
            with csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.file_import.append(row)

    def biannual_delta(self) -> int:
        """Populate biannual dict of deltas and return count of positive deltas."""
        positive_deltas = 0
        if len(self.file_import) == 0:  # if file_import is empty list
            return None
        else:
            for row in self.file_import:
                delta = int(row["Pop_Est_Jul_2020"]) - int(row["Pop_Est_ Apr_2020 "])
                self.biannual[row["Geographic_Area"]] = delta
                if delta > 0:
                    positive_deltas += 1
            return positive_deltas

    def annual_delta(self) -> int:
        """Populate annual dict of deltas and return count of positive deltas."""
        positive_deltas = 0
        if len(self.file_import) == 0:  # if file_import is empty list
            return None
        else:
            for row in self.file_import:
                delta = int(row["Pop_Est_Jul_2021"]) - int(row["Pop_Est_Jul_2020"])
                self.annual[row["Geographic_Area"]] = delta
                if delta > 0:
                    positive_deltas += 1
            return positive_deltas

    def search_by_loc(self, location:str) -> list:
        """Return list of matching search loc's annual and biannual deltas."""
        found = []
        # search annual delta
        try:
            found.append({"annual delta" : self.annual[location]})
        except KeyError:
            found.append(0)
        # search biannual delta
        try:
            found.append({"biannual delta" : self.biannual[location]})
        except KeyError:
            found.append(0)
        return found

    def export_csv(self, filename:str) -> None:
        """Create CSV file with location, annual, and biannual deltas."""
        header = ["Geographic Area", "Bi-Annual Delta", "Annual Delta"]
        data_rows = [[key, self.biannual[key], self.annual[key]] for key in self.biannual]
        with open(filename, "w") as csv_delta_file:
            csv_writer = csv.writer(csv_delta_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data_rows)


def main():
    """Run test cases for Population class."""
    print("Test cases for Population class.")
    population = Population()
    population.import_csv("census_population.csv")
    print("Count of positive biannual deltas: ", population.biannual_delta())  # returns 349
    print("Count of positive annual deltas: ", population.annual_delta())  # returns 364
    print(population.search_by_loc("New York city, New York"))
    print(population.search_by_loc("Nowhere, NotAState"))  # returns zeroes
    population.export_csv("population_delta.csv")


if __name__ == "__main__":
    main()