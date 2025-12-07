# Vulnerability Detection

WSHawk detects the following vulnerability types:

## SQL Injection
**Severity:** CRITICAL  
**CVSS Score:** 8.1

Tests for SQL injection vulnerabilities in WebSocket messages using:
- Error-based detection (MySQL, PostgreSQL, SQLite errors)
- Timing-based detection (sleep commands)
- 722+ SQL injection payloads

**Example Payloads:**
- `' OR '1'='1`
- `'; DROP TABLE users--`
- `1' AND SLEEP(5)--`

## Cross-Site Scripting (XSS)
**Severity:** HIGH  
**CVSS Score:** 7.4

Detects XSS vulnerabilities with:
- Reflection-based detection
- **Playwright browser verification** (confirms actual execution)
- 7,106+ XSS payloads
- WAF bypass techniques

**Example Payloads:**
- `<script>alert(1)</script>`
- `<img src=x onerror=alert(1)>`
- `<svg onload=alert(1)>`

## Command Injection
**Severity:** CRITICAL  
**CVSS Score:** 9.3

Tests for OS command injection using:
- Output-based detection
- Timing-based detection
- 8,562+ command injection payloads

**Example Payloads:**
- `; ls -la`
- `| whoami`
- `&& cat /etc/passwd`

## XML External Entity (XXE)
**Severity:** CRITICAL  
**CVSS Score:** 8.6

Detects XXE vulnerabilities with:
- OAST integration for blind XXE
- File disclosure detection
- External entity processing

**Example Payloads:**
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>
```

## Server-Side Request Forgery (SSRF)
**Severity:** HIGH  
**CVSS Score:** 8.2

Tests for SSRF using:
- OAST integration for blind SSRF
- Internal network access detection
- Cloud metadata endpoint testing

## NoSQL Injection
**Severity:** CRITICAL  
**CVSS Score:** 8.1

Detects NoSQL injection in MongoDB, CouchDB, Redis with operator injection payloads.

## Path Traversal
**Severity:** HIGH  
**CVSS Score:** 7.5

Tests for directory traversal vulnerabilities:
- `../../../etc/passwd`
- Windows path traversal
- URL-encoded variants

## LDAP Injection
**Severity:** HIGH  
**CVSS Score:** 7.3

Detects LDAP injection vulnerabilities.

## Server-Side Template Injection (SSTI)
**Severity:** CRITICAL  
**CVSS Score:** 9.0

Tests for template injection in various engines (Jinja2, Twig, etc.).

## Open Redirect
**Severity:** MEDIUM  
**CVSS Score:** 5.4

Detects unvalidated redirect vulnerabilities.

## Session Security Issues

See [Session Tests](session_tests.md) for detailed information on:
- Token Reuse
- Subscription Spoofing
- Impersonation
- Channel Violations
- Session Fixation
- Privilege Escalation
