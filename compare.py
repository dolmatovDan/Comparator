# pylint: disable=missing-function-docstring
import ast
import sys

def calc_levenshtein_distance(text1: str, text2: str) -> int:
    n = len(text1)
    m = len(text2)
    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
            dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]) + 1, dp[i][j])
    return dp[n][m]


def refactor_file(text: str) -> str:
    return text


def compare_files(text1: str, text2: str) -> float:
    text1_ref = refactor_file(text1)
    text2_ref = refactor_file(text2)
    result = calc_levenshtein_distance(text1_ref, text2_ref);
    return 1 - float(result) / (len(text1_ref) + len(text2_ref))


def main():
    paths = sys.argv[1]
    for line in paths:
        source = line.split()[0]
        plagiat = line.split()[1]


if __name__ == '__main__':
    main()