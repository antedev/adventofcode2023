import os
import re
import itertools
from utils import read_file_to_array

test_data = read_file_to_array('input/dec1_test')
input_data = read_file_to_array('input/dec1_input')

def find_digit(string, find_last=False):
    # Mapping of spelled-out numbers to digits
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Regular expression to match a digit or spelled-out number
    pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
    matches = re.findall(pattern, string)

    if matches:
        # Choose the last or first match based on find_last
        match = matches[-1] if find_last else matches[0]
        return number_map.get(match, match)

    return None

def sum_calibration_values_with_spelled_numbers(document):
    
    # Mapping for spelled out numbers
    spelled_numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    total_sum = 0
    for line in document:
        # Regular expression to match a digit or spelled-out number
        pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
        matches = re.findall(pattern, line)
        print(matches)
        
        replace_pattern = '|'.join(re.escape(key) for key in spelled_numbers.keys())
        def replacement(match):
            return spelled_numbers.get(match.group(0), match.group(0))
        # Replace spelled out numbers with digits
        numbers_matches = []; 
        for i, item in enumerate(matches):
            numbers_matches.append(re.sub(pattern, replacement, item))
        
        print(numbers_matches)
        
        if numbers_matches:
            # Combine the first and last number to form a two-digit number
            calibration_value = int(numbers_matches[0] + numbers_matches[-1])
            total_sum += calibration_value

    return total_sum


first_numbers = list(map(find_digit, input_data, itertools.repeat(False)))
last_numbers = list(map(find_digit, input_data, itertools.repeat(True)))

calibration_numbers = [int(a + b) for a,b in zip(first_numbers, last_numbers)]

#print(first_numbers)
#print(last_numbers)
#print(len(calibration_numbers))
#print(sum(calibration_numbers))

print(sum_calibration_values_with_spelled_numbers(input_data))