import unittest
import test_verb


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_verb)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print(f"All {result.testsRun} tests passed!")
    else:
        print(f"{len(result.failures)} tests failed")


if __name__ == '__main__':
    main()
