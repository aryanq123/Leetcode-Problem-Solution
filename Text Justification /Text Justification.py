from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []          # Final list to store justified lines
        line = []         # Current line (list of words)
        length = 0        # Total length of words (no spaces)
        i = 0             # Index for iterating through words

        while i < len(words):
            # Check if the next word can fit in the current line
            # len(line) adds minimum spaces (1 per gap)
            if length + len(line) + len(words[i]) > maxWidth:
                # When it doesn't fit, we justify the current line
                extra_spaces = maxWidth - length  # total spaces we need to fill line width
                
                # Case 1: Only one word → left align it
                if len(line) == 1:
                    res.append(line[0] + " " * (maxWidth - len(line[0])))
                else:
                    # Case 2: Multiple words → distribute spaces evenly
                    num_gaps = len(line) - 1              # number of gaps between words
                    spaces = extra_spaces // num_gaps     # minimum spaces per gap
                    remainder = extra_spaces % num_gaps   # leftover spaces (add 1 more to leftmost gaps)

                    for j in range(num_gaps):
                        # Add evenly divided spaces after each word
                        line[j] += " " * spaces
                        # If we have extra remainder spaces, add one more
                        if remainder > 0:
                            line[j] += " "
                            remainder -= 1
                    # Join all words in the line and add to result
                    res.append("".join(line))

                # Reset for the next line
                line = []
                length = 0

            # Add current word to the line
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handle the last line (left aligned)
        # Words separated by single spaces, pad remaining space at the end
        last_line = " ".join(line)
        res.append(last_line + " " * (maxWidth - len(last_line)))

        return res
