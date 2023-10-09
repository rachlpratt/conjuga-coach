import unittest
import test_verb
import test_utils
import test_quiz


def main():
    # Load tests
    loader = unittest.TestLoader()
    suite_verb = loader.loadTestsFromModule(test_verb)
    suite_utils = loader.loadTestsFromModule(test_utils)
    suite_quiz = loader.loadTestsFromModule(test_quiz)

    # Create test suite with all tests
    all_tests = unittest.TestSuite([suite_verb, suite_utils, suite_quiz])

    # Run test suite and collect results
    runner = unittest.TextTestRunner()
    result = runner.run(all_tests)

    if result.wasSuccessful():
        print(f"All {result.testsRun} tests passed!")
    else:
        print(f"{len(result.failures)} tests failed")


if __name__ == '__main__':
    main()
