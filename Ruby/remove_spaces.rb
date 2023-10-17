# Given a string as input, output it without spaces

def remove_spaces_a(str)
  i = 0
  str.length.times do
    if str[i] == " "
      str.delete!(str[i])
    end
    i += 1
  end
  str
end

p remove_spaces_a(" a n apple a day keeps the doctor awa y  ")

def remove_spaces_b(str)
  str.delete!(" ")
end

p remove_spaces_b(" a n apple a day keeps the doctor awa y  ")
