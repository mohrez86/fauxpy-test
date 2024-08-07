from enum import Enum
from pathlib import Path
from typing import List, Optional

from . import file_manager
from .entity_type import ScoredEntity, ScoredStatement
from .result_manager import ResultItem


class ProjectType(Enum):
    Dev = 0
    DS = 1
    Web = 2
    CLI = 3


class FLTechnique(Enum):
    Tarantula = 0
    Ochiai = 1
    DStar = 2
    Metallaxis = 3
    Muse = 4
    PS = 5
    ST = 6
    AvgAlfa = 7
    AvgSbst = 8
    Average = 7


class FLGranularity(Enum):
    Statement = 0
    Function = 1
    Module = 2


class MetricLiteratureVal:
    def __init__(self,
                 experiment_time: float,
                 e_inspect: float,
                 is_bug_localized: bool,
                 exam_score: float):
        self._experiment_time = experiment_time
        self._e_inspect = e_inspect
        self._is_bug_localized = is_bug_localized
        self._exam_score = exam_score

    def get_experiment_time(self) -> float:
        return self._experiment_time

    def get_e_inspect(self) -> float:
        return self._e_inspect

    def get_exam_score(self) -> float:
        return self._exam_score

    def is_bug_localized(self) -> bool:
        return self._is_bug_localized


class MetricOurVal:
    def __init__(self,
                 cumulative_distance: float,
                 sv_comp_overall_score: float,
                 cumulative_distance2: float):
        self._cumulative_distance = cumulative_distance
        self._sv_comp_overall_score = sv_comp_overall_score
        self._cumulative_distance2 = cumulative_distance2

    def get_cumulative_distance(self) -> float:
        return self._cumulative_distance

    def get_sv_comp_overall_score(self) -> float:
        return self._sv_comp_overall_score

    def get_cumulative_distance2(self) -> float:
        return self._cumulative_distance2


class CsvScoreItem:
    def __init__(self,
                 csv_paths: Optional[List[Path]],
                 script_id: Optional[int],
                 project_name: str,
                 bug_number: int,
                 localization_technique: FLTechnique,
                 granularity: FLGranularity,
                 scored_entities: Optional[List[ScoredEntity]],
                 experiment_time_seconds: float):
        self._csv_paths = csv_paths
        self._script_id = script_id
        self._project_name = project_name
        self._bug_number = bug_number
        self._localization_technique = localization_technique
        self._granularity = granularity
        self._scored_entities = scored_entities
        self._experiment_time_seconds = experiment_time_seconds
        self._metric_literature_val = None
        self._metric_our_val = None
        self._is_predicate = None
        self._is_crashing = None
        self._is_mutable_bug = None
        self._percentage_of_mutants_on_ground_truth = None
        self._project_type = None
        self._number_of_predicate_instances = None
        self._number_of_failing_tests = None
        self._number_of_mutants = None

    def _pretty_representation(self):
        if self._csv_paths is None:
            csv_files = None
        else:
            csv_files = [x.name for x in self._csv_paths]

        return (f"{self._script_id} "
                f"{self._project_name} "
                f"{self._bug_number} "
                f"{self._localization_technique.name} "
                f"{self._granularity.name} "
                f"SEC:{self._experiment_time_seconds} "
                f"Crashing: {self._is_crashing} "
                f"Predicate: {self._is_predicate} "
                f"Mutable: {self._is_mutable_bug} "
                f"{csv_files}")

    def __str__(self):
        return self._pretty_representation()

    def __repr__(self):
        return self._pretty_representation()

    def set_csv_paths(self, val):
        self._csv_paths = val

    def get_script_id(self) -> int:
        return self._script_id

    def set_script_id(self, val):
        self._script_id = val

    def get_technique(self):
        return self._localization_technique

    def get_scored_entities(self) -> List[ScoredEntity]:
        return self._scored_entities

    def get_project_name(self) -> str:
        return self._project_name

    def get_bug_number(self) -> int:
        return self._bug_number

    def get_experiment_time_seconds(self) -> float:
        return self._experiment_time_seconds

    def set_experiment_time_seconds(self, val):
        self._experiment_time_seconds = val

    def set_metric_literature_val(self, metric_literature_val: Optional[MetricLiteratureVal]):
        self._metric_literature_val = metric_literature_val

    def get_metric_literature_val(self) -> MetricLiteratureVal:
        return self._metric_literature_val

    def set_metric_our_val(self, metric_our_val: Optional[MetricOurVal]):
        self._metric_our_val = metric_our_val

    def get_metric_our_val(self) -> MetricOurVal:
        return self._metric_our_val

    def get_granularity(self) -> FLGranularity:
        return self._granularity

    def set_granularity(self, granularity: FLGranularity):
        self._granularity = granularity

    def set_scored_entities(self, scored_entities: Optional[List[ScoredEntity]]):
        self._scored_entities = scored_entities

    def get_bug_key(self) -> str:
        bug_key = f"{self.get_project_name()}:{self.get_bug_number()}"
        return bug_key

    def get_bug_technique_key(self) -> str:
        bug_technique_key = (f"{self.get_project_name()}:"
                             f"{self.get_bug_number()}:"
                             f"{self._localization_technique.name}")
        return bug_technique_key

    def get_is_predicate(self) -> bool:
        return self._is_predicate

    def set_is_predicate(self, value: bool):
        self._is_predicate = value

    def get_is_crashing(self) -> bool:
        return self._is_crashing

    def set_is_crashing(self, value: bool):
        self._is_crashing = value

    def get_is_mutable_bug(self) -> bool:
        return self._is_mutable_bug

    def set_is_mutable_bug(self, value: bool):
        self._is_mutable_bug = value

    def get_percentage_of_mutants_on_ground_truth(self) -> float:
        return self._percentage_of_mutants_on_ground_truth

    def set_percentage_of_mutants_on_ground_truth(self, value: float):
        self._percentage_of_mutants_on_ground_truth = value

    def get_project_type(self) -> ProjectType:
        return self._project_type

    def set_project_type(self, value: ProjectType):
        self._project_type = value

    def get_number_of_predicate_instances(self) -> int:
        assert self._localization_technique == FLTechnique.PS
        return self._number_of_predicate_instances

    def set_number_of_predicate_instances(self, value: int):
        assert self._localization_technique == FLTechnique.PS
        self._number_of_predicate_instances = value

    def get_number_of_failing_tests(self) -> int:
        assert self._localization_technique == FLTechnique.PS
        return self._number_of_failing_tests

    def set_number_of_failing_tests(self, value: int):
        assert self._localization_technique == FLTechnique.PS
        self._number_of_failing_tests = value

    def get_number_of_mutants(self) -> int:
        assert self._localization_technique in [FLTechnique.Metallaxis, FLTechnique.Muse]
        return self._number_of_mutants

    def set_number_of_mutants(self, value: int):
        assert self._localization_technique in [FLTechnique.Metallaxis, FLTechnique.Muse]
        self._number_of_mutants = value


class CsvScoreItemLoadManager:
    def __init__(self,
                 result_item_list: List[ResultItem]):
        self._result_item_list = result_item_list

    @classmethod
    def _get_family_csv_score_items(cls, result_item: ResultItem) -> List[CsvScoreItem]:
        technique_statement_csv_score_items = []

        fauxpy_result_path = result_item.get_result_path()
        experiment_time_seconds_path = fauxpy_result_path / "deltaTime.txt"
        experiment_time_seconds = cls._extract_experiment_time_seconds_from_file_path(experiment_time_seconds_path)
        assert 0 < experiment_time_seconds <= 48 * 3600  # Less that 48 hours, the cluster server timeout limit.

        fauxpy_csv_paths = list(filter(lambda x: x.name.endswith(".csv"), fauxpy_result_path.iterdir()))

        family = result_item.get_family_name()

        cls._check_fauxpy_csv_paths(family, fauxpy_csv_paths)

        granularity = FLGranularity.Statement
        script_id = None
        project_name = result_item.get_project_name()
        bug_num = result_item.get_bug_number()

        if family == "ps":
            score_table = cls.load_csv_score_file(fauxpy_csv_paths, family, granularity)
            current_csv_score = CsvScoreItem(fauxpy_csv_paths,
                                             script_id,
                                             project_name,
                                             bug_num,
                                             FLTechnique.PS,
                                             granularity,
                                             score_table,
                                             experiment_time_seconds)
            technique_statement_csv_score_items.append(current_csv_score)
        else:
            for csv_score_path in fauxpy_csv_paths:
                score_table = cls.load_csv_score_file([csv_score_path], family, granularity)
                technique = cls._get_technique_from_csv_name(csv_score_path.name)
                current_csv_score = CsvScoreItem([csv_score_path],
                                                 script_id,
                                                 project_name,
                                                 bug_num,
                                                 technique,
                                                 granularity,
                                                 score_table,
                                                 experiment_time_seconds)
                technique_statement_csv_score_items.append(current_csv_score)

        return technique_statement_csv_score_items

    def load_csv_score_items(self) -> List[CsvScoreItem]:
        csv_score_items = []

        for result_item in self._result_item_list:
            family_csv_score_items = self._get_family_csv_score_items(result_item)
            csv_score_items += family_csv_score_items

        return csv_score_items

    @classmethod
    def _check_fauxpy_csv_paths(cls, family, fauxpy_csv_paths):
        fauxpy_csv_file_names = [x.name for x in fauxpy_csv_paths]
        if family == "sbfl":
            assert len(fauxpy_csv_paths) == 3
            assert "Scores_Tarantula.csv" in fauxpy_csv_file_names
            assert "Scores_Ochiai.csv" in fauxpy_csv_file_names
            assert "Scores_Dstar.csv" in fauxpy_csv_file_names
        elif family == "mbfl":
            assert len(fauxpy_csv_paths) == 2
            assert "Scores_Metallaxis.csv" in fauxpy_csv_file_names
            assert "Scores_Muse.csv" in fauxpy_csv_file_names
        elif family == "ps":
            assert len(fauxpy_csv_paths) >= 1
            assert any([x.startswith("Scores_") and x.endswith(".csv") for x in fauxpy_csv_file_names])
        elif family == "st":
            assert len(fauxpy_csv_paths) == 1
            assert "Scores_default.csv" in fauxpy_csv_file_names
        else:
            raise Exception("This should never be reached.")

    @classmethod
    def _get_technique_from_csv_name(cls, csv_file_name) -> FLTechnique:
        if "Scores_Tarantula.csv" in csv_file_name:
            return FLTechnique.Tarantula
        if "Scores_Ochiai.csv" in csv_file_name:
            return FLTechnique.Ochiai
        if "Scores_Dstar.csv" in csv_file_name:
            return FLTechnique.DStar
        if "Scores_Metallaxis.csv" in csv_file_name:
            return FLTechnique.Metallaxis
        if "Scores_Muse.csv" in csv_file_name:
            return FLTechnique.Muse
        if "Scores_default.csv" in csv_file_name:
            return FLTechnique.ST

    @classmethod
    def load_csv_score_file(cls,
                            csv_paths: List[Path],
                            family: str,
                            granularity: FLGranularity) -> List[ScoredEntity]:
        assert granularity == FLGranularity.Statement

        if granularity == FLGranularity.Statement:
            if family in ["sbfl", "mbfl"]:
                csv_file_content = file_manager.load_csv_content_file(csv_paths[0])
                scored_entity_items = cls.csv_content_to_scored_sbfl_mbfl_statement_items(csv_file_content)
            elif family == "ps":
                scored_entity_items = cls._get_ps_scored_entity_items_from_csv_files(csv_paths)
            elif family == "st":
                csv_file_content = file_manager.load_csv_content_file(csv_paths[0])
                scored_entity_items = cls.csv_content_to_scored_st_statement_items(csv_file_content)
            else:
                raise Exception("This should never happen.")
        else:
            raise Exception("This should never happen.")

        scored_entity_items.sort(key=lambda x: x.get_score(), reverse=True)
        return scored_entity_items

    @classmethod
    def _get_ps_scored_entity_items_from_csv_files(cls, csv_paths):
        scored_entity_items_dict = {}
        for csv_path in csv_paths:
            current_csv_file_content = file_manager.load_csv_content_file(csv_path)
            current_scored_entity_items = cls.csv_content_to_scored_ps_statement_items(current_csv_file_content)
            for item in current_scored_entity_items:
                if item.get_entity_name() in scored_entity_items_dict.keys():
                    previous_score, _ = scored_entity_items_dict[item.get_entity_name()]
                    scored_entity_items_dict[item.get_entity_name()] = max(item.get_score(), previous_score), item
                else:
                    scored_entity_items_dict[item.get_entity_name()] = item.get_score(), item
        scored_entity_items = [x[1] for x in scored_entity_items_dict.values()]
        return scored_entity_items

    @classmethod
    def csv_content_to_scored_sbfl_mbfl_statement_items(cls,
                                                        csv_file_content: List[List[str]]) -> List[ScoredStatement]:
        scored_statement_items = []
        for row in csv_file_content:
            col1_parts = row[0].split("::")
            file_path_parts = col1_parts[0].split("/")
            relative_file_path = "/".join(file_path_parts[6:])
            line_number = int(col1_parts[1])
            score = float(row[1])
            scored_statement_item = ScoredStatement(relative_file_path, score, line_number)
            scored_statement_items.append(scored_statement_item)

        return scored_statement_items

    @classmethod
    def csv_content_to_scored_ps_statement_items(cls,
                                                 csv_file_content: List[List[str]]) -> List[ScoredStatement]:
        scored_statement_items = []
        for row in csv_file_content:
            col1_parts = row[0].split("::")
            file_path_parts = col1_parts[0].split("/")
            relative_file_path = "/".join(file_path_parts[6:])
            line_start = int(col1_parts[1])
            line_end = int(col1_parts[2])
            score = float(row[1])
            for line_number in range(line_start, line_end + 1):
                scored_statement_item = ScoredStatement(relative_file_path, score, line_number)
                scored_statement_items.append(scored_statement_item)

        return scored_statement_items

    @classmethod
    def csv_content_to_scored_st_statement_items(cls,
                                                 csv_file_content: List[List[str]]) -> List[ScoredStatement]:
        scored_statement_item_dict = {}
        for row in csv_file_content:
            col1_parts = row[0].split("::")
            file_path_parts = col1_parts[0].split("/")
            relative_file_path = "/".join(file_path_parts[6:])
            line_start = int(col1_parts[2])
            line_end = int(col1_parts[3])
            score = float(row[1])
            for line_number in range(line_start, line_end + 1):
                scored_statement_item = ScoredStatement(relative_file_path, score, line_number)
                if scored_statement_item.get_entity_name() not in scored_statement_item_dict.keys():
                    scored_statement_item_dict[scored_statement_item.get_entity_name()] = scored_statement_item
                else:
                    assert (scored_statement_item_dict[scored_statement_item.get_entity_name()].get_score()
                            > scored_statement_item.get_score())

        scored_statement_item_list = list(scored_statement_item_dict.values())

        return scored_statement_item_list

    @classmethod
    def _extract_experiment_time_seconds_from_file_path(cls, experiment_time_seconds_path):
        file_content = file_manager.load_file_content(experiment_time_seconds_path)
        content_parts = file_content.split("=")
        time_part = content_parts[1].strip()
        num_value_time = float(time_part)
        return num_value_time
