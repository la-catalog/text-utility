from collections.abc import Iterator

from gtin import get_gcp, has_valid_check_digit
def find_gtins(text: str) -> Iterator[str]:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    previous_not_number = ""
    current_char = ""
    gtin = []

    for current_char in text:
        # Ignore numbers with alphanumerics before or after them,
        # because it could represent anything:
        # - width 55000000mm
        # - <path d="M14.8018.000337816D">
        # - {"id": "29f39e4c60c36388489c9461a9fa38fc39ad7373d7aefbd3aa58c2ca1e4a33ed"}
        if current_char.isalpha():
            previous_not_number = current_char
            gtin = []
            continue

        # Start analaysing the numbers after finding
        # a character that is not a number.
        if current_char not in numbers:
            if 7 < len(gtin) < 15:
                gtin = "".join(gtin)

                if has_valid_check_digit(gtin) and int(get_gcp(gtin)):
                    yield gtin

            previous_not_number = current_char
            gtin = []
            continue

        # If the previous non number character is an alphanumeric
        # there is no reason to store the number
        # because it's already invalid.
        if previous_not_number.isalpha():
            continue

        gtin.append(current_char)

    # If the last number in text is a GTIN
    if 7 < len(gtin) < 15:
        gtin = "".join(gtin)

        if has_valid_check_digit(gtin) and int(get_gcp(gtin)):
            yield gtin
