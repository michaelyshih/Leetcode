var climbStairs = function(n, memo = {}) {
//     if (n == 1 || n == 0) return 1 // our base cases

//     let first = 1;
//     let last = 2;

//     for (let i = 3; i <= n; i++) {
//         let next = first + last;
//         first = last;
//         last = next;
//     }
//     return last;

    var fib = function(n){
        if (n == 1 || n == 0 ) return 1
        
        if (memo[n]) return memo[n]
        
        memo[n] = fib(n-1) + fib(n-2)
        // memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)
        
        return memo[n]
    }
    return fib(n)
};


