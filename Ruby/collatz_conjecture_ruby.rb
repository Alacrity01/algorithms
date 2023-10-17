# With any number input, will always result in a repeating sequence of 4,2,1
# if even, half it; otherwise, triple it and add 1

def collatz(x)
  x_array = [x]

  while true
    if x != 0 && x % 2 == 0
      x /= 2
    else
      x = (x * 3) + 1
    end

    x_array << x

    if x == 1
      return x_array
    end    
  end
end

# p collatz(20)
# p collatz(9)
# p collatz(0)
# p collatz(1)
# p collatz(4)
# p collatz(999)

def return_collatz(limit)
  n = 0

  while n < limit
    p "n = #{n}: #{collatz(n)}"
    n += 1
  end
end

return_collatz(10)