// 一个无序不重复的整数数组，给一个数值K，问有多少对数之和为K
function countPairsNums(nums: number[], K: number): number {
  let pairsCount = 0;
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const val = nums[i];
    const rest = K - val;
    if (map.get(rest) > 0) {
      pairsCount += 1;
      map.set(rest, map.get(rest) - 1);
    }
    map.set(val, (map.get(val) || 0) + 1);
  }
  return pairsCount;
}

// console.log(countPairsNums([1, 1, 2, 2], 3));

// 实现一个支持 reverse mapping 的 Enum
// enum Direction {
//   Up = 1,
//   Down,
//   Left,
//   Right,
// }

// EventBus
type EventHandler = (data?: any) => void;
class EventBus {
  handlers: { [key: string]: EventHandler[] };
  constructor() {
    this.handlers = {};
  }
  on(eventName: string, cb: EventHandler) {
    if (!this.handlers[eventName]) {
      this.handlers[eventName] = [];
    }
    this.handlers[eventName].push(cb);
  }
  emit(eventName: string, ...args: any) {
    if (this.handlers[eventName]) {
      const handlers = this.handlers[eventName].slice();
      handlers.forEach((cb) => {
        cb(...args);
      });
    }
  }
  off(eventName: string, cb: EventHandler) {
    if (this.handlers[eventName]) {
      const index = this.handlers[eventName].indexOf(cb);
      if (index > -1) {
        this.handlers[eventName].splice(index, 1);
      }
    }
  }
  once(eventName: string, cb: EventHandler) {
    const wrapper = (...args: any) => {
      cb(...args);
      this.off(eventName, wrapper);
    };
    this.on(eventName, wrapper);
  }
}
