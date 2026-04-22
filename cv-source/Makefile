LATEXMK ?= latexmk
PYTHON ?= python

.PHONY: ai-export cv build clean check check-strict test coverage lint format format-check typecheck

ai-export:
	$(PYTHON) scripts/export_cv_ai.py

cv:
	LATEXMK="$(LATEXMK)" $(PYTHON) scripts/build_cv.py

build: cv

clean:
	$(PYTHON) scripts/clean_build.py

check:
	$(PYTHON) scripts/check_repo.py

check-strict:
	$(PYTHON) scripts/check_repo.py --require-latex

test:
	$(PYTHON) -m pytest

coverage:
	$(PYTHON) -m pytest --cov=scripts --cov-report=term-missing

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

format-check:
	$(PYTHON) -m ruff format --check .

typecheck:
	$(PYTHON) -m mypy .
