# Session Security Tests

WSHawk includes 6 advanced session security tests to detect session hijacking and authentication bypass vulnerabilities.

## 1. Token Reuse
**CVSS Score:** 7.5 (High)

Tests if authentication tokens can be reused after session termination.

**What it tests:**
- Captures authentication token during login
- Closes the session
- Attempts to reuse the token in a new session

**Vulnerable if:**
- Token accepted after session close
- No token expiration
- No session invalidation on logout

**Recommendation:**
- Invalidate tokens on logout
- Implement token expiration (TTL)
- Use short-lived tokens with refresh mechanism

## 2. Subscription Spoofing
**CVSS Score:** 8.1 (High)

Tests if users can subscribe to unauthorized channels.

**What it tests:**
- Attempts to subscribe to admin channels
- Tests private channel access
- Path traversal in channel names

**Test channels:**
- `admin`
- `private_user_123`
- `system`
- `../admin`

**Vulnerable if:**
- Subscription succeeds without authorization
- No channel access control
- Channel names not validated

**Recommendation:**
- Implement strict channel access control
- Validate user permissions before subscription
- Use ACLs for channel access

## 3. Impersonation
**CVSS Score:** 9.1 (Critical)

Tests if users can impersonate other users.

**What it tests:**
- Sending messages as other users
- Updating other users' profiles
- Accessing other users' data

**Attack vectors:**
- `from_user` parameter manipulation
- `user_id` spoofing
- Profile update attacks

**Vulnerable if:**
- Server trusts client-provided user IDs
- No server-side identity validation
- User context not enforced

**Recommendation:**
- Never trust client-provided user IDs
- Validate user identity server-side
- Use session-based user context

## 4. Channel Boundary Violations
**CVSS Score:** 8.6 (High)

Tests if users can access other users' private channels.

**What it tests:**
- Reading private channels
- Accessing DM conversations
- Cross-user message reading

**Test scenarios:**
- `user:user2:private`
- `dm:user2_user3`
- Private channel history

**Vulnerable if:**
- Private data accessible without authorization
- No channel permission checks
- Cross-user data leakage

**Recommendation:**
- Implement strict channel access control
- Validate user permissions for all operations
- Enforce channel boundaries

## 5. Session Fixation
**CVSS Score:** 7.8 (High)

Tests if attackers can set their own session IDs.

**What it tests:**
- Providing session ID during login
- Setting custom session IDs
- Session ID prediction

**Vulnerable if:**
- Server accepts client-provided session IDs
- Session IDs are predictable
- No server-side session generation

**Recommendation:**
- Generate session IDs server-side only
- Use cryptographically random session IDs
- Never accept client-provided session IDs

## 6. Privilege Escalation
**CVSS Score:** 9.8 (Critical)

Tests if users can elevate their privileges.

**What it tests:**
- Role manipulation (`role: admin`)
- Permission elevation
- Admin access attempts

**Attack vectors:**
- `update_role` with `role: admin`
- `set_permissions` with admin permissions
- Login with elevated role

**Vulnerable if:**
- Server accepts client-provided roles
- No server-side role validation
- Permissions can be manipulated

**Recommendation:**
- Enforce server-side role validation
- Never trust client-provided role/permission data
- Implement proper RBAC (Role-Based Access Control)

## Running Session Tests

### Standalone
```bash
python -c "
import asyncio
from wshawk.session_hijacking_tester import SessionHijackingTester

async def test():
    tester = SessionHijackingTester('ws://target.com')
    results = await tester.run_all_tests()
    report = tester.generate_report()
    print(f'Vulnerabilities: {report[\"summary\"][\"vulnerable\"]}')

asyncio.run(test())
"
```

### Included in Full Scan
Session tests run automatically with:
- `wshawk ws://target.com`
- `wshawk-interactive`
- `wshawk-advanced ws://target.com`

## Understanding Results

### Report Format
```json
{
  "summary": {
    "total_tests": 6,
    "vulnerable": 3,
    "critical_vulnerabilities": 2,
    "risk_level": "CRITICAL"
  },
  "vulnerabilities": [
    {
      "type": "impersonation",
      "cvss_score": 9.1,
      "confidence": "CRITICAL",
      "description": "User impersonation possible",
      "recommendation": "Validate user identity server-side"
    }
  ]
}
```

### Risk Levels
- **CRITICAL** - Immediate action required
- **HIGH** - Fix as soon as possible
- **MEDIUM** - Plan remediation
- **LOW** - Monitor and fix when convenient
