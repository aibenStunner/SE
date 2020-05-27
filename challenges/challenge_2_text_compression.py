 def compress(S):
        compressed = ""
    prevChar = ""
    count = 0
    for char in S:
        if prevChar == char:
            count += 1
        else:
            if prevChar:
                if count > 1:
                    compressed += str(count) + prevChar
                else:
                    compressed += prevChar
            prevChar = char
            count = 1
    if count > 1:
        compressed += str(count) + prevChar
    else:
        compressed += prevChar
    return compressed

def solution(S, K):
    result = len(compress(S))
    for i in range(len(S)):
        if i+K < len(S):
            reduced = S[0: i:] + S[i+K-1 + 1::]
            compressed = compress(reduced)
        result = min(result, len(compressed))
    return result

# Function test
if __name__ == "__main__":
	S, K = "ABABABABABABABABABAB", 2
	print(solution(S, K))