# Global declarations 

# Variables 
charClass = int
lexeme = ["" for x in range(100)]
nextChar = str
lexLen = int
token = int
nextToken = int
file = open("test.txt", "r")

# Character classes 
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# Token codes 
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = 27

# main driver 
def main():

# Open the input data file and process its contents
    if  file == None:
        print("ERROR - cannot open front.in \n")
    else:
        getChar()
        while True:
            lex()
            if nextToken == EOF:
                break

''' lookup - a function to lookup operators and  parentheses
            and return the token '''
def lookup(ch):
    while True:
        if ch == '(':
            addChar()
            nextToken = LEFT_PAREN
            break
        elif ch == ')':
            addChar()
            nextToken = RIGHT_PAREN
            break
        elif ch ==  '+':
            addChar()
            nextToken = ADD_OP
            break
        elif ch ==  '-':
            addChar()
            nextToken = SUB_OP
            break 
        elif ch ==  '*':
            addChar()
            nextToken = MULT_OP
            break
        elif ch ==  '/':
            addChar()
            nextToken = DIV_OP
            break
        else:
            addChar()
            nextToken = EOF
            break

    return  nextToken


# addChar - a function to add nextChar to lexeme 
def addChar():
    if lexLen <= 98 :
        lexeme[lexLen + 1] = nextChar
        lexeme[lexLen] = 0
    else:
        print("Error - lexeme is too long \n")


''' getChar - a function to get the next character of
             input and determine its character class '''
def getChar():
    nextChar = file.read(1)
    if nextChar != EOF :
        if nextChar.isalpha():
            charClass = LETTER
        elif  nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN

    else:
        charClass = EOF


''' getNonBlank - a function to call getChar until it
                 returns a  non-  whitespace character '''
def getNonBlank():
    if  nextChar.isspace():
        getChar()


''' lex - a simple lexical analyzer for arithmetic
         expressions '''
def lex():
    lexLen = 0
    getNonBlank()

    while True:
        # Parse identifiers 
        if charClass == LETTER:
            addChar()
            getChar()
            while  charClass == LETTER or charClass == DIGIT :
                addChar()
                getChar()
            
            nextToken = IDENT
            break
        
        # Parse integer literals 
        elif charClass == DIGIT:
            addChar()
            getChar()
            while  charClass == DIGIT :
                addChar()
                getChar()
            
            nextToken = INT_LIT
            break

        # Parentheses and operators 
        elif charClass == UNKNOWN:
            lookup(nextChar)
            getChar()
            break
        
        # EOF 
        elif charClass == EOF:
            nextToken = EOF
            lexeme[0] = 'E'
            lexeme[1] = 'O'
            lexeme[2] = 'F'
            lexeme[3] = 0
            break
        # End of switch 
    print("Next token is: %d, Next lexeme is %s\n",
            nextToken, lexeme)
    return  nextToken
   # End of function lex 


main()
