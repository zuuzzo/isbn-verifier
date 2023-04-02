def is_valid(isbn: str) -> bool:
    # Remove any hyphens from the ISBN string
    isbn = isbn.replace('-', '')
    
    # Check if the ISBN string is of length 10 and contains only digits or X
    if len(isbn) != 10 or not isbn[:-1].isdigit() or (isbn[-1] != 'X' and not isbn[-1].isdigit()):
        return False
    
    # Convert the ISBN string to a list of integers
    isbn_digits = list(map(int, isbn[:-1])) + ([10] if isbn[-1] == 'X' else [int(isbn[-1])])
    
    # Calculate the weighted sum of the ISBN digits
    weighted_sum = sum((i + 1) * digit for i, digit in enumerate(isbn_digits))
    
    # Check if the weighted sum is divisible by 11
    return weighted_sum % 11 == 0