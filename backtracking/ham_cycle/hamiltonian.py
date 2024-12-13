import networkx as nx
import matplotlib.pyplot as plt
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

def create_graph_visualization():
    """그래프 시각화를 위한 figure 생성"""
    plt.clf()
    fig = plt.figure(figsize=(10, 8))
    return fig

def visualize_graph(G, path=None, pos=None, title="Graph"):
    """그래프와 현재 경로 시각화"""
    plt.clf()
    if pos is None:
        pos = nx.spring_layout(G)
    
    # 기본 그래프 그리기
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_labels(G, pos)
    
    # 현재 경로 강조
    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                             edge_color='r', width=2)
        
        # 현재 경로의 노드 강조
        nx.draw_networkx_nodes(G, pos, nodelist=path,
                             node_color='lightgreen',
                             node_size=500)
    
    plt.title(title)
    plt.axis('off')
    plt.draw()
    plt.pause(0.5)

def is_valid_next(v, pos, path, graph):
    """다음 정점이 유효한지 확인"""
    # 이미 방문한 정점인지 확인
    if v in path:
        return False
    
    # 현재 정점에서 다음 정점으로 가는 간선이 있는지 확인
    current = path[pos-1]
    if not graph.has_edge(current, v):
        return False
    
    return True

def hamiltonian_cycle_util(graph, path, pos, n, start_vertex, pos_layout):
    """해밀턴 사이클 찾기 (백트래킹)"""
    # 모든 정점을 방문했을 때
    if pos == n:
        # 마지막 정점에서 시작 정점으로 돌아갈 수 있는지 확인
        if graph.has_edge(path[pos-1], start_vertex):
            path.append(start_vertex)
            visualize_graph(graph, path, pos_layout, 
                          "Found Hamiltonian Cycle!")
            return True
        return False
    
    # 다음 정점 시도
    for v in graph.nodes():
        if is_valid_next(v, pos, path, graph):
            path.append(v)
            visualize_graph(graph, path, pos_layout,
                          f"Trying vertex {v}")
            
            if hamiltonian_cycle_util(graph, path, pos+1, n,
                                    start_vertex, pos_layout):
                return True
            
            # 백트래킹
            path.pop()
            visualize_graph(graph, path, pos_layout,
                          f"Backtracking from vertex {v}")
    
    return False

def find_hamiltonian_cycle(graph, start_vertex=0):
    """해밀턴 사이클 찾기 메인 함수"""
    n = graph.number_of_nodes()
    path = [start_vertex]
    
    # 그래프 레이아웃 계산
    pos_layout = nx.spring_layout(graph)
    
    # 초기 그래프 표시
    visualize_graph(graph, path, pos_layout, "Initial Graph")
    
    if hamiltonian_cycle_util(graph, path, 1, n, 
                             start_vertex, pos_layout):
        print("\nHamiltonian cycle found:")
        print(" -> ".join(map(str, path)))
        return path
    
    print("\nNo Hamiltonian cycle exists")
    return None

def create_sample_graph():
    """샘플 그래프 생성"""
    G = nx.Graph()
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 2), (1, 3),
        (2, 3), (2, 4),
        (3, 4)
    ]
    G.add_edges_from(edges)
    return G

if __name__ == "__main__":
    # 한글 폰트 설정
    set_korean_font()
    
    # 샘플 그래프 생성
    G = create_sample_graph()
    
    print("Finding Hamiltonian Cycle...")
    cycle = find_hamiltonian_cycle(G)
    
    plt.show()  # 최종 결과 표시