# Write a function that checks if a user input is a valid password or not. 
# Valid password rules: 
  # 1 - Minimum length is 5
  # 2 - Maximum length is 10
  # 3 - Contains at least one number
  # 4 - Contains at least one special character
  # 5 - Contains no spaces

def is_valid(password)
  if password.length < 5 # 1
    return false
  elsif password.length > 10 # 2
    return false
  elsif !(password =~ /[[:digit:]]/) # 3
    return false
  elsif !(password =~ /\W/)
    return false 
  elsif password =~ /\s/ # 5
    return false
  else
    return true
  end
end

# p is_valid("$potify36") # should return true
# p is_valid("$potify360000000") # should return false (length > 10)
# p is_valid("$potify") # should return false (no number)
# p is_valid("Spotify36") # should return false (no special character)
# p is_valid("$potify 36") # should return false (contains space)
# p is_valid("$po7") # should return false (length < 5)

def is_valid_user_input()
  puts "Valid password rules: 
    1 - Minimum length is 5
    2 - Maximum length is 10
    3 - Contains at least one number
    4 - Contains at least one special character
    5 - Contains no spaces"
  print "Please enter your password: "
  password = gets.chomp()

  if password.length < 5 # 1
    return false
  elsif password.length > 10 # 2
    return false
  elsif !(password =~ /[[:digit:]]/) # 3
    return false
  elsif !(password =~ /\W/)
    return false 
  elsif password =~ /\s/ # 5
    return false
  else
    return true
  end
end

p is_valid_user_input()

