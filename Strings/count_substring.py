def count_substring(s, ss):
    return sum([1 for i in range(len(s)) if s[i:len(ss)+i] == ss])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
