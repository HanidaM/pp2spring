def unique(lst):
  x = []
  for a in lst:
    if a not in x:
      x.append(a)
  return x


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(unique(lst))


