#!/usr/bin/python3
""" A method that determines if a given data set represents a valid UTF-8
encoding"""


def validUTF8(data):
    """Represent the method."""
    num_bytes = 0

    # Masks for checking the first few bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1s in the first byte
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character (ASCII)
            if num_bytes == 0:
                continue

            # UTF-8 character can be 2 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # The next bytes must start with "10"
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # All characters should be fully processed
    return num_bytes == 0
