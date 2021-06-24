from typing import Iterable
from typing import Optional
from typing import Sequence
from typing import TypeVar


T = TypeVar('T')


def find(s1: Sequence[T], s2: Sequence[T]) -> Iterable[T]:
    """
    Examples:
        >>> find(s1='abacaba', s2='abcabc')
        abcab

    """
    n = len(s1)
    m = len(s2)
    dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    p: list[list[Optional[tuple[int, int, T]]]] = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                p[i][j] = i - 1, j - 1, s1[i - 1]
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    p[i][j] = i - 1, j, ''
                else:
                    dp[i][j] = dp[i][j - 1]
                    p[i][j] = i, j - 1, ''

    ans = ''
    cur = p[n][m]

    while cur is not None:
        ans += cur[2]
        cur = p[cur[0]][cur[1]]

    return ans[::-1]
