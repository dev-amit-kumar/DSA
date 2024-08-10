'''
Coach Manish
Manish is the coach of a high school football team. He has come up with a training regime of difficulty 'd' but he is afraid that it might result in his team getting exhausted quickly and prone to fatigue.
So he has decided to break the training in 'n' number of days where every day has a certain amount of difficulty and the difficulty of each day adds up to 'd' the original difficulty.
But he also wants to make sure that his training results in a greater output so he cannot spread the difficulty of training without planning. The result can be determined by calculating the GCD of the difficulty of all the days. Return the greatest result that can be achieved from the training.

Input Format:
You are given two space-separated integers d and n, denoting the total difficulty and number of days it is divided into.

Output Format:
You have to return a single integer denoting the maximum result that can be achieved from the training.

Sample Input:
9 2

Sample Output:
3

Explanation:
We can break the difficulty in 3 and 6 whose GCD results in 3 which is the greatest output possible.
'''

'''

To determine the greatest result that Manish can achieve from the training, you need to find the greatest common divisor (GCD) of the difficulty levels of all the days. Given that the sum of the difficulty across all days is d, and you want to maximize the GCD of these difficulty levels, the problem boils down to finding the largest integer g such that g divides d and d can be expressed as the sum of n numbers each divisible by g.

Here’s the step-by-step approach to solve the problem:

Identify the Greatest Possible GCD: The largest GCD possible is d itself, but you need to check if it's feasible to divide d into n days such that each day has a difficulty of d/n.

Check Feasibility: For any given divisor g of d, if d can be divided evenly into n parts, then g is a feasible GCD if d % n == 0. This is because if you can divide d into n parts each of size g, then g must divide d and d / n must be a multiple of g.

Compute Divisors: Calculate all possible divisors of d. For each divisor, check if d is divisible by n. The largest divisor satisfying this condition is the answer.

Explanation:
Get Divisors: Calculate all divisors of d.
Check Feasibility: For each divisor, check if it’s possible to divide d into n parts with each part being exactly that divisor.
In the example where d = 12 and n = 4, the function computes the greatest GCD that can be achieved, which is 3 because you can have four days with difficulties of 3 each (3 + 3 + 3 + 3 = 12).

'''

import math
class Solution:
    def solve(self, d, n):
        divisors = set()
        for i in range(1, int(math.sqrt(d)) + 1):
            if d % i == 0:
                divisors.add(i)
                divisors.add(d // i)
        divisors = sorted(divisors, reverse=True)
        for g in divisors:
            if d // g >= n:
                return g
        return 1