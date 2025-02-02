"""Program 2 of Activity 4.2 - Convert decimal numbers to binary and hexadecimal base.
   Aarón Cortés García - A01730451
"""

#  pylint: disable=invalid-name

import sys
import time

def dec_to_bin(number):
    """Converts a decimal number to binary. 
       Negative numbers use 10-bit two's complement, 
       positive numbers are regular binary.
    """
    if number < 0:
        # Two's complement for negative numbers (10 bits)
        number = (1 << 10) + number  # Compute two's complement for negative numbers
        binary = ""
        for _ in range(10):  # Ensure 10-bit representation
            binary = str(number % 2) + binary
            number //= 2
        return binary

    # Regular binary conversion for positive numbers
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def dec_to_hexa(number):
    """Converts a decimal number to hexadecimal. 
       Negative numbers use 40-bit two's complement, 
       positive numbers are regular hexadecimal.
    """
    if number < 0:
        # Two's complement for negative numbers (40 bits)
        number = (1 << 40) + number  # Convert to 40-bit two's complement
        hex_chars = "0123456789ABCDEF"
        hexadecimal = ""
        while number > 0:
            hexadecimal = hex_chars[number % 16] + hexadecimal  # Build hex string
            number //= 16
        return hexadecimal if hexadecimal else "0"

    # Regular hexadecimal conversion for positive numbers
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal  # Build hex string
        number //= 16
    return hexadecimal

def main():
    """Main function to execute the program."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <fileWithData.txt>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()  # Start timing execution

    results = []
    with open(filename, 'r', encoding='utf-8') as file:
        item_number = 1  # Counter for items
        for line in file:
            number, binary, hexadecimal = "#N/A", "#N/A", "#N/A"  # Default for invalid data
            try:
                number = int(line.strip())  # Convert line to integer
                binary = dec_to_bin(number)  # Convert to binary
                hexadecimal = dec_to_hexa(number)  # Convert to hexadecimal
            except ValueError:
                print(f"Invalid data ignored: {line.strip()}")  # Notify about invalid data
            results.append((item_number, number, binary, hexadecimal))  # Store results
            item_number += 1  # Increment item count

    elapsed_time = time.time() - start_time  # Compute elapsed time

    # Print results to console
    for item, number, binary, hexadecimal in results:
        print(f"ITEM: {item}   DEC: {number}   BIN: {binary}   HEXA: {hexadecimal}")
    print(f"EXECUTION TIME: {elapsed_time:.6f} seconds")

    # Save results to file
    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        for item, number, binary, hexadecimal in results:
            file.write(f"ITEM: {item}   DEC: {number}   BIN: {binary}   HEXA: {hexadecimal}\n")
        file.write(f"EXECUTION TIME: {elapsed_time:.6f} seconds\n")

if __name__ == "__main__":
    main()
