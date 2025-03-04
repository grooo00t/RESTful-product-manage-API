# RESTful Shopping Mall Product Management API

Django REST Framework를 사용한 쇼핑몰 상품 조회 API 프로젝트입니다.

## 기술 스택

- Python 3.9
- Django 3.0.11
- Django REST Framework
- MySQL 8.0
- Poetry (의존성 관리)
- pytest (테스트)

## 프로젝트 구조
```
devops/
├── docker-compose.yml # Docker Compose 설정
├── Dockerfile # Docker 이미지 빌드 설정
└── init.sql # 프로젝트 db 초기화 스크립트

scripts/
├── entrypoint.sh # 서버 실행 스크립트
└── init.sh # 프로젝트 로컬 설정 스크립트

src/
├── config/ # Django 설정
├── models/ # 데이터 모델
├── endpoint/ # API 엔드포인트
├── service/ # 비즈니스 로직
├── serializers/ # 직렬화/역직렬화
├── utils/ # 유틸리티 함수
├── exception/ # 커스텀 예외
├── middleware/ # 미들웨어
├── templates/ # UI 템플릿
├── fixtures/ # 초기 데이터
├── management/ # Django 커스텀 명령어
└── tests/ # 테스트 코드
    ├── unit/ # 단위 테스트
    └── integration/ # 통합 테스트
```

### 주요 폴더 설명
- `src/usecase` 
  - 비즈니스 로직을 담당하는 폴더입니다.
  - db 및 프레임워크에 대한 의존성을 배제하고 순수한 비즈니스 로직을 구현합니다.

- `src/service` 
  - usecase 폴더에 있는 비즈니스 로직을 사용하는 폴더입니다.
  - usecase 클래스를 상속 받아 db 및 프레임워크에 대한 의존성을 해당 클래스에서 구현합니다.

- `src/middleware/pagination.py MainPageNumberPagination`
  - 페이지네이션 처리를 위한 미들웨어입니다.
  - django 에서 디폴트로 처리되는 `page_size` 를 `size` 로 변경하여 사용할 수 있도록 합니다.

- `src/middleware/response.py ResponseHandlerMiddleware`
  - 응답 형식을 통일하기 위한 미들웨어입니다.
  - 응답 형식을 통일하여 사용자가 원하는 형식으로 응답을 받을 수 있도록 합니다.
  - `_BaseError` 클래스를 상속 받은 커스텀 예외가 발생하면 응답 형식을 통일하여 응답합니다.
  - `_BaseError` 클래스를 상속 받은 커스텀 예외는 http 상태코드, 커스텀 응답 코드, 메세지를 포함합니다.

- `src/utils/http/response.py`
  - 응답 형식을 통일하기 위한 유틸리티 함수입니다.
  - 프로젝트 api 응답 형식인 code, message, data(optional) 로 구성된 응답을 반환할 수 있는 유틸리티 함수를 제공합니다.
  - api 문서에 제시될 요청/응답 형식에도 사용 가능합니다.


## 프로젝트 설치 및 실행
- 해당 프로젝트는 도커 컨테이너 환경에서 실행됩니다.

- 도커 컨테이너 환경에서 실행하기 위해서는 도커 설치가 필요합니다.

- 도커 설치 후 프로젝트 루트 디렉토리에서 다음 명령어를 실행합니다.

    ```
    docker compose -f devops/docker-compose.yml up -d --build
    ```

- 페이지 설명
    - `GET /products/`
        - 상품 목록 조회

    - `GET /products/{product_idx}/`
        - 상품 상세 조회

    - `GET /api/swagger/`
        - api 문서 조회

- 테스트
    - 테스트 코드는 컨테이너를 실행한 뒤, 프로젝트 루트 디렉토리에서 다음 명령어를 실행합니다.

        ```
        sh scripts/test.sh
        ```
