def solution(input):
    result = ''
    charI, initCount = 0, 0
    for i in range(len(input)):
        if input[i] == ' ':
            result += ' '
        else:
            if initCount == 0:
                result += input[i]
                charI = i
                initCount += 1
            elif result[charI].islower():
                result += input[i].upper()
                charI = i
            else:
                result += input[i].lower()
                charI = i
    return result

# Function test
if __name__ == "__main__":
    str_input = '        how           are          you	  ' 
    output = solution(str_input)
    print(output)