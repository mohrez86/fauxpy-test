from pathlib import Path
from typing import List


class ResultItem:
    def __init__(self,
                 result_path,
                 project_name,
                 bug_number,
                 family_name):
        self._result_path = result_path
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

    def get_result_path(self):
        return self._result_path

    def get_project_name(self):
        return self._project_name

    def get_bug_number(self):
        return self._bug_number

    def get_family_name(self):
        return self._family_name


class ResultManager:
    def __init__(self,
                 project_path_list: List[Path]):
        self._project_path_list = project_path_list
        self._result_item_list = self._load_result_item_list()

    def get_result_item_list(self):
        return self._result_item_list

    def _load_result_item_list(self):
        result_item_list = []

        for project_path in self._project_path_list:
            project_result_item_list = self._get_project_result_item_list(project_path)
            result_item_list += project_result_item_list

        return result_item_list

    def _get_project_result_item_list(self,
                                      project_path: Path) -> List[ResultItem]:
        project_result_item_list = []

        project_name = project_path.name.lower()

        bug_path_list = list(project_path.iterdir())
        assert len(bug_path_list) > 0

        for bug_path in bug_path_list:
            assert bug_path.name.startswith("B")

            bug_result_item_list = self._get_bug_result_item_list(project_name,
                                                                  bug_path)
            assert len(bug_result_item_list) == 4

            project_result_item_list += bug_result_item_list

        return project_result_item_list

    @staticmethod
    def _get_bug_result_item_list(project_name: str,
                                  bug_path: Path) -> List[ResultItem]:
        bug_result_item_list = []

        bug_number = int(bug_path.name.replace("B", ""))

        result_path_list = list(bug_path.iterdir())
        assert len(result_path_list) == 4
        for result_path in result_path_list:
            assert result_path.name.split("_")[1].lower() == project_name
            family_name = result_path.name.split("_")[2].lower()
            result_item = ResultItem(result_path,
                                     project_name,
                                     bug_number,
                                     family_name)
            bug_result_item_list.append(result_item)

        return bug_result_item_list


def load_result_item_list(scripts_path: Path) -> List[ResultItem]:
    project_path_list = [x for x in scripts_path.iterdir()
                         if x.is_dir()]
    assert len(project_path_list) > 0

    result_manager = ResultManager(project_path_list)
    result_item_list = result_manager.get_result_item_list()
    assert len(project_path_list) <= len(result_item_list)

    return result_item_list
