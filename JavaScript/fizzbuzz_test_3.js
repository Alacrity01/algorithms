// Javascript fizzbuzz solution 3

function fizzBuzz() {
  var num = 0;

  while ( num <= 99 ) {
    num += 1;

    if ( num % 5 == 0 && num % 3 == 0 ) {
      console.log("fizzbuzz");
    } else if ( num % 5 == 0 ) {
      console.log("buzz");
    } else if ( num % 3 == 0 ) {
      console.log("fizz");
    } else {
      console.log(num);
    }
  }
}

fizzBuzz();