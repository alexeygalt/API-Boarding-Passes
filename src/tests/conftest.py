import pytest


@pytest.fixture(scope="class")
def input_row_data():
    return {
        "departure_point": "Moscow",
        "arrival_point": "Praga",
        "boarding_passes": [
            {
                "transport_type": "fly",
                "departure_point": "Moscow",
                "arrival_point": "London",
                "number": "37b",
                "seat_place": "123",
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
                "number": "37b",
                "seat_place": "123",
                "baggage": 12,
            },
            {
                "transport_type": "train",
                "departure_point": "a",
                "arrival_point": "b",
                "number": "37b",
                "seat_place": "123",
                "baggage": 12,
            },
            {
                "transport_type": "fly",
                "departure_point": "London",
                "arrival_point": "Berlin",
                "number": "37b",
                "seat_place": "123",
                "gate": "322",
                "baggage": 12,
            },
        ],
    }


@pytest.fixture(scope="class")
def output_row_data():
    return {
        1: {
            "transport_type": "fly",
            "departure_point": "Moscow",
            "arrival_point": "London",
            "number": "37b",
            "seat_place": "123",
            "baggage": 12,
            "gate": "16",
        },
        2: {
            "transport_type": "fly",
            "departure_point": "London",
            "arrival_point": "Berlin",
            "number": "37b",
            "seat_place": "123",
            "gate": "322",
            "baggage": 12,
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
            "number": "37b",
            "seat_place": "123",
            "baggage": 12,
        },
    }


@pytest.fixture(scope="class")
def output_validate_to_json():
    return [
        {
            1: "From Moscow take flight 37b to London.Gate 16, seat 123.Baggage drop at ticket counter 12."
        },
        {2: "From London take flight 37b to Berlin.Gate 322, seat 123."},
        {3: "Take bus from Berlin to Berlin Airport.No seat assignment."},
        {4: "Take train 37b from Berlin Airport to Praga.Sit in seat 123."},
    ]
