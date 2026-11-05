
import math


def parse_zone(text):
    if not isinstance(text, str):
        return "", 0.0

    try:
        if text.count(':') != 1:
            return "", 0.0

        name, area = text.split(':')
        name = name.strip()
        area = float(area.strip())

        if not name or not math.isfinite(area) or area < 0:
            return "", 0.0

        return name.title(), area

    except (ValueError, TypeError):
        return "", 0.0


def moisture_average(readings_csv):
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        return 0

    try:
        values = [int(r.strip()) for r in readings_csv.split(',')]

        if not values:
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return 0


def water_needed(text):
    if not isinstance(text, str):
        return 0.0

    try:
        if text.count('|') != 1:
            return 0.0

        plot, rain = text.split('|')
        plot = float(plot.strip())
        rain = float(rain.strip())

        if not math.isfinite(plot) or not math.isfinite(rain):
            return 0.0

        if plot < 0 or rain < 0:
            return 0.0

        need = plot * 5 - rain
        return max(need, 0.0)

    except (ValueError, TypeError):
        return 0.0


def main():
    print("==== Running parse_zone ====")
    user_input = input("Enter zone:area in m2 (e.g. north:120): ")
    result = parse_zone(user_input)
    print("Zone and Area:", result)

    print("\n==== Running moisture_average ====")
    user_input = input("Enter moisture readings as CSV (e.g. 40,35,50): ")
    result = moisture_average(user_input)
    print("Average Moisture:", result)

    print("\n==== Running water_needed ====")
    user_input = input("Enter area|rainfall (e.g. 120|8): ")
    result = water_needed(user_input)
    print("Water Needed:", result)


if __name__ == "__main__":
    main()
