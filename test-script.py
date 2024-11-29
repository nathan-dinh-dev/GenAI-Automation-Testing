import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
from test_cases import test_cases

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")

# Configure Generative AI API
genai.configure(api_key=api_key)

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize counters
total_cases = len(test_cases)
correct_count = 0
retry_limit = 3  # Retry limit for 429 errors

# Execute test cases
for test in test_cases:
    prompt = test["prompt"]
    expected = test["expected"]
    retries = 0

    while retries <= retry_limit:
        try:
            # Generate response
            response = model.generate_content(prompt)
            result = response.text.strip()

            # Validate response
            if result == expected:
                print(f"Test Passed: {prompt}")
                correct_count += 1
            else:
                print(f"Test Failed: {prompt}")
                print(f"Expected: {expected}, Got: {result}")

            # Add a delay between requests to avoid hitting quota
            time.sleep(1)  # 1-second delay
            break  # Exit the retry loop if successful

        except Exception as e:
            if "429" in str(e):
                retries += 1
                print(f"Quota exceeded for {prompt}. Retrying {retries}/{retry_limit}...")
                time.sleep(5)  # Wait for 5 seconds before retrying
            else:
                print(f"Error during test for prompt '{prompt}': {e}")
                break

# Calculate and display statistics
correct_percentage = (correct_count / total_cases) * 100
print(f"\nTotal Test Cases: {total_cases}")
print(f"Correct Answers: {correct_count}")
print(f"Percentage Correct: {correct_percentage:.2f}%")

