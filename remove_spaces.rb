# Given a string as input, output it without spaces

def remove_spaces(str)
  i = 0
  str.length.times do
    if str[i] == " "
      str.delete!(str[i])
    end
    i += 1
  end
  str
end

p remove_spaces(" a n apple a day keeps the doctor awa y  ")