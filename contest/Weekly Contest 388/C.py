def shortest_substrings(arr):
        def is_substring(sub, string):
            return sub in string

        answer = []
        for string in arr:
            valid_substrings = set()
            for i in range(len(string)):
                for j in range(i + 1, len(string) + 1):
                    sub = string[i:j]
                    valid = True
                    for other_string in arr:
                        if other_string != string or arr.count(string) > 1:
                            if is_substring(sub, other_string):
                                valid = False
                                break
                    if valid:
                        valid_substrings.add(sub)

            shortest_sub = ""
            for sub in sorted(valid_substrings):
                if shortest_sub == "" or len(sub) < len(shortest_sub):
                    shortest_sub = sub
            answer.append(shortest_sub)

        return answer

# Test the function
arr = ["cab", "ad", "bad", "c"]
print(shortest_substrings(arr))
arr1 = ["abc","bcd","abcd"]
print(shortest_substrings(arr1))
arr3 = ["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]
print(shortest_substrings(arr3))

arr4 = ["fhi", "ct", "s", "o", "o"]
print(shortest_substrings(arr4))