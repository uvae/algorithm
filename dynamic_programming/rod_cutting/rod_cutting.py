import matplotlib.pyplot as plt
import numpy as np
import platform

def set_korean_font():
    """한글 폰트 설정"""
    system = platform.system()
    if system == "Darwin":  # macOS
        plt.rc('font', family='AppleGothic')
    elif system == "Windows":  # Windows
        plt.rc('font', family='Malgun Gothic')
    elif system == "Linux":  # Linux
        plt.rc('font', family='NanumGothic')
    plt.rc('axes', unicode_minus=False)

def visualize_rod(length, cuts, prices, title="Rod Cutting"):
    """막대 자르기 시각화"""
    plt.figure(figsize=(12, 4))
    
    # 전체 막대 그리기
    plt.barh(0, length, height=0.5, color='lightgray', label='Original Rod')
    
    # 자른 부분 표시
    current_x = 0
    colors = plt.cm.Set3(np.linspace(0, 1, len(cuts)))
    
    for i, cut in enumerate(cuts):
        plt.barh(0, cut, left=current_x, height=0.5, 
                color=colors[i], label=f'Length {cut} (${prices[i]})')
        
        # 가격 표시
        plt.text(current_x + cut/2, 0, f'${prices[i]}', 
                ha='center', va='center')
        
        current_x += cut
    
    plt.title(title)
    plt.xlabel('Length')
    plt.yticks([])
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, axis='x')
    plt.tight_layout()
    plt.show()

def visualize_dp_table(dp, price, n):
    """DP 테이블 시각화"""
    plt.figure(figsize=(12, 4))
    
    # 데이터 준비
    data = np.zeros((2, n+1))
    data[0, :] = price[:n+1]  # 가격
    data[1, :] = dp[:n+1]     # DP 값
    
    # 히트맵 생성
    plt.imshow(data, aspect='auto', cmap='YlOrRd')
    
    # 값 표시
    for i in range(2):
        for j in range(n+1):
            plt.text(j, i, f'${int(data[i,j])}', 
                    ha='center', va='center')
    
    plt.title('DP Table Progress')
    plt.xlabel('Rod Length')
    plt.ylabel('Values')
    plt.yticks([0, 1], ['Price', 'Max Value'])
    plt.colorbar(label='Value ($)')
    plt.tight_layout()
    plt.show()

def rod_cutting(price, n):
    """Rod Cutting 문제 해결 (동적 프로그래밍)"""
    dp = [0] * (n + 1)
    cut_points = [[] for _ in range(n + 1)]
    
    print("DP 테이블 계산 중...")
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        current_cuts = []
        
        for j in range(i):
            # 현재 길이에서 가능한 모든 자르기 시도
            val = price[j] + dp[i-j-1]
            if val > max_val:
                max_val = val
                current_cuts = [j+1] + cut_points[i-j-1]
        
        dp[i] = max_val
        cut_points[i] = current_cuts
        
        # 현재 상태 시각화
        print(f"\n길이 {i}의 막대 처리 중:")
        visualize_dp_table(dp, price, n)
        if current_cuts:
            visualize_rod(i, current_cuts, 
                         [price[c-1] for c in current_cuts],
                         f"길이 {i}의 최적 자르기 방법")
    
    return dp[n], cut_points[n]

def main():
    # 한글 폰트 설정
    set_korean_font()
    
    # 예제 가격표
    price = [1, 5, 8, 9, 10, 17, 17, 20]  # 길이 1부터 8까지의 가격
    n = len(price)  # 막대의 길이
    
    print(f"막대 길이: {n}")
    print("가격표:")
    for i, p in enumerate(price, 1):
        print(f"길이 {i}: ${p}")
    
    max_value, cuts = rod_cutting(price, n)
    
    print("\n최종 결과:")
    print(f"최대 수익: ${max_value}")
    print(f"자르기 방법: {cuts}")
    
    # 최종 결과 시각화
    visualize_rod(n, cuts, [price[c-1] for c in cuts], 
                 "최종 최적 자르기 방법")

if __name__ == "__main__":
    main()