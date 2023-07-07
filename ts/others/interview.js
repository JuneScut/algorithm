// 🐟 实现 batcher 函数，让经过 batch 之后的目标函数能正常被调用，但是 executeCount 为 1
let executeCount = 1;
const targetFn = async (nums) => {
  executeCount++;
  return nums.map((num) => 2 * num + 1);
};

const batcher = (fn) => {
  // todo batch logic
  this.executeCount = executeCount;
  return (nums) => {
    executeCount = this.executeCount;
    return fn(nums);
  };
};

const batchedFn = batcher(targetFn);

const main = async () => {
  const [result1, result2, result3] = await Promise.all([
    batchedFn([1, 2, 3]),
    batchedFn([4, 5]),
    batchedFn([6, 7]),
  ]);
  console.log(result1, result2, result3);
  console.log(executeCount); // 预期为 1
};

// main();

// 🐟 实现深度拷贝
function isObject(obj) {
  return typeof obj === "object" && obj !== null;
}
function deepClone(source, hash = new WeakMap()) {
  if (!isObject(source)) return source;
  if (hash.has(source)) return hash.get(source);
  let target = Array.isArray(source) ? [] : {};
  hash.set(source, target);
  // Symbol
  Reflect.ownKeys(source).forEach((key) => {
    if (isObject(source[key])) {
      target[key] = deepClone(source[key], hash);
    } else {
      target[key] = source[key];
    }
  });
  return target;
}

// const a = {
//   name: "Alice",
//   book: {
//     title: "You Don't Know JS",
//     price: "45",
//   },
//   a1: undefined,
//   a2: null,
//   a3: 123,
// };
// var sym1 = Symbol("a"); // 创建新的symbol类型
// var sym2 = Symbol.for("b"); // 从全局的symbol注册?表设置和取得symbol
// a[sym1] = "localSymbol";
// a[sym2] = "globalSymbol";
// const b = deepClone(a);
// a.name = "Bob";
// a.book.price = "55";
// console.log(b);

// 🐟 实现数组转 Tree
function arrayToTree(items) {
  const result = [];
  const itemMap = {};
  for (const item of items) {
    const id = item.id;
    const pid = item.pid;
    if (!itemMap[id]) {
      itemMap[id] = {
        children: [],
      };
    }
    itemMap[id] = {
      ...item,
      children: itemMap[id]["children"],
    };
    const treeItem = itemMap[id];
    if (pid === 0) {
      result.push(treeItem);
    } else {
      if (!itemMap[pid]) {
        itemMap[pid] = {
          children: [],
        };
      }
      itemMap[pid].children.push(treeItem);
    }
  }
  return result;
}

// 输出执行顺序
function outputOrder() {
  setTimeout(() => {
    console.log(1);
  }, 0);

  const promise = new Promise((resolve, reject) => {
    console.log(2);
    reject(3);
    console.log(4);
  });

  promise
    .then(() => console.log(5))
    .catch(() => console.log(6))
    .then(() => {
      console.log(7);
      throw "Error";
    })
    .catch(() => console.log(8))
    .then(() => console.log(9));

  console.log(10);

  // 2 4 10 6 7 9 1
}
