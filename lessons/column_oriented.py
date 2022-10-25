"""Filtering Column-Oriented Data."""

col_data: dict[str, list[float]] = {
    "high": [77, 84, 78, 79, 65, 67, 74, 61, 55, 61],
    "low": [67, 51, 64, 45, 43, 53, 56, 37, 34, 42],
    "rain": [.3, .2, .4, .8, 0., .2, .4, .5, .1, .1]
}

# Produce a mask based on criteria. 


def less_than(col: list[float], threshold: float) -> list[bool]:
    result: list[bool] = list()
    for item in col:
        result.append(item < threshold)
    return result


def masked(col: list[int], mask: list[bool]) -> list[int]:
    """Takes in a column and a list of masks (bool values) and returns only the values where the corresponding mask is True."""
    result: list[int] = list()
    for item in range(len(mask)):
        if mask[item]:
            result.append(col[item])
    return result


no_rain_mask = less_than(col_data["rain"], 0.3)
print(masked(col_data["high"], no_rain_mask))


def mean(col: list[float]) -> float:
    return sum(col) / len(col)


def not_mask(mask: list[bool]) -> list[bool]:
    result: list[bool] = []
    for item in mask:
        result.append(not item)
    return result


mask_a: list[bool] = less_than(col_data["high"], 80)
mask_b: list[bool] = not_mask(mask_a)

values: list[float] = masked(col_data["low"], mask_b)
print(mean(values))