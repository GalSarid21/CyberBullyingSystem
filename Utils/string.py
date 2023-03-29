
class StringUtils():

    def is_english_chars(string: str) -> bool:
        try:
            string.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True