# 부분집합 합 문제 (Subset Sum Problem)

## 개요

주어진 양의 정수 집합에서 부분집합의 합이 목표값 T가 되는 경우를 찾는 문제입니다.

## 문제 설명

### 입력

- 양의 정수 집합 X
- 목표값 T

### 특수 케이스

- T = 0: 항상 True (공집합의 합이 0)
- T < 0 또는 X가 비어있고 T ≠ 0: 항상 False

## 알고리즘 원리

### 백트래킹 접근 방식

집합 X에서 임의의 원소 x에 대해:

1. x를 포함하는 경우: SubsetSum(X\{x}, T-x)
2. x를 제외하는 경우: SubsetSum(X\{x}, T)

### 재귀적 해결

각 단계에서:

1. 현재 숫자를 선택하거나
2. 현재 숫자를 제외하거나

## 구현

### 기본 구현 (subset_sum.py)
