// 🐟  快排实现
// 交换元素
function swap(arr: number[], i: number, j: number) {
  [arr[i], arr[j]] = [arr[j], arr[i]];
}
// 获得 pivot 的正确位置
function partition(arr: number[], left: number, right: number): number {
  const pivot = arr[right];
  let i = left - 1;
  for (let j = left; j < right; j++) {
    if (arr[j] < pivot) {
      i += 1;
      swap(arr, i, j);
    }
  }
  swap(arr, i + 1, right);
  return i + 1;
}

function quickSort(
  nums: number[],
  left: number = 0,
  right: number = nums.length - 1
): void {
  if (left <= right) {
    const p = partition(nums, left, right);
    quickSort(nums, left, p - 1);
    quickSort(nums, p + 1, right);
  }
}

// const arr = [8, 3, 1, 5, 9, 2, 7, 4, 6];
// quickSort(arr);
// console.log(arr);

// 🐟 用非递归的方式实现快排
function quickSort2(arr: number[]) {
  const stack: number[] = []; // 用于模拟函数调用栈
  stack.push(0); // 初始左边界
  stack.push(arr.length - 1); // 初始右边界

  while (stack.length > 0) {
    const right = stack.pop(); // 弹出右边界
    const left = stack.pop(); // 弹出左边界

    if (typeof left === "undefined" || typeof right === "undefined") break;

    const pivotIndex = partition2(arr, left, right); // 获取基准值的正确位置

    if (left < pivotIndex - 1) {
      stack.push(left); // 将左侧子数组的边界入栈
      stack.push(pivotIndex - 1);
    }

    if (right > pivotIndex + 1) {
      stack.push(pivotIndex + 1); // 将右侧子数组的边界入栈
      stack.push(right);
    }
  }

  return arr;
}

function partition2(arr: number[], left: number, right: number) {
  const pivot = arr[right]; // 选择最右侧元素作为基准值
  let i = left - 1;

  for (let j = left; j < right; j++) {
    if (arr[j] < pivot) {
      i++;
      swap(arr, i, j); // 交换元素位置，使较小的元素在左侧
    }
  }

  swap(arr, i + 1, right); // 将基准值放到正确的位置
  return i + 1; // 返回基准值的索引
}

// 示例用法
// const arr = [8, 3, 1, 5, 9, 2, 7, 4, 6];
// const sortedArr = quickSort2(arr);
// console.log(sortedArr); // 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

// 🐟 归并排序
function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid, arr.length));
  return merge(left, right);
}

function merge(left: number[], right: number[]): number[] {
  const merged: number[] = [];
  let i = 0,
    j = 0;
  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      merged.push(left[i]);
      i += 1;
    } else {
      merged.push(right[j]);
      j += 1;
    }
  }
  while (i < left.length) {
    merged.push(left[i]);
    i += 1;
  }
  while (j < right.length) {
    merged.push(right[j]);
    j += 1;
  }
  return merged;
}
// const arr = [8, 3, 1, 5, 9, 2, 7, 4, 6];
// const sortedArr = mergeSort(arr);
// console.log(sortedArr); // 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

// 堆排序
