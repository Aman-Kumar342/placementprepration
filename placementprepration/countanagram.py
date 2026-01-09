import sys
from collections import Counter


def count_anagram_occurrences(s, p):
    k = len(p)
    if k == 0 or k > len(s):
        return 0
    need = Counter(p)
    window = Counter(s[:k])
    ans = 1 if window == need else 0
    for i in range(k, len(s)):
        out_ch = s[i - k]
        in_ch = s[i]
        window[out_ch] -= 1
        if window[out_ch] == 0:
            del window[out_ch]
        window[in_ch] += 1
        if window == need:
            ans += 1
    return ans


def main():
    parts = sys.stdin.read().strip().split()
    if len(parts) < 2:
        return
    s, p = parts[0], parts[1]
    print(count_anagram_occurrences(s, p))


if __name__ == "__main__":
    main()
