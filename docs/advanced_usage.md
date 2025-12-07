# Advanced Usage

## Python API

### Basic Scan
```python
import asyncio
from wshawk.scanner_v2 import WSHawkV2

async def scan():
    scanner = WSHawkV2("ws://target.com", max_rps=10)
    await scanner.run_intelligent_scan()

asyncio.run(scan())
```

### Full Features Enabled
```python
scanner = WSHawkV2("ws://target.com")
scanner.use_headless_browser = True  # Playwright XSS
scanner.use_oast = True              # OAST for blind vulns
await scanner.run_intelligent_scan()
```

### Session Hijacking Tests
```python
from wshawk.session_hijacking_tester import SessionHijackingTester

async def test_sessions():
    tester = SessionHijackingTester("ws://target.com")
    results = await tester.run_all_tests()
    report = tester.generate_report()
    
    print(f"Vulnerabilities: {report['summary']['vulnerable']}")
    for vuln in report['vulnerabilities']:
        print(f"  - {vuln['type']}: CVSS {vuln['cvss_score']}")

asyncio.run(test_sessions())
```

### Payload Mutation
```python
from wshawk.payload_mutator_v3 import PayloadMutationEngineV3

engine = PayloadMutationEngineV3()
report = engine.generate(
    "<script>alert(1)</script>",
    context="xss",
    max_total=20
)

for strategy, variants in report.by_strategy.items():
    print(f"{strategy}: {len(variants)} payloads")
```

### CVSS Scoring
```python
from wshawk.cvss_calculator import CVSSCalculator

calc = CVSSCalculator()
score = calc.calculate_for_vulnerability("SQL Injection", "HIGH")
print(f"Score: {score.base_score} ({score.severity})")
print(f"Vector: {score.vector_string}")
```

## Custom Integrations

### Integration with CI/CD
```python
import sys

scanner = WSHawkV2("ws://staging.app.com")
await scanner.run_intelligent_scan()

# Fail build if critical vulns found
critical = [v for v in scanner.vulnerabilities if v.get('confidence') == 'CRITICAL']
if critical:
    print(f"Found {len(critical)} critical vulnerabilities!")
    sys.exit(1)
```

### Custom Reporting
```python
# Access raw vulnerability data
for vuln in scanner.vulnerabilities:
    print(f"Type: {vuln['type']}")
    print(f"Severity: {vuln['confidence']}")
    print(f"CVSS: {vuln.get('cvss_score', 'N/A')}")
    print(f"Payload: {vuln['payload']}")
```

## Configuration

### Rate Limiting
```python
scanner = WSHawkV2("ws://target.com", max_rps=5)  # 5 requests/second
```

### Disable Features
```python
scanner.use_headless_browser = False  # Faster, no Playwright
scanner.use_oast = False              # No OAST testing
```

## Advanced Scenarios

### Testing Multiple Endpoints
```python
endpoints = [
    "ws://api.example.com/chat",
    "ws://api.example.com/notifications",
    "ws://api.example.com/updates"
]

for endpoint in endpoints:
    scanner = WSHawkV2(endpoint)
    await scanner.run_intelligent_scan()
```

### Custom Headers
```python
# Note: Headers set via WebSocket connection parameters
# See scanner_v2.py for implementation details
```
