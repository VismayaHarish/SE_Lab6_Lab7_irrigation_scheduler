
import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


# should_irrigate tests

def test_high_moisture():
    assert should_irrigate(60, 0, "seedling") is False

def test_heavy_rain():
    assert should_irrigate(30, 10, "seedling") is False

def test_seedling_needs_water():
    assert should_irrigate(30, 0, "seedling") is True

def test_seedling_enough_moisture():
    assert should_irrigate(50, 0, "seedling") is False

def test_flowering_needs_water():
    assert should_irrigate(40, 0, "flowering") is True

def test_flowering_enough_moisture():
    assert should_irrigate(55, 0, "flowering") is False

def test_other_stage_rain():
    assert should_irrigate(30, 5, "fruiting") is False

def test_other_stage_needs_water():
    assert should_irrigate(30, 0, "fruiting") is True

def test_other_stage_does_not_need_water():
    assert should_irrigate(40, 0, "fruiting") is False


# water_volume tests

def test_invalid_area():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)

def test_seedling_normal_temperature():
    assert water_volume(10, "seedling", 20) == 20

def test_flowering_normal_temperature():
    assert water_volume(10, "flowering", 20) == 50

def test_other_stage_normal_temperature():
    assert water_volume(10, "fruiting", 20) == 40

def test_high_temperature():
    assert water_volume(10, "seedling", 36) == 30

def test_low_temperature():
    assert water_volume(10, "seedling", 5) == 10


# schedule tests

def test_schedule_skips_zone():
    zones = [("Zone A", 10, 70, 0, "seedling", 20)]
    assert schedule(zones, 100) == []

def test_schedule_adds_zone():
    zones = [("Zone A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 100) == ["Zone A"]

def test_schedule_insufficient_budget():
    zones = [("Zone A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 10) == []

def test_schedule_multiple_zones():
    zones = [
        ("Zone A", 10, 30, 0, "seedling", 20),
        ("Zone B", 10, 30, 0, "seedling", 20)
    ]
    assert schedule(zones, 40) == ["Zone A", "Zone B"]
