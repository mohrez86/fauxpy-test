import argparse
from pathlib import Path
from typing import List

from info_lib import csv_output_feature_manager, csv_output_load_manager, file_manager
from info_lib.csv_output_feature_manager import CsvOutputFeatureItem

_Csv_output_directory_name_prefix = "csv_output"

_Fl_features_file_name_postfix = "fl_features.json"
_Extracted_features_directory_name = "extracted_features"


def check_current_against_previous(
        current_csv_output_feature_item_list: List[CsvOutputFeatureItem],
        previous_csv_output_feature_item_list: List[CsvOutputFeatureItem]):
    assert len(current_csv_output_feature_item_list) == len(previous_csv_output_feature_item_list)

    discrepancy = False
    for current_item in current_csv_output_feature_item_list:
        previous_item_list = [x for x in previous_csv_output_feature_item_list
                              if x.get_csv_output_item_key() == current_item.get_csv_output_item_key()]
        assert len(previous_item_list) == 1
        previous_item = previous_item_list[0]

        if current_item != previous_item:
            discrepancy = True
            print(f"Discrepancy:\n"
                  f"current_version: {current_item}\n"
                  f"previous_version: {previous_item}")

    return discrepancy


def produce_fl_features_for_version_exp(version_path: Path,
                                        feature_dict_file_name: str,
                                        csv_output_directory_name: str) -> List[CsvOutputFeatureItem]:
    print(f"Extracting features for version {version_path.name}")

    csv_output_item_list = csv_output_load_manager.get_csv_output_item_list(version_path,
                                                                            csv_output_directory_name)
    (csv_output_feature_item_list,
     csv_output_feature_item_dict_list) = csv_output_feature_manager.get_csv_output_feature_item_dict_list(
        csv_output_item_list
    )

    feature_dict_file_path = (Path(_Extracted_features_directory_name) /
                              feature_dict_file_name)
    print(f"Saving features for version {version_path.name}")
    file_manager.save_object_to_json(csv_output_feature_item_dict_list,
                                     feature_dict_file_path)

    return csv_output_feature_item_list


def main():
    # https://www.geeksforgeeks.org/command-line-arguments-in-python/
    help_message = (f"testing the current version against a previous "
                    f"version. Generate corresponding features "
                    f"files before running this Python script.")
    parser = argparse.ArgumentParser(description=help_message)

    required_args = parser.add_argument_group('Required arguments')
    required_args.add_argument("-e",
                               "--Experiment",
                               choices=["tiny", "small", "large"],
                               required=True,
                               help="experiment type.")
    required_args.add_argument("-c",
                               "--Current",
                               required=True,
                               help="name of the current version "
                                    "to test (e.g., v0_1).")
    required_args.add_argument("-p",
                               "--Previous",
                               required=True,
                               help="name of the previous version "
                                    "to test (e.g., v0_0).")
    args = parser.parse_args()

    experiment_name = args.Experiment
    current_version_name = args.Current
    previous_version_name = args.Previous

    csv_output_directory_name = (f"{_Csv_output_directory_name_prefix}_"
                                 f"{experiment_name}")

    current_features_dict_file_name = (f"{current_version_name}_"
                                       f"{experiment_name}_"
                                       f"{_Fl_features_file_name_postfix}")
    previous_features_dict_file_name = (f"{previous_version_name}_"
                                        f"{experiment_name}_"
                                        f"{_Fl_features_file_name_postfix}")

    current_version_path = Path(current_version_name).resolve()
    previous_version_path = Path(previous_version_name).resolve()

    current_csv_output_feature_item_list = produce_fl_features_for_version_exp(
        current_version_path,
        current_features_dict_file_name,
        csv_output_directory_name)

    previous_csv_output_feature_item_list = produce_fl_features_for_version_exp(
        previous_version_path,
        previous_features_dict_file_name,
        csv_output_directory_name)

    discrepancy = check_current_against_previous(current_csv_output_feature_item_list,
                                                 previous_csv_output_feature_item_list)

    if not discrepancy:
        print(f"Output of {current_version_name} "
              f"is equivalent to "
              f"the output of {previous_version_name}")


if __name__ == '__main__':
    main()
