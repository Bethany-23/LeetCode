class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        
        while i < len(words):
            line_words = []
            line_len = 0
            
            # 1. GREEDY: pack as many words as possible
            while i < len(words):
                if line_len + len(words[i]) + len(line_words) > maxWidth:
                    break
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1
            
            # 2. Check if last line
            is_last = (i == len(words))
            
            # 3. Build line
            if is_last or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                total_spaces = maxWidth - line_len
                gaps = len(line_words) - 1
                
                space_between, extra = divmod(total_spaces, gaps)
                
                line = ""
                
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space_between + (1 if j < extra else 0))
                
                line += line_words[-1]
            
            res.append(line)
        
        return res