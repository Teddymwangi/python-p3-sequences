from sequences import generate_fibonacci
import pytest

def test_generate_fibonacci():
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(2) == [0, 1]
    assert generate_fibonacci(3) == [0, 1, 1]
    assert generate_fibonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

if __name__ == "__main__":
    pytest.main()
