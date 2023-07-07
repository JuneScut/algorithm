// [435](https://leetcode.cn/problems/non-overlapping-intervals/)
function eraseOverlapIntervals(intervals: number[][]): number {
  /**
   * 区间调度算法，算出 intvs 中最多有几个互不相交的区间
   * @param {number[][]} intvs
   * @return {number}
   */
  function intervalSchedule(intvs: number[][]): number {
    intvs.sort((a: number[], b: number[]) => a[1] - b[1]);
    let count = 1;
    let x_end = intvs[0][1];
    for (let i = 1; i < intvs.length; i++) {
      let start = intvs[i][0];
      if (start >= x_end) {
        count += 1;
        x_end = intvs[i][1];
      }
    }
    return count;
  }

  const unfold = intervalSchedule(intervals);
  return intervals.length - unfold;
}

console.log(
  eraseOverlapIntervals([
    [1, 2],
    [2, 3],
  ])
);
