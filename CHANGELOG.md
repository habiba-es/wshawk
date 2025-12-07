# Changelog

All notable changes to WSHawk will be documented in this file.

## [2.0.3] - 2025-12-07

### Fixed
- Version mismatch between `__init__.py` and package files (now all 2.0.2)
- Inconsistent time usage: Changed `time.time()` to `time.monotonic()` in scanner_v2.py for system-time-change safety
- Added missing PyYAML dependency
- Fixed entry point for `wshawk` command

### Added
- Centralized logging system (`wshawk/logger.py`) with colored output and file logging support
- Configurable authentication in SessionHijackingTester - no longer hardcoded to user1/pass1
- CHANGELOG.md for tracking all changes

### Improved
- Session tester now accepts `auth_config` parameter for custom authentication flows
- Better error handling with specific exception types (ongoing)
- All CLI commands work correctly (wshawk, wshawk-interactive, wshawk-advanced)

## [2.0.1] - 2025-12-07

### Changed
- Cleaned up documentation
- Removed attribution text from README

## [2.0.0] - 2025-12-07

### Added
- Complete rewrite with advanced features
- Real vulnerability verification with Playwright
- OAST integration for blind vulnerabilities
- Session hijacking tests (6 security tests)
- Intelligent mutation engine with WAF bypass
- CVSS v3.1 scoring
- Professional HTML reporting
- Adaptive rate limiting
- Plugin system
- Three CLI modes (quick, interactive, advanced)

### Changed
- Scanner API completely rewritten
- New command-line interface
- Python 3.8+ required
- New dependencies: playwright, aiohttp, PyYAML

## [1.0.6] - Previous

### Features
- Basic WebSocket scanning
- Reflection-based detection
- 22,000+ payloads
