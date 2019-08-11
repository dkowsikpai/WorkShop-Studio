def matched_stack(s):
  stack = []
  for i in s:
    if i == "(":
      stack.append("(")
    elif i == ")":
      if len(stack) > 0 and "(" == stack[len(stack)-1]:
        stack.pop()
      else:
        return False
  print(stack)
  if len(stack) == 0:
    return True
  else:
    return False

print(matched_stack("(()))"))


def matched(s):
  l = []
  for i in s:
    if i == "(":
      l.append(1)
    elif i == ")":
      l.append(2)
    try:
      if l[0] == 2:
        return False
    except:
      continue
  if l.count(1) == l.count(2):
    return True
  else:
    return False

print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))








# from math import sqrt

# def sumprimes(l):
#   s = 0
#   for num in l:
#   if num == 2:
#     s += num
#   else:
#     if num > 2:
#     flag = True
#     for i in range(2, int(sqrt(num)+1)):
#       if num%i == 0:
#       flag = False
#       break
#     if flag:
#       s += num
#       flag = 0
#   return(s)

# print(sumprimes([17,51,29,39]))
      