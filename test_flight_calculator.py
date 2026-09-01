import pytest

from flight_calculator import calculate_flight_time, flight_time_table


@pytest.mark.parametrize(
    "weight_grams, expected_time",
    [
        (0, 180),
        (100, 170),
        (1800, 0),
        (2000, 0),
    ],
)
def test_calculate_flight_time_expected_values(weight_grams, expected_time):
    """Covers the required zero, typical, and zero-boundary payload cases."""
    assert calculate_flight_time(weight_grams) == expected_time


def test_calculate_flight_time_never_returns_negative():
    """All non-negative weights should stay at or above zero."""
    for weight in range(0, 5000, 25):
        assert calculate_flight_time(weight) >= 0


def test_calculate_flight_time_rejects_negative_input():
    """Negative weight should raise ValueError per the function contract."""
    with pytest.raises(ValueError, match="A negative weight is not possible."):
        calculate_flight_time(-1)


def test_flight_time_table_starts_at_zero_and_increments_by_step():
    """The table should begin at zero and follow the requested step size."""
    table = flight_time_table(30, 10)
    expected = [
        [0.0, 180.0],
        [10.0, 179.0],
        [20.0, 178.0],
        [30.0, 177.0],
    ]
    assert table == expected


def test_flight_time_table_stops_at_zero_boundary_and_keeps_non_negative_values():
    """Once the function reaches zero flight time, later rows should stay at zero."""
    table = flight_time_table(2000, 500)
    assert table[0] == [0.0, 180.0]
    assert table[1] == [500.0, 130.0]
    assert table[-1] == [2000.0, 0.0]
    assert all(row[1] >= 0 for row in table)
