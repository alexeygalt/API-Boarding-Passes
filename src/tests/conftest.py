import pytest


@pytest.fixture(scope="class")
def input_row_data():
    return {
        "boarding_passes": [
            {
                "transport_type": "fly",
                "departure_point": "Moscow",
                "arrival_point": "London",
                "number": "227D",
                "seat_place": "141",
                "baggage": 12,
                "gate": "16",
            },
            {
                "transport_type": "bus",
                "departure_point": "Berlin",
                "arrival_point": "Berlin Airport",
            },
            {
                "transport_type": "train",
                "departure_point": "Berlin Airport",
                "arrival_point": "Praga",
                "number": "21A",
                "seat_place": "40",
                "baggage": 44,
            },
            {
                "transport_type": "fly",
                "departure_point": "London",
                "arrival_point": "Berlin",
                "number": "113C",
                "seat_place": "24",
                "gate": "322",
                "baggage": 312,
            },
        ]
    }


@pytest.fixture(scope="class")
def output_row_data():
    return {
        1: {
            "transport_type": "fly",
            "departure_point": "Moscow",
            "arrival_point": "London",
            "number": "227D",
            "seat_place": "141",
            "baggage": 12,
            "gate": "16",
        },
        2: {
            "transport_type": "fly",
            "departure_point": "London",
            "arrival_point": "Berlin",
            "number": "113C",
            "seat_place": "24",
            "gate": "322",
            "baggage": 312,
        },
        3: {
            "transport_type": "bus",
            "departure_point": "Berlin",
            "arrival_point": "Berlin Airport",
        },
        4: {
            "transport_type": "train",
            "departure_point": "Berlin Airport",
            "arrival_point": "Praga",
            "number": "21A",
            "seat_place": "40",
            "baggage": 44,
        },
    }


@pytest.fixture(scope="class")
def output_validate_to_json():
    return [
        {
            1: "From Moscow take flight 227D to London.Gate 16, seat 141.Baggage drop at ticket counter 12."
        },
        {2: "From London take flight 113C to Berlin.Gate 322, seat 24."},
        {3: "Take bus from Berlin to Berlin Airport.No seat assignment."},
        {4: "Take train 21A from Berlin Airport to Praga.Sit in seat 40."},
    ]
