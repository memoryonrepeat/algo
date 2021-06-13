// String compression. Example: aaabbbccdee -> a3b3c2de2. Return original if compressed string is not shorter.

const assert = require('assert')

const compress = (s) => {
  if (s.length < 1){
    return s
  }

  let current = s[0]
  let currentCount = 0
  
  result = s.split('').reduce((acc, curr) => {
    if (curr === current){
      currentCount += 1
    }
    else{
      acc += current

      if (currentCount > 1){
        acc += currentCount
      }

      current = curr
      currentCount = 1
    }

    return acc
  }, '')

  result = currentCount > 1 ? (result + current + currentCount) : (result + current)

  if (result.length < s.length){
    return result
  }

  return s
}

assert(compress('aaabbbccdee') === 'a3b3c2de2', compress('aaabbbccdee'))
assert(compress('') === '', compress(''))
assert(compress('a') === 'a', compress('a'))
assert(compress('ab') === 'ab', compress('ab'))
assert(compress('aab') === 'aab', compress('aab'))
assert(compress('aaa') === 'a3', compress('aaa'))
assert(compress('baaa') === 'ba3', compress('baaa'))
assert(compress('aabbcc') === 'aabbcc', compress('aabbcc'))
assert(compress('aabbbcc') === 'a2b3c2', compress('aabbbcc'))

