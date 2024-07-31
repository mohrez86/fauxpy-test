from pathlib import Path
from typing import List

from . import file_manager
from .entity_type import ScoredEntity, ScoredStatement


class CsvOutputItem:
    def __init__(self,
                 csv_output_item_path: Path,
                 project_name: str,
                 bug_number: int,
                 technique_name: str,
                 scored_entity_list: List[ScoredEntity]):
        self._csv_output_item_path = csv_output_item_path
        self._project_name = project_name
        self._bug_number = bug_number
        self._technique_name = technique_name
        self._scored_entity_list = scored_entity_list

    def get_csv_output_item_key(self):
        return (f"{self._project_name}:"
                f"{self._bug_number}:"
                f"{self._technique_name}")

    def __repr__(self):
        return self.get_csv_output_item_key()

    def __str__(self):
        return self.get_csv_output_item_key()

    def get_scored_entities(self):
        return self._scored_entity_list

    def get_bug_key(self):
        return (f"{self._project_name}:"
                f"{self._bug_number}")


class CsvOutputManager:
    def __init__(self,
                 version_path: Path,
                 csv_output_directory_name: str):
        self._version_path = version_path
        self._csv_output_directory_name = csv_output_directory_name
        self._csv_output_item_list = self._load_csv_output_item_list()

    def get_csv_output_item_list(self):
        return self._csv_output_item_list

    def _load_csv_output_item_list(self) -> List[CsvOutputItem]:
        csv_output_item_list = []

        csv_output_item_path_list = list(
            (self._version_path /
             self._csv_output_directory_name)
            .iterdir()
        )

        for csv_output_item_path in csv_output_item_path_list:
            csv_output_item = self._get_csv_output_item(csv_output_item_path)
            csv_output_item_list.append(csv_output_item)

        return csv_output_item_list

    @staticmethod
    def _get_csv_output_item(csv_output_item_path: Path) -> CsvOutputItem:
        project_name = csv_output_item_path.name.split("_")[0]
        bug_number = int(csv_output_item_path.name.split("_")[1])
        technique_name = csv_output_item_path.name.split("_")[2]

        csv_item_row_list = file_manager.load_csv_content_file(csv_output_item_path)
        scored_entity_list = []
        for csv_item_row in csv_item_row_list:
            file_path = csv_item_row[0].split("::")[0]
            line_number = int(csv_item_row[0].split("::")[1])
            score = float(csv_item_row[1])
            scored_entity = ScoredStatement(file_path, score, line_number)
            scored_entity_list.append(scored_entity)

        csv_output_item = CsvOutputItem(csv_output_item_path,
                                        project_name,
                                        bug_number,
                                        technique_name,
                                        scored_entity_list)

        return csv_output_item


def get_csv_output_item_list(version_path: Path,
                             csv_output_directory_name: str) -> List[CsvOutputItem]:
    csv_output_manager = CsvOutputManager(version_path,
                                          csv_output_directory_name)
    csv_output_item_list = csv_output_manager.get_csv_output_item_list()
    return csv_output_item_list
