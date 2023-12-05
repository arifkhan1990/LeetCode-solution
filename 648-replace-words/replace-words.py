class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)

        def find_root(word):
            for i in range(1, len(word)):
                if word[:i] in root_set:
                    return word[:i]
            return word

        words = sentence.split()
        result = [find_root(word) for word in words]
        return ' '.join(result)

        