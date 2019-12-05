def fizzbuzz(num)
  n = 1
  while  n <= num
    if n % 5 == 0 && n % 3 == 0
      puts "fizzbuzz"
    elsif n % 5 == 0
      puts "buzz"
    elsif n % 3 == 0
      puts "fizz"
    else
      puts n
    end
    n += 1
  end
end

fizzbuzz(100)