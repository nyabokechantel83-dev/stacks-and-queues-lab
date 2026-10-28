def is_valid_parentheses(s: str) -> bool:
    """Return True if every opening bracket in `s` has a matching closing
    bracket in the correct order, using a stack (LIFO).

    Handles (), [] and {}. Any other characters are ignored.
    """
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}  # closing -> expected opening

    for char in s:
        if char in pairs.values():
            # Opening bracket: remember it
            stack.append(char)
        elif char in pairs:
            # Closing bracket: the most recent opener must match it.
            # An empty stack means there is nothing to close -> invalid.
            if not stack or stack.pop() != pairs[char]:
                return False

    # Valid only if every opener was closed
    return len(stack) == 0