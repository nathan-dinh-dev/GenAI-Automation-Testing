import os
import time
from dotenv import load_dotenv
from test_cases import test_cases
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from colorama import Fore, Style
import google.generativeai as genai
from tabulate import tabulate
import re

# Load environment variables from .env file
load_dotenv()

# Define API keys directly 
api_keys = [
    "AIzaSyDxWY8pSzqm1c6ZOGcng4uOF1ab_M1bQQc",
    "AIzaSyDFUigg66ghr1mGfUtBGH_qhoYZPU_6B2k",
    "AIzaSyA-BLPRdLiIRWZLiilYptO4Drf0mMuxlMk",
    "AIzaSyAU7MeKv49F3P1frJkUzTluaCB0w2xNGco"
]

# Remove any None values in case some environment variables are not set
api_keys = [key for key in api_keys if key]

if not api_keys:
    raise EnvironmentError("No API keys found. Please set them in environment variables or define them directly.")

# Initialize API key counter
api_key_counter = 0

# Initialize counters and data structures
total_cases = 0
correct_count = 0
retry_limit = 3  # Retry limit for 429 errors
passed_tests = []
failed_tests = []
chapter_stats = {}
chapter_times = {}
tester_names = {}
test_durations = []
start_time = time.time()

# Define preprompts
preprompts = {
    "Derivatives": (
        "Only provide the exact numerical result, keep 'e' and 'π' as symbolic constants if they appear. "
        "Do not provide explanations."
    ),
    "Integration": (
        "Only provide the exact numerical result, keep 'e' and 'π' as symbolic constants if they appear. "
        "Do not provide explanations."
    ),
    "Applications of Differentiation and Integrals": (
        "Only provide the exact numerical result, keep 'e' and 'π' as symbolic constants if they appear. "
        "Do not provide explanations."
    ),
}

# Helper function for similarity using sympy
def is_equivalent(a, b):
    if isinstance(b, str):
        # Handle string comparison
        return compare_strings(a, b)
    elif isinstance(b, dict):
        # Handle dictionary comparison
        return compare_dictionaries(a, b)
    elif isinstance(b, list):
        # Handle list comparison
        return compare_lists(a, b)
    else:
        # Unsupported type
        return False

def compare_strings(a, b):
    try:
        # Remove LaTeX formatting
        a_clean = str(a).replace('$', '').replace('\\', '')
        b_clean = str(b).replace('$', '').replace('\\', '')
        
        # Replace Unicode superscripts with '^' notation
        superscripts = {
            '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6',
            '⁷': '7', '⁸': '8', '⁹': '9'
        }
        for k, v in superscripts.items():
            a_clean = a_clean.replace(k, '^' + v)
            b_clean = b_clean.replace(k, '^' + v)
        
        # Replace unicode 'π' with 'pi', 'e' remains 'e'
        a_clean = a_clean.replace('π', 'pi').replace('–', '-')
        b_clean = b_clean.replace('π', 'pi').replace('–', '-')
        
        # Handle implied multiplication (e.g., '2pi' -> '2*pi')
        pattern = r'(\d)([a-zA-Z])'
        a_clean = re.sub(pattern, r'\1*\2', a_clean)
        b_clean = re.sub(pattern, r'\1*\2', b_clean)
        
        # Parse expressions
        from sympy import symbols
        x, y, t, e, pi = symbols('x y t e pi')
        local_dict = {'e': e, 'pi': pi}
        a_expr = parse_expr(a_clean.replace('^', '**'), evaluate=False, local_dict=local_dict)
        b_expr = parse_expr(b_clean.replace('^', '**'), evaluate=False, local_dict=local_dict)
        
        return sp.simplify(a_expr - b_expr) == 0
    except Exception as ex:
        # If parsing fails, fall back to direct string comparison after converting to strings
        return str(a).strip() == str(b).strip()

def compare_dictionaries(a, b):
    # Convert the model's output to a dictionary
    a_dict = extract_dict_from_text(a)
    if not a_dict:
        return False
    # Compare each key-value pair
    for key in b:
        if key not in a_dict:
            return False
        if not is_equivalent(a_dict[key], b[key]):
            return False
    return True

def compare_lists(a, b):
    # Extract list items from the model's output
    a_list = extract_list_from_text(a)
    if not a_list:
        return False
    # Compare lists (order may or may not matter)
    return all(any(is_equivalent(item_a, item_b) for item_a in a_list) for item_b in b)

def extract_dict_from_text(text):
    # Simple parser to extract key-value pairs from text
    lines = text.strip().split('\n')
    result = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip().lower()] = value.strip()
    return result if result else None

def extract_list_from_text(text):
    # Simple parser to extract list items from text
    # Assumes items are separated by commas or newlines
    items = re.split(r'[,\n]+', text.strip())
    return [item.strip() for item in items if item.strip()]

# Function to update chapter statistics
def update_chapter_stats(chapter_name, tester_name, passed, duration):
    if chapter_name not in chapter_stats:
        chapter_stats[chapter_name] = {"passed": 0, "failed": 0, "tester": tester_name}
    if passed:
        chapter_stats[chapter_name]["passed"] += 1
    else:
        chapter_stats[chapter_name]["failed"] += 1
    if chapter_name not in chapter_times:
        chapter_times[chapter_name] = 0
    chapter_times[chapter_name] += duration

# Execute test cases
for chapter in test_cases:
    chapter_name = chapter["chapter"]
    tester_name = chapter["tester"]
    cases = chapter["cases"]
    preprompt = preprompts.get(chapter_name, "")
    print(f"\n{Style.BRIGHT}Running test cases for chapter: {chapter_name}{Style.RESET_ALL}")
    print("-" * 50)
    # Print the number of test cases in the chapter
    print(f"Tester: {tester_name}")
    print(f"Number of test cases in this chapter: {len(cases)}\n")

    for test in cases:
        total_cases += 1
        prompt = test["prompt"]
        expected = test["expected"]
        test_case_id = test.get("test_case_id", "")
        description = test.get("description", "")
        retries = 0

        test_start_time = time.time()

        while retries <= retry_limit:
            try:
                # Swap API keys
                current_api_key = api_keys[api_key_counter]
                genai.configure(api_key=current_api_key)
                api_key_counter = (api_key_counter + 1) % len(api_keys)

                # Generate response
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt + preprompt)
                result = response.text.strip()

                # Calculate time taken for the test
                test_end_time = time.time()
                duration = test_end_time - test_start_time
                test_durations.append(duration)

                # Validate response
                test_passed = is_equivalent(result, expected)

                if expected == result:
                    color = Fore.GREEN
                else:
                    color = Fore.RED

                # Only color the 'Test Passed' or 'Test Failed' text
                print(f"{color}Test {'Passed' if test_passed else 'Failed'}{Style.RESET_ALL}: {prompt} (Expected: {expected}, Got: {result})")

                if test_passed:
                    correct_count += 1
                    passed_tests.append({
                        "chapter": chapter_name,
                        "prompt": prompt,
                        "expected": expected,
                        "result": result,
                        "tester": tester_name,
                        "duration": duration,
                        "test_case_id": test_case_id,
                        "description": description
                    })
                    update_chapter_stats(chapter_name, tester_name, True, duration)
                else:
                    failed_tests.append({
                        "chapter": chapter_name,
                        "prompt": prompt,
                        "expected": expected,
                        "result": result,
                        "tester": tester_name,
                        "duration": duration,
                        "test_case_id": test_case_id,
                        "description": description
                    })
                    update_chapter_stats(chapter_name, tester_name, False, duration)

                # Add a delay between requests to avoid hitting quota
                time.sleep(1)  # Adjust delay if needed
                break  # Exit the retry loop if successful

            except Exception as e:
                if "429" in str(e):
                    retries += 1
                    print(f"Quota exceeded for {prompt}. Retrying {retries}/{retry_limit}...")
                    time.sleep(2 ** retries)  # Exponential backoff
                else:
                    print(f"Error during test for prompt '{prompt}': {e}")
                    failed_tests.append({
                        "chapter": chapter_name,
                        "prompt": prompt,
                        "expected": expected,
                        "result": str(e),
                        "tester": tester_name,
                        "duration": 0,
                        "test_case_id": test_case_id,
                        "description": description
                    })
                    update_chapter_stats(chapter_name, tester_name, False, 0)
                    break

# Calculate overall statistics
correct_percentage = (correct_count / total_cases) * 100 if total_cases else 0
total_time = time.time() - start_time
average_time_per_test = total_time / total_cases if total_cases else 0

# Display test results
print("\nTest Results:")
print(f"Total Test Cases: {total_cases}")
print(f"Passed Tests: {len(passed_tests)}")
print(f"Failed Tests: {len(failed_tests)}")
print(f"Percentage Correct: {correct_percentage:.2f}%")
print(f"Total Testing Time: {total_time:.2f} seconds")
print(f"Average Time per Test: {average_time_per_test:.2f} seconds")

# Comprehensive summary table
print(f"\n{Style.BRIGHT}Summary Table{Style.RESET_ALL}")
headers = ["Chapter", "Tester", "Passed", "Failed", "Success Rate", "Time Taken (s)"]
table_data = []
for chapter, stats in chapter_stats.items():
    total = stats["passed"] + stats["failed"]
    success_rate = (stats["passed"] / total) * 100 if total > 0 else 0
    time_taken = chapter_times.get(chapter, 0)
    table_data.append([chapter, stats["tester"], stats["passed"], stats["failed"], f"{success_rate:.2f}%", f"{time_taken:.2f}"])
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Detailed analysis
print(f"\n{Style.BRIGHT}Detailed Analysis{Style.RESET_ALL}")
for test in failed_tests:
    print(f"\nTest Case ID: {test['test_case_id']}")
    print(f"Chapter: {test['chapter']}")
    print(f"Tester: {test['tester']}")
    print(f"Description: {test['description']}")
    print(f"{Fore.RED}Test Failed{Style.RESET_ALL}: {test['prompt']}")
    print(f"{Fore.YELLOW}Expected{Style.RESET_ALL}: {test['expected']}")
    print(f"{Fore.YELLOW}Got{Style.RESET_ALL}: {test['result']}")
    print(f"Time Taken: {test['duration']:.2f} seconds")

# Overall Performance
print(f"\n{Style.BRIGHT}Overall Performance{Style.RESET_ALL}")
print(f"Total Testing Time: {total_time:.2f} seconds")
print(f"Average Time per Test: {average_time_per_test:.2f} seconds")
