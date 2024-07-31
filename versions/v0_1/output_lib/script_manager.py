from pathlib import Path
from typing import List


class ScriptItem:
    def __init__(self,
                 script_path: Path,
                 script_name: str,
                 project_name: str,
                 bug_number: int,
                 family_name: str):
        self._script_path = script_path
        self._script_name = script_name
        self._project_name = project_name
        self._bug_number = bug_number
        self._family_name = family_name

    def _pretty_representation(self):
        return (f"{self._project_name}, "
                f"{self._bug_number}, "
                f"{self._family_name}")

    def __str__(self):
        return self._pretty_representation()

    def __repr__(self):
        return self._pretty_representation()

    def get_project_name(self):
        return self._project_name

    def get_bug_number(self):
        return self._bug_number

    def get_family_name(self):
        return self._family_name


class ScriptManager:
    def __init__(self,
                 script_path_list: List[Path]):
        self._script_path_list = script_path_list
        self._script_item_list = self._load_script_item_list()

    def _load_script_item_list(self):
        script_item_list = []

        for script_path in self._script_path_list:
            name = script_path.name
            project = name.split("_")[3].lower()
            bug_number = int(name.split("_")[4])
            family_name = name.split("_")[5].lower()

            script_item = ScriptItem(script_path,
                                     name,
                                     project,
                                     bug_number,
                                     family_name)
            script_item_list.append(script_item)

        return script_item_list

    def get_script_item_list(self):
        return self._script_item_list


def load_script_item_list(scripts_path: Path) -> List[ScriptItem]:
    script_path_list = [x for x in scripts_path.iterdir()
                        if x.is_file() and x.name.endswith(".sh")]
    assert len(script_path_list) > 0

    script_manager = ScriptManager(script_path_list)
    script_item_list = script_manager.get_script_item_list()
    assert len(script_path_list) == len(script_item_list)

    return script_item_list
