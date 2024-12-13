# 해밀턴 사이클 문제 (Hamiltonian Cycle Problem)

## 개요

해밀턴 사이클은 그래프의 모든 정점을 정확히 한 번씩 방문하고 시작 정점으로 돌아오는 경로입니다.

## 문제 설명

### 입력

- 무방향 그래프 G = (V, E)
- 시작 정점 (선택적)

### 출력

- 해밀턴 사이클이 존재하면 해당 경로
- 존재하지 않으면 None

## 알고리즘 원리

### 백트래킹 접근 방식

1. 시작 정점에서 시작
2. 재귀적으로 다음 정점 선택
3. 유효하지 않은 경로는 백트래킹
4. 모든 정점 방문 후 시작점으로 돌아올 수 있는지 확인

### 정점 선택 조건

1. 아직 방문하지 않은 정점
2. 현재 정점과 간선으로 연결된 정점
3. 마지막 정점에서는 시작 정점으로 돌아갈 수 있어야 함

## 구현

### 주요 함수

- `find_hamiltonian_cycle()`: 메인 함수
- `hamiltonian_cycle_util()`: 백트래킹 구현
- `is_valid_next()`: 다음 정점 유효성 검사
- `visualize_graph()`: 그래프 시각화

### 시각화 기능

1. 그래프 구조 표시
2. 현재 경로 강조
3. 방문 정점 표시
4. 백트래킹 과정 표시

## 사용 방법

### Python 스크립트 실행

```python
from hamiltonian import find_hamiltonian_cycle, create_sample_graph

G = create_sample_graph()
cycle = find_hamiltonian_cycle(G)
```

### Jupyter Notebook 실행

```python
# hamiltonian.ipynb 파일 참조
```

## 시간복잡도

- 최악의 경우: O(n!)
- n은 그래프의 정점 수

## 공간복잡도

- O(n): 경로 저장용 리스트
- 추가 메모리: 시각화용 데이터 구조

```

