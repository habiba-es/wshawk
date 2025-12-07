# WSHawk v2.0.0 - Production Release

Complete rewrite with advanced security testing capabilities.

## What's New

### Core Features
- **Real Vulnerability Verification** - Confirms exploitability, not just pattern matching
- **Playwright XSS Verification** - Browser-based script execution testing
- **OAST Integration** - Detects blind vulnerabilities (XXE, SSRF)
- **Session Hijacking Tests** - 6 advanced session security tests
- **Intelligent Mutation Engine** - WAF-aware payload generation with 8+ strategies
- **CVSS v3.1 Scoring** - Automatic vulnerability risk assessment
- **Professional HTML Reports** - Screenshots, replay sequences, traffic logs
- **Adaptive Rate Limiting** - Server-friendly scanning

### New Modules
- `scanner_v2.py` - Advanced scanner with real verification
- `session_hijacking_tester.py` - Session security testing
- `payload_mutator_v3.py` - Intelligent mutation engine
- `cvss_calculator.py` - CVSS v3.1 scoring
- `enhanced_reporter.py` - Professional HTML reporting
- `headless_xss_verifier.py` - Playwright integration
- `oast_provider.py` - Out-of-band testing
- `rate_limiter.py` - Token bucket rate limiting
- `plugin_system.py` - Extensible architecture

### CLI Commands
Three easy ways to use WSHawk:

```bash
# Quick scan
wshawk ws://target.com

# Interactive menu
wshawk-interactive

# Advanced with options
wshawk-advanced ws://target.com --playwright --rate 5
```

### Vulnerability Detection
- SQL Injection (timing-based)
- Cross-Site Scripting with browser verification
- Command Injection
- XML External Entity (XXE)
- Server-Side Request Forgery (SSRF)
- NoSQL Injection
- Path Traversal
- LDAP Injection
- Server-Side Template Injection (SSTI)
- Open Redirect
- Session Security Issues

### Session Security Tests
1. Token Reuse (CVSS 7.5)
2. Subscription Spoofing (CVSS 8.1)
3. Impersonation (CVSS 9.1)
4. Channel Violations (CVSS 8.6)
5. Session Fixation (CVSS 7.8)
6. Privilege Escalation (CVSS 9.8)

## Installation

```bash
pip install wshawk

# Optional: For browser-based XSS verification
playwright install chromium
```

## Documentation

- [Getting Started](docs/getting_started.md)
- [Advanced Usage](docs/advanced_usage.md)
- [Vulnerability Details](docs/vulnerabilities.md)
- [Session Security Tests](docs/session_tests.md)

## Breaking Changes from v1.0

- Scanner API completely rewritten
- New command-line interface
- Python 3.8+ required
- New dependencies: playwright, aiohttp

## Migration Guide

v1.0 users should review the [Getting Started](docs/getting_started.md) guide for new usage patterns.

## Statistics

- 39 files changed
- 6,679 lines added
- 22,000+ attack payloads
- 6 session security tests
- 8+ mutation strategies

## Contributors

@noobforanonymous

## License

MIT License
