from pathlib import Path
from typing import List

from . import file_manager

_Bip_ground_truth_filename = "bip_ground_truth_info.json"
_Bip_size_counts_filename = "bip_size_counts.json"

_Data_project_directory_name = "data_project"


def get_subject_line_count(subject_key: str) -> int:
    bip_size_counts_file_path_str = str(
        (Path(_Data_project_directory_name) / _Bip_size_counts_filename).absolute().resolve())
    line_count_dict = file_manager.load_json_to_object(bip_size_counts_file_path_str)

    subject_line_count = line_count_dict[subject_key]["LINE_COUNT"]

    return subject_line_count


def get_subject_buggy_line_list(subject_key: str) -> List[str]:
    bip_size_ground_truth_file_path_str = str(
        (Path(_Data_project_directory_name) / _Bip_ground_truth_filename).absolute().resolve())
    ground_truth_info_dict = file_manager.load_json_to_object(bip_size_ground_truth_file_path_str)

    subject_ground_truth_module_item_list = ground_truth_info_dict[subject_key]

    buggy_entity_names = []
    for module_item in subject_ground_truth_module_item_list:
        module_name = module_item["FILE_NAME"]
        entity_items = module_item["LINES"] + module_item["EXTENDED_LINES"]
        for entity_item in entity_items:
            entity_name = f"{module_name}::{entity_item}"
            buggy_entity_names.append(entity_name)

    return buggy_entity_names
