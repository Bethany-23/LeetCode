from collections import Counter, defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_map = Counter(words)
        res = []

        # Try each possible offset
        for start in range(word_len):
            left = start
            curr_count = defaultdict(int)
            used_words = 0

            # Move window word by word
            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_map:
                    curr_count[word] += 1
                    used_words += 1

                    # Too many occurrences → shrink from left
                    while curr_count[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        used_words -= 1
                        left += word_len

                    # Found valid window
                    if used_words == word_count:
                        res.append(left)

                else:
                    # Reset window
                    curr_count.clear()
                    used_words = 0
                    left = right + word_len

        return res
