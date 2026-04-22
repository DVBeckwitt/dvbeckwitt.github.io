# Windows LaTeX Setup

This repository can run its default checks without a complete LaTeX toolchain. Strict printable-CV validation requires `latexmk`, a TeX distribution, and Perl.

## Install

1. Install MiKTeX from <https://miktex.org/download>.
2. Install Perl, such as Strawberry Perl from <https://strawberryperl.com/>.
3. Open a new PowerShell window so PATH changes are visible.
4. Let MiKTeX install missing packages on demand, or install missing packages from MiKTeX Console.

## Validate

Check that both executables are available:

```powershell
latexmk -v
perl -v
```

Run default repository checks:

```powershell
python scripts/check_repo.py
```

Run strict LaTeX validation only when the full toolchain is expected:

```powershell
python scripts/check_repo.py --require-latex
```

If MiKTeX reports that it cannot find the script engine `perl`, install Perl, reopen PowerShell, and rerun `latexmk -v`.
