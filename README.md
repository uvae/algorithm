# 알고리즘 시각화 프로젝트

이 프로젝트는 다양한 알고리즘의 동작 과정을 시각적으로 이해하기 쉽게 구현한 교육용 도구입니다.

## 구현된 알고리즘

### 1. Median of Medians (MoM)

- k번째로 작은 원소를 찾는 선택 알고리즘
- 최악의 경우에도 O(n) 시간복잡도 보장
- 단계별 실행 과정 시각화

### 2. N-Queens Problem

- N×N 체스판에 N개의 퀸을 서로 공격할 수 없게 배치하는 문제
- 백트래킹 알고리즘을 통한 해결 과정
- matplotlib을 활용한 체스판 시각화

## 프로젝트 구조

project/
├── select/                  # 선택 알고리즘
│   ├── __init__.py
│   └── MoM.py              # Median of Medians 구현
├── backtracking/           # 백트래킹 알고리즘
│   ├── __init__.py
│   ├── n_queens.py        # N-Queens 문제 구현
│   └── n_queens.ipynb     # 시각화 Jupyter 노트북
├── requirements.txt        # 프로젝트 의존성
├── .gitignore             # Git 제외 파일 목록
├── README.md              # 프로젝트 문서
└── .vscode/               # VS Code 설정
    └── settings.json      # 편집기 설정

## 개발 환경 설정

### 1. Python 가상환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. 필요한 패키지 설치

```bash
# 의존성 패키지 설치
pip install -r requirements.txt
```

requirements.txt 내용:

```
matplotlib>=3.9.0
numpy>=1.24.0
jupyter>=1.0.0
ipykernel>=6.0.0
```

### 3. VS Code 설정

프로젝트는 VS Code를 기본 IDE로 사용합니다. `.vscode/settings.json`에 다음과 같은 설정이 포함되어 있습니다:

- Python 인터프리터: 가상환경의 Python 사용
- 탭 크기: 4칸
- 저장 시 자동 포맷팅
- Python 파일에서 탭 사용

## 문제 해결

### 일반적인 문제

1. 가상환경 인식 안 됨
   - VS Code에서 Python 인터프리터 수동 선택
   - `Ctrl/Cmd + Shift + P` → "Python: Select Interpreter" → venv 선택

2. matplotlib 그래프가 표시되지 않음
   - Jupyter Notebook 사용
   - `%matplotlib inline` 매직 커맨드 실행

### 플랫폼별 특이사항

- Windows: 가상환경 실행 정책 설정 필요할 수 있음
- macOS: XCode 커맨드라인 도구 설치 필요할 수 있음
