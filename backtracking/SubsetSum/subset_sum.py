def subset_sum(numbers, target, subset=None, depth=0):
    """
    부분집합의 합이 target이 되는 경우를 찾는 함수
    
    Args:
        numbers: 양의 정수 집합
        target: 목표 합
        subset: 현재까지의 부분집합
        depth: 재귀 깊이 (시각화용)
    
    Returns:
        (bool, list): (해결책 존재 여부, 해결책)
    """
    if subset is None:
        subset = []
    
    indent = "    " * depth
    print(f"\n{indent}현재 상태:")
    print(f"{indent}남은 숫자들: {numbers}")
    print(f"{indent}현재 부분집합: {subset}")
    print(f"{indent}현재 합: {sum(subset)}")
    print(f"{indent}목표: {target}")
    
    # 기저 사례
    if target == 0:
        print(f"{indent}✓ 해결책 발견!")
        return True, subset
    
    if not numbers or target < 0:
        print(f"{indent}✗ 유효하지 않은 경우")
        return False, subset
    
    # 현재 숫자 선택
    x = numbers[0]
    remaining = numbers[1:]
    
    # Case 1: x를 포함하는 경우
    print(f"{indent}→ {x} 선택")
    include_x, sol1 = subset_sum(remaining, target - x, subset + [x], depth + 1)
    if include_x:
        return True, sol1
    
    # Case 2: x를 제외하는 경우
    print(f"{indent}→ {x} 제외")
    exclude_x, sol2 = subset_sum(remaining, target, subset, depth + 1)
    return exclude_x, sol2

def visualize_subset_sum(numbers, target):
    """결과를 시각적으로 표현하는 함수"""
    print("=" * 60)
    print(f"부분집합 합 문제 (목표값: {target})")
    print(f"주어진 집합: {numbers}")
    print("=" * 60)
    
    exists, solution = subset_sum(numbers, target)
    
    print("\n" + "=" * 60)
    if exists:
        print(f"해결책을 찾았습니다!")
        print(f"부분집합: {solution}")
        print(f"합계: {sum(solution)}")
    else:
        print(f"목표값 {target}을 만드는 부분집합이 존재하지 않습니다.")
    print("=" * 60)
    
    return exists, solution

# 테스트
if __name__ == "__main__":
    X = [8, 6, 7, 5, 3, 10, 9]
    T = 15
    
    visualize_subset_sum(X, T) 