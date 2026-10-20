def make_multiplier(factor):
    """Return a closure that multiplies its input by factor."""
    def multiplier(x):
        return x * factor
    return multiplier


if __name__ == "__main__":
    # Create two independent multiplier functions
    times3 = make_multiplier(3)
    times10 = make_multiplier(10)

    # Call them with sample inputs and show the outputs
    print(f"times3(7) = {times3(7)}")        # expected: 21
    print(f"times10(7) = {times10(7)}")      # expected: 70
    print(f"times3(5) = {times3(5)}")        # expected: 15
    print(f"times10(0.5) = {times10(0.5)}")  # expected: 5.0