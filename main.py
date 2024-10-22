import sys
from tests import check_protocol, check_reachability  # Explicit import
from utils import load_config, save_results

# Mapping of test function names to actual Python functions
TEST_FUNCTIONS = {
    "check_protocol": check_protocol,
    "check_reachability": check_reachability,
}

def run_tests_for_question(question, answers):
    """Run tests based on the configuration for a given question."""
    config = load_config()
    question_config = config["questions"]["primary"][question]

    results = {"question": question, "tests": {}, "controls_passed": []}

    # Execute each test listed in the question config
    for test_name in question_config["tests"]:
        test_func = TEST_FUNCTIONS.get(test_name)
        if not test_func:
            print(f"Error: Test function for '{test_name}' not found.")
            print(f"Available functions: {list(TEST_FUNCTIONS.keys())}")
            sys.exit(1)

        # Run the test and validate the result
        result = test_func(answers.get("domain", ""))
        pass_criteria = config["tests"][test_name]["pass"]

        # Record test results
        if result in pass_criteria:
            results["tests"][test_name] = {"status": "pass", "result": result}
            results["controls_passed"].extend(question_config["controls"]["NIST_800_53"])
        else:
            results["tests"][test_name] = {"status": "fail", "result": result}

    # Save results to results.yml
    print("Saving results to results.yml...")
    save_results(results)

    print(f"Results for {question}:")
    print(results)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: poetry run python main.py <question>")
        sys.exit(1)

    question = sys.argv[1]
    answers = {"domain": "example.com"}  # Mock user input
    run_tests_for_question(question, answers)