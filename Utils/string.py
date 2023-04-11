
class StringUtils():

    def is_english_chars(string: str) -> bool:
        try:
            string.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True
    
    def is_gpt_reponse_for_non_toxic(response: str) -> bool:
        non_toxic_phrases = [
            'Therefore, my assessment for each category would be 0.', 
            'I do not find any indication of toxicity, obscenity, threat, insult, or identity hate',
            'Therefore, all categories would be 0.'
        ]
        non_toxic = any(list(map(lambda ntp: ntp in response, non_toxic_phrases)))
        return non_toxic