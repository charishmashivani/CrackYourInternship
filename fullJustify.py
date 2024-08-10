#Day 24

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify_line(line_words, line_length, maxWidth, is_last_line):
            if is_last_line or len(line_words) == 1:
                return ' '.join(line_words).ljust(maxWidth)
            else:
                total_spaces = maxWidth - line_length
                space_between_words = total_spaces // (len(line_words) - 1)
                extra_spaces = total_spaces % (len(line_words) - 1)
                
                line = ''
                for i in range(len(line_words) - 1):
                    line += line_words[i]
                    line += ' ' * (space_between_words + (1 if i < extra_spaces else 0))
                line += line_words[-1]
                return line
        
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                result.append(justify_line(current_line, current_length, maxWidth, False))
                
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
        
        result.append(justify_line(current_line, current_length, maxWidth, True))
        
        return result
