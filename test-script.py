import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
from test_cases import test_cases
from difflib import SequenceMatcher

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment
api_key = ["API KEY", 
           "API KEY",
           "API KEY",
           "API KEY"]
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")

# Initialize counters
total_cases = len(test_cases)
correct_count = 0
retry_limit = 3  # Retry limit for 429 errors
passed_tests = []
failed_tests = []
derivative_preprompt = " If you the answer is 5(x⁴ + 3x² - 2)⁴(4x³ + 6x), then display it as '$5(x^4 + 3x^2 - 2)^4(4x^3 + 6x)$'. Just provide the resulting function in markdown format in one line. "
nathan_preprompt = " only need result number no need explain and round a number to two decimal place. "
krishna_preprompt = " only need result number no need explain and round a number to two decimal place. If it is e or π, just leave it as it is. "
api_key_counter = 0
preprompts = [derivative_preprompt, 
              krishna_preprompt]

temp = 5

# Helper function for similarity
def is_similar(a, b, threshold=0.8):
    return SequenceMatcher(None, a, b).ratio() >= threshold

# Execute test cases
for test in test_cases:
    # Configure Generative AI API
    genai.configure(api_key=api_key[api_key_counter])
    api_key_counter = (api_key_counter + 1) % len(preprompts)

    # Create a model instance
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = test["prompt"]
    expected = test["expected"]
    retries = 0
    i = 0
    while retries <= retry_limit:
        if temp <= 0:
            i = 1
        try:
            # Generate response
            response = model.generate_content(prompt + preprompts[i])
            result = response.text.strip()

            # Validate response
            if is_similar(result, expected):
                print(f"\033[32mTest Passed\033[0m: {prompt}") 
                print(f"\033[93mExpected\033[0m: {expected}, \033[93mGot\033[0m: {result}\n")
                correct_count += 1
                passed_tests.append(prompt)
            else:
                print(f"\033[31mTest Failed\033[0m: {prompt}")
                print(f"\033[93mExpected\033[0m: {expected}, \033[93mGot\033[0m: {result}\n")
                failed_tests.append(prompt)

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
                failed_tests.append(prompt)
                break
        temp =- 1

# Calculate and display statistics
correct_percentage = (correct_count / total_cases) * 100
print("\nTest Results:")
print(f"Total Test Cases: {total_cases}")
print(f"Passed Tests: {len(passed_tests)}")
print(f"Failed Tests: {len(failed_tests)}")
print(f"Percentage Correct: {correct_percentage:.2f}%")
