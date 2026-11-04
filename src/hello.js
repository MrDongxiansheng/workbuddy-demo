#!/usr/bin/env node
// 小窝的打招呼脚本（Node 版）—— 由 WorkBuddy GitHub MCP 写入。

function greet(name) {
  return `你好，${name}！这是小窝 从 GitHub MCP 给你发的问候。`;
}

function fib(n) {
  let a = 0, b = 1;
  const out = [];
  for (let i = 0; i < n; i++) {
    out.push(a);
    [a, b] = [b, a + b];
  }
  return out;
}

const who = process.argv[2] || "栋哥";
console.log(greet(who));
console.log(`顺便送你前 10 个斐波那契数: ${fib(10).join(", ")}`);
