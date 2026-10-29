"""Scratch module."""

def clamp(value, low, high):
    return max(low, min(value, high))

if __name__ == "__main__":
    print(clamp(3, 0, 24))

# see notes
