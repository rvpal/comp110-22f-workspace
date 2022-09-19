"""Examples of importing in Python."""

from lessons import helpers


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer is {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()