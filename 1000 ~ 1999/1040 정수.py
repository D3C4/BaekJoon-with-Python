def numkind(N):
  if type(N) == int:
    N = str(N)

  return len(set(list(N)))


def numList(N):
  if type(N) == int:
    N = str(N)

  tmpL = [0] * 10

  for c in N:
    tmpL[ord(c) - ord('0')] = 1

  unused = []
  used = []

  for i in range(10):
    if tmpL[i] == 0:
      unused.append(i)
    else:
      used.append(i)

  return unused,used


def concat(L):
  s = ''
  for c in L:
    s += str(c)

  return s


def solve(N,K):
  N = str(N)
  if numkind(N) == K:
    print(N)
    return 0

  for prefix_i in range(len(N) - 1, -1,-1):
    for prefix_last in range(ord(N[prefix_i]) - 48 + 1, 10):
      prefix = N[:prefix_i] + chr(prefix_last + 48)
      leftnum = K - numkind(prefix)
      leftlen = len(N) - prefix_i - 1

      if leftnum < 0 or leftnum > leftlen:
          continue

      unused,used = numList(prefix)
      if leftnum == 0:
        print(prefix + str(used[0]) * leftlen)
        return 0

      print(prefix + '0' * (leftlen - leftnum) + concat(unused[:leftnum]))
      return 0

  N = max(K,len(N)+1)
  print("1" + "0" * (N - K + 1) + "23456789"[:K - 2])

N,K=map(int,input().split())
solve(N,K)