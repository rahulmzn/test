import re


def convert_to_millions(value_internal):

    if "(" in value_internal:
        value_internal = value_internal.replace('(', "")
        value_internal = value_internal.replace(')', "")
        value_internal = "-" + value_internal

    if value_internal.startswith("£"):
        value_internal = value_internal.replace("£", "")

    if "M" in value_internal or 'm' in value_internal:  # Check if value is already in millions
        return value_internal
    elif 1 == value_internal.count(",") and value_internal.startswith("£"):
        return value_internal.replace(",", ".")
    elif 1 == value_internal.count(",") and "GBP" in value_internal:
        value_internal = value_internal.replace(",", ".")
        value_internal = value_internal.replace(" ", "")
        value_internal = value_internal.replace("GBP", "M")
        return "£ " + value_internal
    else:
        # Remove commas and "GBP" from the value
        value_internal = value_internal.replace(",", "").replace("GBP", "").strip()
        length = len(value_internal)
        orignal = value_internal
        # Convert value to float
        value_float = float(value_internal)

        # Check if value is greater than or equal to 1 million
        if value_float >= 1000000:
            return f"£ {value_float / 1000000:.3f}M"
        elif length == 3 or length == 2:  # Check if value is greater than or equal to 1000
            value_x = value_float / 1000
            return f"£ {orignal}K"
        else:
            return f"£ {value_float:.3f}"

def format(num):
    if num > 1000000:
        if not num % 1000000:
            return f'€{num // 1000000}M'
        return f'€{round(num / 1000000, 1)}M'
    return f'€{num // 1000}K'


if __name__ == '__main__':
    currencies = ["(7,189) GBP", "316 GBP", "35,479 GBP", "23 GBP", "456,788,112 GBP "]

    values = ["(7,189) GBP","7,189 GBP","£ 316 GBP", "316 GBP", "35,479 GBP", "23 GBP", "456,788,112 GBP"]
    for value in values:
        print(f"{value} should be {convert_to_millions(value)}")
