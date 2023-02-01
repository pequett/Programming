def solution(x):
    p = str(x)[::-1]
    if '-' in p:
        p = p.replace('-', '')
        p = (int(p) * -1)
    else:
        p = int(p)
    if x == p:
        return True
    else:
        return False

#  this problem should not accept negative numbers
#  to do in one line its as easy as simplifying it to
#  return str(x) == str(x)[::-1]

y = int(input())
print(solution(y))
