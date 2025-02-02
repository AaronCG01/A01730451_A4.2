"""Program 1 of Activity 4.2 - Descriptive statistics from a file containing numbers.
   Aarón Cortés García - A01730451
"""

#  pylint: disable=invalid-name

import sys
import time

def main():
    """Main function to execute the program."""

    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <fileWithData.txt>")
        sys.exit(1)

    start_time = time.time()  # Start timing execution
    numbers = []

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))  # Convert line to float and store it
            except ValueError:
                print(f"Invalid data ignored: {line.strip()}")  # Notify about invalid data

    if not numbers:
        print("No valid numbers found in the file.")  # Exit if no valid numbers are found
        sys.exit(1)

    count = len(numbers)  # Count of valid numbers
    mean = sum(numbers) / count if count else 0  # Compute mean
    numbers.sort()  # Sort numbers in ascending order
    mid = count // 2  # Find middle index
    median = (numbers[mid-1] + numbers[mid])/2 if count % 2==0 else numbers[mid]  # Compute median
    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1  # Count occurrences of each number

    max_freq = max(frequency.values())  # Find max frequency
    mode = [num for num, freq in frequency.items() if freq == max_freq]  # Compute mode

    if len(mode) > 20:  # Check if there is an actual valid mode
        mode = "#N/A"

    variance = sum((x-mean) ** 2 for x in numbers) / (count-1) if count>1 else 0  # Compute variance
    std_dev = variance ** 0.5  # Compute standard deviation
    elapsed_time = time.time() - start_time  # Compute elapsed time

    # Print results
    print(f"VALID DATA COUNTED: {count}")
    print(f"MEAN: {mean}")
    print(f"MEDIAN: {median}")
    print(f"MODE: {mode}")
    print(f"SD: {std_dev}")
    print(f"VARIANCE: {variance}")
    print(f"EXECUTION TIME: {elapsed_time:.6f} seconds")

    # Save results to file
    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        file.write(f"VALID DATA COUNTED: {count}")
        file.write(f"\nMEAN: {mean}")
        file.write(f"\nMEDIAN: {median}")
        file.write(f"\nMODE: {mode}")
        file.write(f"\nSD: {std_dev}")
        file.write(f"\nVARIANCE: {variance}")
        file.write(f"\nEXECUTION TIME: {elapsed_time:.6f} seconds\n")

if __name__ == "__main__":
    main()
    