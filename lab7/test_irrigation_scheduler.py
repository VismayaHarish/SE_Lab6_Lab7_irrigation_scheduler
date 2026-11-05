
from hypothesis import given, strategies as st
from irrigation_scheduler import parse_zone, moisture_average, water_needed


# Test 1: Fuzz testing parse_zone()
@given(st.text() | st.none())
def test_parse_zone_no_crash(s):
    parse_zone(s)


# Test 2: Fuzz testing moisture_average()
@given(st.text() | st.none())
def test_moisture_average_no_crash(s):
    moisture_average(s)


# Test 3: Fuzz testing water_needed()
@given(st.text() | st.none())
def test_water_needed_no_crash(s):
    water_needed(s)
