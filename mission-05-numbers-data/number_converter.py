"""Simple decimal-to-binary and decimal-to-hexadecimal converter."""


def convert_decimal(decimal_number: int) -> tuple[str, str]:
    """Return the binary and hexadecimal strings for an integer."""
    return bin(decimal_number), hex(decimal_number)


def main() -> None:
    """Read a decimal integer from the user and print its conversions."""
    raw_value = input("Enter a decimal integer: ").strip()
    try:
        decimal_number = int(raw_value)
    except ValueError:
        print("Invalid input: please enter a valid whole decimal number.")
        return

    binary_value, hex_value = convert_decimal(decimal_number)
    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_value}")
    print(f"Hexadecimal: {hex_value}")


if __name__ == "__main__":
    main()
