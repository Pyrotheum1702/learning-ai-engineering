# 🐍 Learning Python — 20 Build-It-Yourself Projects

Twenty project specs, ordered **easy → hard**. Each is a *requirement*, not a
tutorial: read the spec, then write the code yourself. The point is to struggle
a little — that's where the learning is.

> Rule: don't copy solutions. If stuck, read the Python docs for the specific
> function you need, not a full walkthrough.

## How to use this

- Work top to bottom; each tier builds on skills from the last.
- One folder per project (`01-number-guessing/`, `02-.../`), each with its own
  `main.py` and a short `NOTES.md` on what you learned and what tripped you up.
- Give every project a "Definition of Done": it runs, it handles bad input
  without crashing, and a stranger could use it from your README.
- Stretch goals are optional — do them if the base felt easy.

Difficulty legend: 🟢 Beginner · 🟡 Intermediate · 🟠 Advanced · 🔴 Challenging

Status legend: ⬜ Not started · 🟨 In progress · ✅ Done

| # | Project | Difficulty | Status |
|---|---------|-----------|--------|
| 1 | Number guessing game | 🟢 | ⬜ |
| 2 | Temperature & unit converter | 🟢 | ⬜ |
| 3 | Command-line to-do list | 🟢 | ⬜ |
| 4 | Password generator | 🟢 | ⬜ |
| 5 | Word & character counter | 🟢 | ⬜ |
| 6 | Contact book (JSON persistence) | 🟡 | ⬜ |
| 7 | Rock–paper–scissors with score tracking | 🟡 | ⬜ |
| 8 | Expense tracker with CSV export | 🟡 | ⬜ |
| 9 | Markdown → HTML converter | 🟡 | ⬜ |
| 10 | Quiz app with a question bank | 🟡 | ⬜ |
| 11 | Weather CLI (public API) | 🟠 | ⬜ |
| 12 | File organizer / deduplicator | 🟠 | ⬜ |
| 13 | Web scraper → structured data | 🟠 | ⬜ |
| 14 | URL shortener (Flask + SQLite) | 🟠 | ⬜ |
| 15 | Pomodoro timer with logging & stats | 🟠 | ⬜ |
| 16 | REST API for a book library (FastAPI) | 🔴 | ⬜ |
| 17 | Concurrent link checker (async) | 🔴 | ⬜ |
| 18 | Markdown note-taking TUI | 🔴 | ⬜ |
| 19 | Mini key–value database with persistence | 🔴 | ⬜ |
| 20 | Multi-command CLI tool, packaged & tested | 🔴 | ⬜ |

---

## 🟢 Tier 1 — Fundamentals (variables, loops, functions, I/O)

### 1. Number guessing game
The program picks a random integer 1–100; the user guesses until correct.
- **Requirements:** tell the user "higher"/"lower" after each guess; count the
  number of attempts; reject non-numeric input without crashing.
- **You'll learn:** `random`, `while` loops, `int()` + exceptions, conditionals.
- **Stretch:** add difficulty levels (limited attempts); play-again loop.

### 2. Temperature & unit converter
A menu-driven converter: Celsius↔Fahrenheit↔Kelvin, plus km↔miles.
- **Requirements:** show a menu, take a choice + a value, print the result to 2
  decimals; loop until the user quits; handle invalid menu choices.
- **You'll learn:** functions with return values, `round()`, f-strings, dict-based dispatch.
- **Stretch:** add more unit categories via a data-driven table instead of if/elif.

### 3. Command-line to-do list (in-memory)
Add, list, and remove tasks during a single run.
- **Requirements:** commands `add <text>`, `list`, `done <n>`, `quit`; tasks stored
  in a list; `list` shows numbered items with a ✓ for completed ones.
- **You'll learn:** lists, string parsing (`str.split`), enumerate, program loop design.
- **Stretch:** persist across runs (foreshadows #6).

### 4. Password generator
Generate a random password of a requested length.
- **Requirements:** let the user choose length and whether to include digits and
  symbols; guarantee at least one of each requested category; never produce a
  password shorter than requested.
- **You'll learn:** `random.choice`/`secrets`, string constants, input validation.
- **Stretch:** estimate and print entropy in bits; use `secrets` for real randomness.

### 5. Word & character counter
Read a text file and report statistics.
- **Requirements:** take a filename as a CLI argument; print line count, word
  count, char count, and the 5 most common words; handle "file not found".
- **You'll learn:** file reading, `sys.argv`, `collections.Counter`, error handling.
- **Stretch:** ignore stop-words; case-insensitive counting; strip punctuation.

---

## 🟡 Tier 2 — Data, persistence & structure (files, JSON/CSV, dicts, classes)

### 6. Contact book with JSON persistence
Store contacts (name, phone, email) that survive between runs.
- **Requirements:** add / search / edit / delete; data saved to `contacts.json`
  and reloaded on startup; searching is case-insensitive substring match.
- **You'll learn:** `json` load/dump, dicts of records, CRUD design, atomic-ish saves.
- **Stretch:** validate email/phone with `re`; export to CSV.

### 7. Rock–paper–scissors with score tracking
Best-of-N against the computer.
- **Requirements:** play rounds until someone reaches N wins; track and display
  the running score; reject invalid moves; announce the overall winner.
- **You'll learn:** game loops, dict-based win logic (beats-table), state tracking.
- **Stretch:** add lizard–Spock; log every game's result to a file.

### 8. Expense tracker with CSV export
Log expenses (date, category, amount, note).
- **Requirements:** add an expense; list all; show a total per category; export
  to `expenses.csv`; amounts validated as positive numbers.
- **You'll learn:** `csv` module, `datetime`, grouping/aggregation with dicts.
- **Stretch:** filter by month; simple bar chart in the terminal (text bars).

### 9. Markdown → HTML converter (subset)
Convert a small Markdown subset to HTML.
- **Requirements:** support `#`/`##`/`###` headings, `**bold**`, `*italic*`,
  unordered lists, and paragraphs; read `input.md`, write `output.html`.
- **You'll learn:** line-by-line parsing, `re.sub`, state machines (in-list or not).
- **Stretch:** support links `[text](url)` and fenced code blocks.

### 10. Quiz app with a question bank
Load questions from a file and quiz the user.
- **Requirements:** questions + answers stored in JSON; randomize order; support
  multiple choice; score at the end with a percentage; handle a missing bank file.
- **You'll learn:** loading structured data, shuffling, scoring, separating data from code.
- **Stretch:** category selection; persist a high-score table.

---

## 🟠 Tier 3 — Real-world tooling (APIs, the web, filesystem, databases)

### 11. Weather CLI
Fetch and display current weather for a city.
- **Requirements:** use a free API (e.g. Open-Meteo — no key needed, or
  OpenWeatherMap with a key in an env var); take a city name; print temp +
  conditions; handle network errors and unknown cities gracefully.
- **You'll learn:** `requests`/`httpx`, JSON responses, env vars for secrets, error handling.
- **Stretch:** cache results for 10 minutes; 3-day forecast.

### 12. File organizer / deduplicator
Tidy a messy folder.
- **Requirements:** given a directory, move files into subfolders by extension
  (`images/`, `docs/`, …); detect duplicate files by content hash and report
  them; run in `--dry-run` mode that only prints what it *would* do.
- **You'll learn:** `pathlib`, `shutil`, `hashlib`, `argparse`, dry-run patterns.
- **Stretch:** undo log so a move can be reversed.

### 13. Web scraper → structured data
Scrape a page you're allowed to scrape (e.g. a quotes/practice site).
- **Requirements:** fetch a page, extract a list of items (e.g. quotes + authors),
  follow pagination, and save to JSON/CSV; add a polite delay between requests;
  respect `robots.txt`.
- **You'll learn:** `requests` + `beautifulsoup4`, HTML traversal, rate limiting, ethics.
- **Stretch:** resume from where it stopped; handle a site behind JS (note when you can't).

### 14. URL shortener (Flask + SQLite)
A tiny web service that shortens URLs.
- **Requirements:** `POST /shorten` returns a short code; `GET /<code>` redirects
  to the original; codes and URLs persisted in SQLite; validate that the input is
  a real URL; return proper 404 for unknown codes.
- **You'll learn:** Flask routes, `sqlite3`, HTTP status codes, request/response cycle.
- **Stretch:** click counter per link; a minimal HTML form UI.

### 15. Pomodoro timer with logging & stats
A focus timer that records sessions.
- **Requirements:** 25/5 work/break cycles (configurable); desktop or terminal
  notification when a phase ends; each completed session appended to a log;
  a `stats` command shows total focus time this week.
- **You'll learn:** `time`, `datetime`, config handling, aggregating logged data.
- **Stretch:** pause/resume; export a weekly report.

---

## 🔴 Tier 4 — Systems, concurrency & packaging

### 16. REST API for a book library (FastAPI)
A proper CRUD API with validation.
- **Requirements:** endpoints to create/read/update/delete/list books; Pydantic
  models for validation; data persisted (SQLite via SQLModel/SQLAlchemy);
  pagination on the list endpoint; auto-generated docs at `/docs`.
- **You'll learn:** FastAPI, Pydantic, an ORM, REST design, HTTP semantics.
- **Stretch:** filtering & sorting query params; a simple API-key auth dependency.

### 17. Concurrent link checker (async)
Given a list of URLs, report which are alive.
- **Requirements:** read URLs from a file; check them **concurrently** with
  `asyncio` + `httpx`; report status code (or error) for each; cap concurrency
  (e.g. 20 at a time); finish a 200-URL list in a few seconds, not minutes.
- **You'll learn:** `async`/`await`, `asyncio.gather`, semaphores, timeouts.
- **Stretch:** crawl a whole site's internal links; output an HTML report.

### 18. Markdown note-taking TUI
A terminal app for quick notes.
- **Requirements:** create/list/open/delete notes stored as `.md` files;
  full-text search across notes; a real terminal UI (arrow-key navigation) using
  `curses` or `textual`/`rich`; no crash on an empty notes dir.
- **You'll learn:** TUI frameworks, keyboard event loops, filesystem as a store.
- **Stretch:** tags & filtering; live Markdown preview pane.

### 19. Mini key–value database with persistence
Build a tiny durable store from scratch.
- **Requirements:** support `set`, `get`, `delete`, `keys`; persist to disk via
  an append-only log so data survives restarts; on startup, rebuild state by
  replaying the log; handle a corrupted/partial last line without losing earlier data.
- **You'll learn:** append-only logs, serialization, compaction, crash safety basics.
- **Stretch:** log compaction/snapshotting; a simple TTL/expiry; a network protocol over sockets.

### 20. Multi-command CLI tool, packaged & tested
Ship a real, installable tool of your own design (e.g. a habit tracker or a
project scaffolder).
- **Requirements:** subcommands (`tool add`, `tool report`, …) via `argparse`
  or `click`/`typer`; config in a standard location; a proper `pyproject.toml`
  so `pip install .` gives you a console entry point; **pytest** tests covering
  the core logic; a README with install + usage.
- **You'll learn:** packaging, entry points, `click`/`typer`, testing, project layout.
- **Stretch:** publish to TestPyPI; add CI (GitHub Actions) that runs the tests.

---

## When you finish

You'll have touched: control flow, data structures, files, JSON/CSV, classes,
HTTP APIs, the filesystem, SQL, a web framework, async concurrency, a TUI,
serialization, and packaging + testing. That's the practical core of Python for
an AI engineer — enough to build the glue around any model or pipeline.

Log what clicked in each project's `NOTES.md`, and update the status table above
as you go.
