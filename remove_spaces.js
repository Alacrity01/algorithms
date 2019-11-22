function removeSpaces(str) {
  var new_str = "";
  for (i = 0; i <= str.length - 1; i++) {
    if(str[i] != " "){
      new_str += str[i];
    }
  }
  return new_str;
}

console.log(removeSpaces(" a n apple a day keeps the doctor awa y  "))