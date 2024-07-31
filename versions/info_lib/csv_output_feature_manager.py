from typing import List, Dict, Tuple

from . import data_project_manager
from .csv_output_load_manager import CsvOutputItem
from .generalized_e_inspect import EInspect


class CsvOutputFeatureItem:
    def __init__(self,
                 csv_output_item_key: str,
                 generalized_e_inspect: float,
                 output_length: int):
        self._csv_output_item_key = csv_output_item_key
        self._generalized_e_inspect = generalized_e_inspect
        self._output_length = output_length

    def get_csv_output_item_key(self):
        return self._csv_output_item_key

    def _pretty_representation(self):
        return (f"{self._csv_output_item_key}, "
                f"{self._generalized_e_inspect}, "
                f"{self._output_length}")

    def __eq__(self, other):
        # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
        if isinstance(other, CsvOutputFeatureItem):
            return (self._csv_output_item_key == other._csv_output_item_key and
                    self._generalized_e_inspect == other._generalized_e_inspect and
                    self._output_length == other._output_length)
        return False

    def __str__(self):
        return self._pretty_representation()

    def __repr__(self):
        return self._pretty_representation()

    def get_as_dict(self):
        return {
            "csv_output_item_key": self._csv_output_item_key,
            "generalized_e_inspect": self._generalized_e_inspect,
            "output_length": self._output_length
        }


class CsvOutputFeatureManager:
    def __init__(self,
                 csv_output_item: CsvOutputItem):
        self._csv_output_item = csv_output_item
        self._csv_output_feature_item = self._extract_csv_output_feature_item()

    def get_csv_output_feature_item(self):
        return self._csv_output_feature_item

    def _extract_csv_output_feature_item(self) -> CsvOutputFeatureItem:
        generalized_e_inspect = self._get_generalized_e_inspect()
        output_length = len(self._csv_output_item.get_scored_entities())
        csv_output_feature_item = CsvOutputFeatureItem(
            self._csv_output_item.get_csv_output_item_key(),
            generalized_e_inspect,
            output_length
        )

        return csv_output_feature_item

    def _get_generalized_e_inspect(self):
        subject_key = self._csv_output_item.get_bug_key()
        bug_line_count = data_project_manager.get_subject_line_count(subject_key)
        buggy_lines_list = data_project_manager.get_subject_buggy_line_list(subject_key)

        e_inspect_object = EInspect(self._csv_output_item.get_scored_entities(),
                                    bug_line_count,
                                    buggy_lines_list)
        e_inspect_value = e_inspect_object.get_e_inspect()

        return e_inspect_value


def get_csv_output_feature_item_dict_list(csv_output_item_list) -> Tuple[List, List[Dict]]:
    csv_output_feature_item_list = []
    csv_output_feature_item_dict_list = []

    for csv_output_item in csv_output_item_list:
        csv_output_feature_manager = CsvOutputFeatureManager(csv_output_item)
        csv_output_feature_item = csv_output_feature_manager.get_csv_output_feature_item()
        csv_output_feature_item_list.append(csv_output_feature_item)
        csv_output_feature_item_dict_list.append(csv_output_feature_item.get_as_dict())

    return csv_output_feature_item_list, csv_output_feature_item_dict_list
