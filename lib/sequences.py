def generate_fibonacci(length):
    """Generate Fibonacci sequence up to the given length."""
    if length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
