class Numbers():
    
    def has_numbers(inputString: str) -> bool:
        return any(char.isdigit() for char in inputString)