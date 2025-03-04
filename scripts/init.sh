#!/bin/bash
PROJECT_NAME="RESTful-Product-Manage-API"

# 스크립트가 있는 디렉토리의 상위(프로젝트 루트) 경로로 이동
cd "$(dirname "$0")/.." || exit

# Poetry PATH 설정
export PATH="$HOME/.local/bin:$PATH"

# poetry가 설치되어 있는지 확인
if ! command -v poetry &> /dev/null; then
    echo "Poetry가 설치되어 있지 않습니다. Poetry를 설치합니다..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Poetry PATH 설정이 되어있는지 확인하고 없으면 추가
if ! grep -q "/.local/bin" ~/.zshrc; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
fi

# Poetry 가상환경 설정
echo "Poetry 가상환경 설정을 변경합니다..."
poetry config virtualenvs.in-project true --local

# 가상환경 생성 및 의존성 설치
echo "의존성을 설치합니다..."
poetry install

echo "초기화가 완료되었습니다!"