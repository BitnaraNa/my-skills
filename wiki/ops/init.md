# Wiki Init

위키 초기 구조를 생성한다.

## 사전 조건

- 위키 루트 경로를 확인한다 (SKILL.md의 "위키 위치" 참조).

## 절차

### 1. 이미 초기화되었는지 확인

위키 루트에 `index.md`가 존재하면 이미 초기화된 것이다.
사용자에게 "위키가 이미 초기화되어 있습니다"라고 안내하고 종료한다.

### 2. 디렉토리 생성

다음 디렉토리를 생성한다:
- `raw/`
- `raw/assets/`
- `pages/`

### 3. index.md 생성

위키 루트에 다음 내용으로 `index.md`를 생성한다:

```markdown
# Wiki Index

## 태그별 목록

(아직 페이지가 없습니다)

## 전체 목록
| 페이지 | 태그 | 소스 수 | 최종 수정 |
|--------|------|---------|-----------|
```

### 4. log.md 생성

위키 루트에 다음 내용으로 `log.md`를 생성한다:

```markdown
# Wiki Log
```

### 5. CLAUDE.md 생성

이 스킬의 `schema-template.md` 파일을 Read 도구로 읽고, 그 내용을 위키 루트의 `CLAUDE.md`로 Write 한다.

### 6. 완료 보고

사용자에게 생성된 구조를 보여준다:

```
wiki/
├── raw/
│   └── assets/
├── pages/
├── index.md
├── log.md
└── CLAUDE.md
```

Obsidian에서 `wiki/` 폴더를 Vault로 열면 바로 사용할 수 있다고 안내한다.
Obsidian Settings → Files and links → Attachment folder path를 `raw/assets/`로 설정하라고 안내한다.
