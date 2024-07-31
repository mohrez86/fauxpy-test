import argparse
import pathlib
from typing import List

from output_lib import file_manager
from output_lib.csv_score_load_manager import CsvScoreItemLoadManager, CsvScoreItem
from output_lib.result_manager import load_result_item_list, ResultItem
from output_lib.script_manager import load_script_item_list, ScriptItem

# Constants
_Scripts_tiny_file_name = "run_tiny_scripts.sh"
_Scripts_small_file_name = "run_small_scripts.sh"
_Scripts_large_file_name = "run_large_scripts.sh"

_Scripts_tiny_dir_name = "scripts_tiny"
_Scripts_small_dir_name = "scripts_small"
_Scripts_large_dir_name = "scripts_large"

_Csv_output_tiny_dir_name = "csv_output_tiny"
_Csv_output_small_dir_name = "csv_output_small"
_Csv_output_large_dir_name = "csv_output_large"


def _cross_check(script_item_list: List[ScriptItem],
                 result_item_list: List[ResultItem]):
    """
    Enduring that there is one and only one result for each script.
    """

    assert len(script_item_list) == len(result_item_list)
    for script_item_list in script_item_list:
        item_list = [x for x in result_item_list
                     if x.get_project_name() == script_item_list.get_project_name()
                     and x.get_bug_number() == script_item_list.get_bug_number()
                     and x.get_family_name() == script_item_list.get_family_name()]
        assert len(item_list) == 1


def refine_csv_score_item(csv_score_item: CsvScoreItem):
    """
    At this step, we remove the starting part of
    module paths in a csv_score_item so that
    module paths comply with the ground truth
    information.

    For example:
    we change
        B3_Fsbfl_Gstatement/black/black.py
    to
        black.py
    """

    for scored_entity_item in csv_score_item.get_scored_entities():
        old_file_path = scored_entity_item.get_file_path()
        path_parts = old_file_path.split("/")
        new_file_path = "/".join(path_parts[2:])
        scored_entity_item.set_path(new_file_path)


def produce_csv_output_for_exp(scripts_dir_name,
                               csv_output_dir_name):
    print(f"Parameters: "
          f"{scripts_dir_name}, "
          f"{csv_output_dir_name}")

    scripts_path = pathlib.Path(scripts_dir_name)
    script_item_list = load_script_item_list(scripts_path)
    result_item_list = load_result_item_list(scripts_path)
    _cross_check(script_item_list, result_item_list)

    csv_score_item_load_manager = CsvScoreItemLoadManager(result_item_list)
    csv_score_items = csv_score_item_load_manager.load_csv_score_items()

    for csv_score_item in csv_score_items:
        refine_csv_score_item(csv_score_item)

    csv_output_dir_path = file_manager.clean_make_output_dir(csv_output_dir_name)
    file_manager.save_score_items_to_given_directory_path(csv_output_dir_path,
                                                          csv_score_items)


def main():
    # https://www.geeksforgeeks.org/command-line-arguments-in-python/
    help_message = (f"Run the corresponding bash scrips "
                    f"'{_Scripts_tiny_file_name}', "
                    f"'{_Scripts_small_file_name}', or "
                    f"'{_Scripts_large_file_name}' "
                    f"before running this Python script.")

    parser = argparse.ArgumentParser(description=help_message)
    required_args = parser.add_argument_group('Required arguments')
    required_args.add_argument("-e",
                               "--Experiment",
                               choices=["tiny", "small", "large"],
                               required=True,
                               help="Experiment type.")
    args = parser.parse_args()

    if args.Experiment == "tiny":
        scripts_dir_name = _Scripts_tiny_dir_name
        csv_output_dir_name = _Csv_output_tiny_dir_name
    elif args.Experiment == "small":
        scripts_dir_name = _Scripts_small_dir_name
        csv_output_dir_name = _Csv_output_small_dir_name
    elif args.Experiment == "large":
        scripts_dir_name = _Scripts_large_dir_name
        csv_output_dir_name = _Csv_output_large_dir_name
    else:
        raise Exception("This one must not happen.")

    produce_csv_output_for_exp(scripts_dir_name,
                               csv_output_dir_name)


if __name__ == '__main__':
    main()
