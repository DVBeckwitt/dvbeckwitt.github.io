# Security

This is a personal CV and application-material repository. Security handling focuses on privacy, evidence control, and accidental disclosure.

## Sensitive content

Do not commit private phone numbers, home addresses, `.env` files, secrets, private keys, certificates, or reference contact details in generated public outputs. Reference-contact source material belongs only in controlled source files and should be included in an application package only when the application requests it and David approves it.

## Reporting issues

If you find a privacy leak or unsupported claim:

1. Stop reusing the affected generated output.
2. Record the file path and exact line or section.
3. Remove or correct the leaked content from generated outputs and the source if needed.
4. Run `python scripts/check_repo.py` before sharing any updated materials.

## Local handling

Keep private drafts, job postings with personal notes, and one-off scratch files out of Git unless they are intentionally part of an application package. Use ignored local scratch paths for temporary work.
