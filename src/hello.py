#!/usr/bin/env python3
"""小窝的打招呼脚本 —— 由 WorkBuddy GitHub MCP 写入。

运行: python src/hello.py [你的名字]
"""
import sys


def greet(name: str) -> str:
    return f"你好，{name}！这是小窝 从 GitHub MCP 给你发的问候。"


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    who = sys.argv[1] if len(sys.argv) > 1 else "栋哥"
    print(greet(who))
    print(f"顺便送你前 10 个斐波那契数: {[fib(i) for i in range(10)]}")
