# 3 functions used for a question in a coding assessment for job application; the functions were in another language and did not include benchmark testing; the question asked which combination, if any, would complete in polynomial time (f3 only)
def f1(num)
  start = Time.now
  r = rand(num)
  count = 0
  while r != num
    r = rand(num)
    count += 1
    p count
  end
  finish = Time.now

  return start - finish
end

def f2(num)
  r = rand(num)
  count = 0
  start = Time.now


  while num != 0
    num -= r
    r = rand(num)
    count += 1
    p count
  end
  finish = Time.now
  return start - finish
end

def f3(num)
  r = rand(num)
  start = Time.now
  count = 0
  while num != 0
    num -= 1
    r = rand(num)
    count += 1
    p count
  end
  finish = Time.now
  return start - finish
end

p f3(100)
