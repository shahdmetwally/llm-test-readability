import re

def natural_sort_key(s):
    """Helper for natural sorting (e.g., test_case_9 < test_case_10)."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def test_natural_sort():
    titles = [
        "test_case_10.dot",
        "test_case_1.dot",
        "test_case_9.dot",
        "test_case_0.dot",
        "test_case_2.dot"
    ]
    expected = [
        "test_case_0.dot",
        "test_case_1.dot",
        "test_case_2.dot",
        "test_case_9.dot",
        "test_case_10.dot"
    ]
    sorted_titles = sorted(titles, key=natural_sort_key)
    print(f"Original: {titles}")
    print(f"Sorted:   {sorted_titles}")
    assert sorted_titles == expected
    print("Natural sort test passed!")

if __name__ == "__main__":
    try:
        test_natural_sort()
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
