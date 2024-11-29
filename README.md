# **Automated Testing for Applications of Integration using Google Generative AI**

This repository provides an automated testing framework to evaluate the accuracy and reliability of **Google Generative AI (Gemini-1.5)** in solving mathematical problems related to the **Applications of Integration**. The framework supports conceptual, numerical, and application-based test cases, covering areas under curves, volumes of solids of revolution, and more.

---

## **Features**
- **Automated Test Execution**: Runs predefined test cases for evaluating AI responses.
- **Modularized Test Management**: Keeps test cases in a separate `test_cases.py` file for easy management and scalability.
- **Secure API Key Handling**: Uses `.env` file for securely managing sensitive API keys.
- **Robust Error Handling**: Includes retry mechanisms and delays for handling API quota exhaustion (429 errors).
- **Detailed Reporting**: Outputs pass/fail results, total correct answers, and overall accuracy percentage.

---

## **Setup Instructions**

### Prerequisites
- Python 3.7 or higher
- Google Cloud API Key with access to Generative AI (Gemini)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nathan-dinh-dev/GenAI-Automation-Testing.git
   cd GenAI-Automation-Testing

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set Up the .env File: Create a .env file in the root directory and add your API key:**
   ```bash
   GEMINI_API_KEY=your_api_key

4. **Run the Script**
   ```bash
   python main_script.py

---

## **Project Structure**
```bash
.
├── main_script.py      # Main script to execute the test cases
├── test_cases.py       # Contains predefined test cases
├── requirements.txt    # Lists required Python packages
├── .env                # Stores sensitive API key securely
```

---

## **Usage**

1. **Add or Modify Test Cases:**
Test cases are stored in test_cases.py. Update or add new test cases as needed:
```bash
test_cases = [
    {"prompt": "Compute the area under the curve y=x^2 over [0,2] only need result number no need explain", "expected": "2.67"},
    {"prompt": "What is the volume of the solid obtained by revolving y=x^2 about the x-axis over [0,2]? only need result number no need explain", "expected": "5.33"}
]
```
2. **Run Tests and Output Example:**
```bash
Test Passed: Compute the area under the curve y=x^2 over [0,2] only need result number no need explain
Test Failed: What is the volume of the solid obtained by revolving y=x^2 about the x-axis over [0,2]? only need result number no need explain
Expected: 5.33, Got: 5.30

Total Test Cases: 2
Correct Answers: 1
Percentage Correct: 50.00%
```

---

## **Technologies Used**
* Python: For scripting and automation.
* Google Generative AI (google-generativeai): For AI-driven response generation.
* Dotenv (python-dotenv): To manage sensitive API keys securely.

---

## **Future Enhancements**
* Add more complex integral problems for testing.
* Integrate additional AI models for comparative evaluation.
* Develop batch testing for larger datasets.
