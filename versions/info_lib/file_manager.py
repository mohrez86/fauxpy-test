import csv
import json
from pathlib import Path
from typing import List, Any


def load_csv_content_file(csv_path: Path) -> List[List[str]]:
    rows = []
    with csv_path.open("r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return rows


def load_json_to_object(file_name: str):
    with open(file_name) as file:
        data_dict = json.load(file)

    return data_dict


def save_object_to_json(obj: Any,
                        file_path: Path):
    string_object = json.dumps(obj, indent=5)
    save_string_to_file(string_object, file_path)


def save_string_to_file(content: str,
                        file_path: Path):
    with file_path.open("w") as file:
        file.write(content)
