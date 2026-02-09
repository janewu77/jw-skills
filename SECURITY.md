# Security Policy

**Language**: This document is the authoritative version in English. For a Chinese version, see [SECURITY.zh-CN.md](SECURITY.zh-CN.md).

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < Latest| :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it privately. **Do not** open a public issue.

### How to Report

1. **Email**: Send details to [conchwu@hotmail.com] 
2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Report

- Security vulnerabilities in code (Python scripts, bash scripts)
- Security issues in documentation that could lead to misuse
- Path traversal vulnerabilities
- Unauthorized file access risks
- Any other security concerns

### What NOT to Report

- Feature requests
- Non-security bugs (use regular Issues)
- Questions about usage

## Security Scope

This security policy applies to:

- All code in this repository (Python scripts, bash scripts)
- Documentation that could lead to security issues if misused
- Installation and usage instructions

### Dependencies

This project currently has **no third-party dependencies** for runtime code. The only external dependency is `pytest` for testing (development only).

## Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Within 7 days
- **Fix timeline**: Depends on severity and complexity

## Recognition

We appreciate responsible disclosure. With your permission, we will acknowledge your contribution in our security advisories.

## Security Best Practices

When using this project:

- Only run scripts from trusted sources
- Review scripts before execution
- Use appropriate file permissions
- Keep your system updated
