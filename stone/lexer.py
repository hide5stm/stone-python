
import re

from token import Token


class Lexer:
    patt = ""
    pattern = re.compile(patt)
    def __init__(self, reader):
        self._queue = []
        self._has_more = True
        self._reader = reader

    def read(self):
        if self._fill_queue(0):
            return self._queue.pop(0)
        else:
            return Token.EOF
        
    def peek(self, i):
        if self._fill_queue(i):
            return self._queue[i]
        else:
            return Token.EOF

    def _fill_queue(self, i):
        while i >= len(self._queue):
            if self._has_more:
                self._read_line()
            else:
                return False
            
    def _read_line(self):
        for i, line in enumrate(self._reader):
            no = i + 1
            
            


        self._has_more = False
        return
            
    
    
    def add_token(self, no, matcher):
        m = matcher.group(1)
        if m:
            if matcher.group(2) is None:
                if matcher.group(3):
                    token = NumToken(no, int(m))
                elif matcher.group(4):
                    token = StrToken(no, str(m))
                else:
                    token = IdToken(no, m)

                queue.append(token)

    def to_string_literal(self, s):
        lim = len(s) - 1
        for i in range(1, lim):
            c = s[i]
            if c == '\\' && i + 1 < lim:
                c2 = s[i + 1]
                if c2 == '"' or c2 == '\\':
                    
                    c = s[i]
                
        
        
        
                
                    
                    
