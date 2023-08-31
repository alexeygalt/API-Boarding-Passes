import re
import typing as t

HTTP_MESSAGE = {
    200: "200 OK",
    201: "201 Created",
    303: "303 See Other",
    304: "304 Not Modified",
    400: "400 Bad Request",
    404: "404 Not Found",
    405: "405 Method Not Allowed",
    422: "422 Unprocessable Entity",
    500: "500 Internal Server Error",
}


# Checks if any regex matches with given URL
def route_url(regexes: t.List[str], url: str) -> bool:
    matches = [bool(re.compile(regex).match(url)) for regex in regexes]
    return any(matches)


# the implementation of this algorithm expects the use of all available passes in the stack
# otherwise, input data restriction and their subsequent validation are required


def validate_row_data(obj: dict) -> dict:
    result = {}
    count = 1
    departure_point_set = {item["departure_point"] for item in obj["boarding_passes"]}
    arrival_point_set = {item["arrival_point"] for item in obj["boarding_passes"]}

    departure_point = list(departure_point_set.difference(arrival_point_set))[0]
    while obj["boarding_passes"]:
        for boarding_pass in obj["boarding_passes"]:
            if boarding_pass["departure_point"] == departure_point:
                result[count] = boarding_pass
                departure_point = boarding_pass["arrival_point"]
                count += 1
                obj["boarding_passes"].remove(boarding_pass)

    return result


# of course, this is probably a hardcode,
# but I think that in this case we do not get a sick number of entrance tickets.
# Plus, we carry out minimal validation at the entrance


def validate_to_json(obj: dict) -> list[dict]:
    """preparing data for writing to json and returning to the client"""
    result = []
    for key, value in obj.items():
        match value["transport_type"]:
            case "train":
                temp = (
                    f"Take {value['transport_type']} {value['number']}"
                    f" from {value['departure_point']} to {value['arrival_point']}."
                    f"Sit in seat {value['seat_place']}."
                )
                result.append({key: temp})

            case "bus":
                temp = (
                    f"Take {value['transport_type']} from {value['departure_point']} to {value['arrival_point']}."
                    f"No seat assignment."
                )
                result.append({key: temp})
            case "fly":
                temp = (
                    f"From {value['departure_point']} take flight {value['number']} to {value['arrival_point']}."
                    f"Gate {value['gate']}, seat {value['seat_place']}."
                )

                if result:
                    if "flight" in result[-1].values():
                        temp += "Baggage will we automatically transferred from your last leg."
                else:
                    temp += f"Baggage drop at ticket counter {value['baggage']}."

                result.append({key: temp})

    return result
