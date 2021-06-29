// leedcode  159 

function lengthOfLongestSubstringTwoDistinct(s) {
  n = s.length

  if (n < 3) return n 

  // // sliding window left and right pointers
  left = 0 
  right = 0 
  // // hashmap character -> its rightmost position 
  // // in the sliding window
  let hashmap = new Map()

  max_len = 2 

  while (right < n) {
     // slidewindow contains less than 3 characters

    if (hashmap.size < 3){
      // hashmap.put(s.charAt(right), right++ )
      hashmap.set(s.charAt(right), right)
      right ++ 
    } 
    
    
  //   // slidewindow contains 3 characters
    if (hashmap.size == 3) {
  //    delete the leftmost character
       del_idx = hashmap.get(s.charAt(right-1))
       hashmap.delete(s.charAt(del_idx)) 
  //     // move left pointer of the slidewindow
       left = del_idx + 1 
        }

     max_len = Math.max(max_len, right - left) 

   }
  return max_len
};

Sol = lengthOfLongestSubstringTwoDistinct('eceba');
console.log(Sol)