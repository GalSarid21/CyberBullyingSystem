
class StringUtils():

    def is_english(string: str) -> bool:
        try:
            string.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True