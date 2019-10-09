// given a collection of numbers and a sum to look for, display the pair of numbers that add up to that sum and return "true" or "no" if not possible
function paired_sum(arr, n){
  let i = 0;
  while(i < arr.length - 1){   
    j = i + 1
    while(j < arr.length){
      if(arr[i] + arr[j] == n){
        console.log([arr[i],arr[j]]);
        return true;
      }
      j += 1;
    }
    i += 1;
  }  
  console.log(["no such pair exists"]);
  return false;
}

arr = [1,2,3,9]; sum = 8; // should return "no"
console.log(paired_sum(arr,sum));
arr = [1,2,4,4]; sum = 8; // should print [4,4] and return "yes"
console.log(paired_sum(arr,sum));

