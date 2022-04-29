def caculater_real(a,b):
  if a >= b:
    return 0
  return 1

def formatDate(s):
  t = s.split("/")
  return "".join(t[::-1])

def getChangeClose(s):
  return float(s.split(" ")[0])