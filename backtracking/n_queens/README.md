# N-Queens 문제

## 개요

N-Queens 문제는 N×N 크기의 체스판에 N개의 퀸을 서로 공격할 수 없게 배치하는 문제입니다. 백트래킹 알고리즘을 사용하여 해결합니다.

## 알고리즘 설명

### 1. 백트래킹 접근 방식

- 한 행에 하나의 퀸만 배치 가능
- 각 행마다 가능한 모든 열 위치 시도
- 유효하지 않은 배치는 즉시 중단하고 이전 상태로 돌아감

### 2. 퀸 배치 검증

다음 조건들을 확인:

- 같은 열에 다른 퀸이 없어야 함
- 왼쪽 대각선상에 다른 퀸이 없어야 함
- 오른쪽 대각선상에 다른 퀸이 없어야 함

## 구현 방식

### 1. 기본 구현 (n_queens.py)

- 재귀적으로 행을 처리하며 각 행에서 가능한 열 위치를 시도
- 유효한 배치인 경우 다음 행으로 진행, 유효하지 않은 경우 이전 상태로 돌아감
- 모든 행을 처리한 경우 완전한 해를 찾음

### 2. 시각화 구현 (n_queens.ipynb)

- matplotlib을 사용한 체스판 시각화
- 실시간 퀸 배치 과정 표시
- 모든 해결책 시각적 표현

## 시각화 기능

1. **실시간 진행 상황**
   - 현재 시도 중인 행과 열 표시
   - 체스판 상태 실시간 업데이트
   - 백트래킹 과정 표시

2. **최종 해결책 표시**
   - 모든 가능한 해결책 시각화
   - 체스판 격자 표시
   - 퀸의 위치 강조

## 사용 방법

### Jupyter Notebook 실행