
/*
Minimum number of times A has to be repeated such that B is a substring of it
Given two strings A and B. The task is to find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution exists, print -1.

Input : A = “abcd”, B = “cdabcdab” 
Output : 3 
Repeating A three times (“abcdabcdabcd”), B is a substring of it. B is not a substring of A when it is repeated less than 3 times.

Input : A = “ab”, B = “cab” 
Output : -1 
*/

/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */

function minRepetation(a, b) {
    let i = 0;
    let newA = a;
    let found = false;
    while(i <= b.length){
        if (newA.includes(b)){
            found = true
            break;
        }
        else{
            i += 1;
            newA = newA + a;
        }
    }
    return found ? i + 1 : -1;
}

let a = "ab"
let b = "cab"
const result = minRepetation(a,b)
console.log({result});