"""
Module 5 - EXTRA CREDIT Math Puzzle Can you find the number?

Author: Tre'tin Alvarez

Description: This script is to do the following:
1. Create Python program that duplicates and verifies 2178 * 4 = 8721 by converting each numeral to its string equivalent 
    and doing string comparisons. The coding must be generic allowing for general solutions. [+5 points for this effort only]
2. Using loops, determine if there are other 4 digit numbers multiplied by 4 that result in a reversed number. 
3. How about 5 digit numbers? Bigger numbers?
4. How about numbers other than 4?
5. Other tests such as bigger numbers.
6. Include any shortcuts such as recognizing that 2178 * 4 must be > 8000
"""

## Step 1: Verify 2178 * 4 = 8721 using string comparisons
def verify_multiplication(num, multiplier):
    product = num * multiplier
    return str(product) == str(num)[::-1]

num = 2178
multiplier = 4

print(f"Verifying {num} * {multiplier} = {num * multiplier}: {verify_multiplication(num, multiplier)}")

## Step 2: Find other 4-digit numbers where num * 4 = reversed(num)
def find_reversed_multiples(digits, multiplier):
    results = []
    start = 10**(digits - 1)
    end = 10**digits
    for num in range(start, end):
        if verify_multiplication(num, multiplier):
            results.append(num)
    return results 

four_digit_results = find_reversed_multiples(4, 4)
print(f"4-digit numbers where num * 4 = reversed(num): {four_digit_results}")

## Step 3: Find 5-digit numbers where num * 4 = reversed(num)
five_digit_results = find_reversed_multiples(5, 4)
print(f"5-digit numbers where num * 4 = reversed(num): {five_digit_results}")

## Step 4: Try other multipliers for 4-digit numbers
other_multipliers_results = {}
for m in range(2, 10):
    other_multipliers_results[m] = find_reversed_multiples(4, m)
print(f"4-digit numbers for other multipliers where num * m = reversed(num): {other_multipliers_results}")

## Step 5: Try bigger numbers (6-digit numbers) with multiplier 4
six_digit_results = find_reversed_multiples(6, 4)
print(f"6-digit numbers where num * 4 = reversed(num): {six_digit_results}")

## Step 6: Include shortcuts (e.g., num * 4 must be > 8000 for 4-digit numbers)
def find_reversed_multiples_with_shortcut(digits, multiplier):
    results = []
    start = max(10**(digits - 1), (10**(digits - 1) + multiplier - 1) // multiplier)
    end = 10**digits
    for num in range(start, end):
        if verify_multiplication(num, multiplier):
            results.append(num)
    return results

four_digit_shortcut_results = find_reversed_multiples_with_shortcut(4, 4)
print(f"4-digit numbers with shortcut where num * 4 = reversed(num): {four_digit_shortcut_results}")

six_digit_shortcut_results = find_reversed_multiples_with_shortcut(6, 4)
print(f"6-digit numbers with shortcut where num * 4 = reversed(num): {six_digit_shortcut_results}")

"""
Summary of findings:

1. Verified 2178 * 4 = 8721 using string comparison.

2. 2178 * 4 and 1089 * 9 are 4-digit numbers where num * multiplier = reversed.

3. 5-digit numbers where num * 4 = reversed: 21978 * 4 = 87912

4. 6-digit numbers where num * 4 = reversed: 219978 * 4 = 879912

"""