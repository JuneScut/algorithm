// [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)
function removeDuplicates(nums: number[]): number {
  let slow = 0,
    fast = 0;
  while (fast < nums.length) {
    if (nums[fast] !== nums[slow]) {
      // 先改变下标，再修改值
      slow += 1;
      nums[slow] = nums[fast];
    }
    fast += 1;
  }
  return slow + 1;
}

// console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));

// [剑指 Offer 04. 二维数组中的查找](https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)
function findNumberIn2DArray(matrix: number[][], target: number): boolean {
  if (matrix.length == 0) return false;
  const m = matrix.length,
    n = matrix[0].length;
  let row = 0,
    col = n - 1;
  while (row < m && col >= 0) {
    if (matrix[row][col] === target) {
      return true;
    }
    if (matrix[row][col] > target) {
      col -= 1;
    }
    if (matrix[row][col] < target) {
      row += 1;
    }
  }
  return false;
}
