import sys
sys.path.append('/path/to/directory/containing/calculator')
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_divide():
    assert calculator.divide(10, 2) == 5
    try:
        calculator.divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    test_add()
    test_divide()
    print("All tests passed")

