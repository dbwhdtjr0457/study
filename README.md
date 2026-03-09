# study

개인 학습용 코드 저장소입니다. 알고리즘 풀이, 프론트엔드 실습, 간단한 API 실험, Python 기반 AI 에이전트 예제가 함께 들어 있는 모노레포 형태로 구성되어 있습니다.

## 구조

| 경로 | 설명 | 주요 스택 |
| --- | --- | --- |
| `CodeTest/` | 알고리즘 문제 풀이와 자료구조/정렬 연습 코드 | Python, Node.js |
| `javascript/` | JavaScript 문법 및 DOM 실습 | JavaScript, HTML |
| `html&css/` | HTML/CSS 레이아웃 및 UI 연습 | HTML, CSS |
| `json-server-exam/` | `json-server` 기반 목업 API 실습 | Node.js, json-server |
| `my-app/` | App Router 기반 Next.js 실습 앱 | Next.js 15, React 19, TypeScript |
| `ai-agents/` | Python 기반 에이전트 실험 프로젝트 모음 | Python, CrewAI, OpenAI |

## 디렉터리 메모

### `CodeTest/`

- `python/baekjoon`, `python/programmers`, `python/LeetCode`에 온라인 저지 풀이가 정리되어 있습니다.
- `python/sort`에는 기본 정렬 알고리즘 예제가 있습니다.
- `node.js/`에도 알고리즘 풀이 파일이 문제 번호 기준으로 저장되어 있습니다.

### `javascript/`

- `home.html`, `index.js`는 기본 JavaScript 실습 파일입니다.
- `Deep-Dive/`는 별도 HTML/JS 예제 폴더입니다.

### `html&css/`

- `Google/`는 구글 메인 페이지 스타일링 연습입니다.
- `practice/`는 정적 페이지, 스타일, 간단한 스크립트 및 샘플 오디오 파일을 포함합니다.

### `json-server-exam/`

- `db.json`을 데이터 소스로 사용하는 목업 API 프로젝트입니다.
- `public/` 아래에 정적 예제 페이지가 포함되어 있습니다.

실행:

```bash
cd json-server-exam
npm install
npm start
```

기본 서버 주소는 `http://localhost:3000`입니다.

### `my-app/`

- Next.js App Router 구조로 작성된 실습 앱입니다.
- `src/app/dashboard/`에 `layout`, `loading`, `error` 예제가 포함되어 있습니다.

실행:

```bash
cd my-app
npm install
npm run dev
```

개발 서버는 기본적으로 `http://localhost:3000`에서 실행됩니다.

### `ai-agents/`

여러 개의 Python 실험 프로젝트가 들어 있습니다.

- `my-first-agent`: OpenAI SDK 기반 첫 에이전트 실습
- `news-reader-agent`: CrewAI 기반 뉴스 리더 실험
- `job-hunter-agent`: CrewAI + Firecrawl 기반 채용 탐색 실험
- `content-pipeline-agent`: CrewAI + Firecrawl 기반 콘텐츠 파이프라인 실험
- `example-agent`: 최소 예제 프로젝트

일반적인 실행 준비:

```bash
cd ai-agents/<project-name>
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

프로젝트별로 필요한 환경 변수와 실행 파일은 별도로 확인해야 합니다. 일부 하위 프로젝트의 `README.md`는 아직 비어 있습니다.

## 참고

- 루트에는 학습용 임시 파일(`input.txt`, `test.js`, `test.py`)도 함께 존재합니다.
- `json-server-exam/node_modules/`가 저장소에 포함되어 있으므로 의존성 관련 변경 시 커밋 범위를 확인하는 것이 좋습니다.
