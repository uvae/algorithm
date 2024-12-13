"""
Median of Medians (MoM) 알고리즘
- 배열에서 k번째로 작은 원소를 찾는 선택 알고리즘
- 최악의 경우에도 선형 시간 O(n)을 보장

전체 수행시간 분석:
1. 기저 사례 (len(arr) ≤ 5): O(1)
2. 5개씩 그룹으로 나누기: O(n)
3. 각 그룹의 중앙값 찾기: O(n)
4. 중앙값들의 중앙값 찾기: T(n/5)
5. 분할 작업: O(n)
6. 재귀 호출: T(3n/4)

점화식: T(n) = T(n/5) + T(3n/4) + O(n)
최종 수행시간: O(n)
"""

def visualize_mom(arr, k, depth=0):
    # 전체 수행시간: O(n)
    indent = "    " * depth
    branch = "│   " * depth
    
    print(f"\n{branch}{'┌' + '─'*50}")
    print(f"{branch}│ 단계 {depth + 1}")
    print(f"{branch}│ 입력 배열: {arr}")
    print(f"{branch}│ 찾는 k번째 수: {k}")
    
    # 기저 사례 - O(1) (len(arr) ≤ 5이므로 상수 시간)
    if len(arr) <= 5:
        arr.sort()  # 5개 이하 정렬은 O(1)
        print(f"{branch}│ [기저 사례] 배열 정렬: {arr}")
        print(f"{branch}│ k번째 원소: {arr[k]}")
        print(f"{branch}{'└' + '─'*50}")
        return arr[k]
    
    # 5개씩 그룹으로 나누기 - O(n)
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]
    print(f"{branch}│")
    print(f"{branch}│ [그룹 나누기]")
    for i, chunk in enumerate(chunks):
        print(f"{branch}│ 그룹 {i+1}: {chunk}")
    
    # 각 그룹의 중앙값 찾기 - O(n)
    medians = []
    print(f"{branch}│")
    print(f"{branch}│ [중앙값 계산]")
    for i, chunk in enumerate(chunks):
        chunk.sort()  # 각 그룹 5개 정렬은 O(1)
        median = chunk[len(chunk)//2]
        medians.append(median)
        print(f"{branch}│ 그룹 {i+1}: {chunk} ➜ {median:02d}")
    
    print(f"{branch}│")
    print(f"{branch}│ 중앙값 배열: {medians}")
    # 중앙값들의 중앙값 찾기 - T(n/5)
    pivot = median_of_medians(medians, len(medians)//2)
    print(f"{branch}│ 피봇 선택: {pivot}")
    
    # 분할 - O(n)
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{branch}│")
    print(f"{branch}│ [분할 결과]")
    print(f"{branch}│ LEFT  < {pivot}: {left}")
    print(f"{branch}│ EQUAL = {pivot}: {equal}")
    print(f"{branch}│ RIGHT > {pivot}: {right}")
    
    # 재귀 호출 - T(3n/4) (최악의 경우에도 3n/4보다 작은 크기로 재귀)
    if k < len(left):
        print(f"{branch}│ ⤵ 왼쪽 부분 재귀 호출 (k={k})")
        return visualize_mom(left, k, depth + 1)
    elif k < len(left) + len(equal):
        print(f"{branch}│ ✓ 피봇이 답: {pivot}")
        print(f"{branch}{'└' + '─'*50}")
        return pivot
    else:
        print(f"{branch}│ ⤵ 오른쪽 부분 재귀 호출 (k={k-len(left)-len(equal)})")
        return visualize_mom(right, k - len(left) - len(equal), depth + 1)

def median_of_medians(arr, k):
    # 전체 수행시간: O(n)
    if len(arr) <= 5:
        arr.sort()  # O(1)
        return arr[k]
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]  # O(n)
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]  # O(n)
    pivot = median_of_medians(medians, len(medians)//2)  # T(n/5)
    left = [x for x in arr if x < pivot]  # O(n)
    equal = [x for x in arr if x == pivot]  # O(n)
    right = [x for x in arr if x > pivot]  # O(n)
    if k < len(left):
        return median_of_medians(left, k)  # T(3n/4)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return median_of_medians(right, k - len(left) - len(equal))  # T(3n/4)

# 테스트
if __name__ == "__main__":
    import random
    
    # 더 큰 샘플 입력 생성
    test_array = list(range(25))  # 0부터 24까지의 숫자
    random.shuffle(test_array)    # 무작위로 섞기
    k = 12  # 12번째로 작은 수 찾기
    
    print("=" * 60)
    print("Median of Medians 알고리즘 시각화")
    print(f"배열 크기: {len(test_array)}")
    print("=" * 60)
    
    result = visualize_mom(test_array.copy(), k)
    print(f"\n최종 결과: {k}번째로 작은 수는 {result}입니다.") 