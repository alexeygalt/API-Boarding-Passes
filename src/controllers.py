import json
import typing as t
from pydantic_core import ValidationError
from src import ErrorResponse
from src.parse_input_data import parse_input_data
from src.serializers import BaseInputData
from src.utils import HTTP_MESSAGE, validate_row_data, validate_to_json


def get_current_board_list(environ: dict, response: t.Callable) -> t.List[bytes]:
    """Take current boardings list from data.json"""
    with open("data.json") as f:
        response_body = json.load(f)

    response(HTTP_MESSAGE[200], [("Content-Type", "application/json")])
    return [json.dumps(response_body).encode("utf-8")]


def create_board_list(environ: dict, response: t.Callable) -> t.List[bytes]:
    """Take json data, validate it, write in to data.json and return to client"""
    data = json.loads(parse_input_data(environ))
    try:
        temp = BaseInputData(**data)
    except ValidationError:
        raise ErrorResponse(400, message=f"Data is not valid! Check it.")
    response(HTTP_MESSAGE[201], [("Content-Type", "application/json")])
    temp = validate_row_data(temp.model_dump())
    result = validate_to_json(temp)
    with open("data.json", "w") as file:
        json.dump(result, file, indent=4)
    return [json.dumps(result).encode("utf-8")]
