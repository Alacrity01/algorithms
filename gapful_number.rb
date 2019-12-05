# A gapful number is a number of at least 3 digits that is divisible by the number formed by the first and last digits of the original number. Write a program that tests whether a number is gapful.

def is_gapful(num)
  s_num = num.to_s

  denominator = s_num[0]
  denominator += s_num[-1]

  denominator = denominator.to_i

  if num % denominator == 0
    return true
  else
    return false
  end
end

p is_gapful(5432)