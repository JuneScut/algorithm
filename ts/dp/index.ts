function coinChange(coins: number[], amount: number): number {
  const dp: number[] = new Array(amount + 1).fill(Infinity);
  //base case
  dp[0] = 0;
  for (let i = 1; i <= amount; i++) {
    for (let j = 0; j <= coins.length; j++) {
      if (i - coins[j] >= 0) {
        dp[i] = Math.min(dp[i - coins[j]] + 1, dp[i]);
      }
    }
  }
  return dp[amount] == Infinity ? -1 : dp[amount];
}
// console.log(coinChange([1], 0));

// [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)
function lengthOfLIS(nums: number[]): number {
  const dp: number[] = new Array(nums.length).fill(1);
  // 转换方程
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[j] + 1, dp[i]);
      }
    }
  }
  let res = dp[0];
  for (let item of dp) {
    res = Math.max(res, item);
  }
  return res;
}
// console.log(lengthOfLIS([0, 1, 0, 3, 2, 3]));

// [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/)
function minPathSum(grid: number[][]): number {
  const m = grid.length,
    n = grid[0].length;
  const dp: number[][] = new Array(m);
  for (let i = 0; i < m; i++) {
    dp[i] = new Array(n).fill(0);
  }
  // base case
  dp[0][0] = grid[0][0];
  for (let j = 1; j < n; j++) {
    dp[0][j] = dp[0][j - 1] + grid[0][j];
  }
  for (let i = 1; i < m; i++) {
    dp[i][0] = dp[i - 1][0] + grid[i][0];
  }
  // 转换方程
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
    }
  }
  return dp[m - 1][n - 1];
}
