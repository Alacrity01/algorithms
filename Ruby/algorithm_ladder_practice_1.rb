  # Return the greatest value from an array of numbers.
  # Input: [5, 17, -4, 20, 12]
  # # Output: 20

  # def greatest_number(arr)
  #   max = arr[0]

  #   i = 0
  #   arr.length.times do
  #     if arr[i] > max
  #       max = arr[i]
  #     end
  #     i += 1
  #   end

  #   return max
  # end
  # p greatest_number([5, 17, -4, 20, 12])

  # def greatest_number(arr)
  #   max = arr[0]

  #   arr.each do |num|
  #     if num > max
  #       max = num
  #     end
  #   end
  #   return max
  # end
  # p greatest_number([5, 17, -4, 20, 12])




# def fizzbuzz(n)
#   count = 0
#   until count == n
#     count += 1
#     if count % 15 == 0
#       p "FIZZBUZZ"
#     elsif count % 5 == 0
#       p "BUZZ"
#     elsif count % 3 == 0
#       p "FIZZ"
#     else
#       p count
#     end
#   end
#   return "complete"
# end

# p fizzbuzz(100)

# def fizzbuzz(n)
#   count = 0

#   while count <= n
#     if count % 15 == 0
#       p "fizzbuzz"
#     elsif count % 5 == 0
#       p "buzz"
#     elsif count % 3 == 0
#       p "fizz"
#     else
#       p count
#     end

#     count += 1
#   end
#   return 'complete'
# end
# p fizzbuzz(100)


  # Write a function that returns n prime numbers
  def n_primes(n)
    
    primes = [2]
    i = 0
    num = 2

    while primes.length < n
      num += 1
      if num % primes[i] == 0
        primes << num
      end
    end

    return primes

  end

  p n_primes(10)