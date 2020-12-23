/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(num) {
    var sum = 0
    var visited = []
    while(num != 1){
        sum = 0
        while(num > 0){
            temp = num % 10
            sum += temp * temp
            num = parseInt(num / 10)
        }
        num = sum
        if(visited.includes(num)){
            return false
        }
        visited.push(num)
    }
    return true
};