# Security Policy

## Supported Versions

Currently supported versions of Website Blocker:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Considerations

### Administrator Privileges

⚠️ **This application requires administrator privileges** to:
- Modify the Windows hosts file (`C:\Windows\System32\drivers\etc\hosts`)
- Run HTTP server on port 80

**Security Implications:**
- Application has system-level access when running as admin
- Can modify critical system files
- Users should review source code before running

### Hosts File Modification

✅ **Safety Measures:**
- Creates backup before modifications (`hosts.bak`)
- Validates entries before writing
- Restores backup on errors
- Uses file locking to prevent corruption

⚠️ **Risks:**
- Incorrect modifications could break internet access
- Malicious code could redirect sites to harmful servers
- **Recommendation**: Review source code in `src/website_blocker.py`

### HTTP Server (Port 80)

⚠️ **Security Notes:**
- Runs local HTTP server on port 80
- Serves static HTML block page only
- No external network access
- No sensitive data transmitted

**Potential Risks:**
- Port 80 accessible on local network
- Other devices on network could access block page
- **Mitigation**: Server only serves static HTML, no code execution

### Data Storage

✅ **Configuration File** (`config/blocked_sites.json`):
- Stores only website domains
- No sensitive user data
- Plain text JSON format
- User can inspect and edit manually

**What's Stored:**
```json
{
    "blocked_sites": [
        "facebook.com",
        "youtube.com"
    ]
}
```

### Dependencies

✅ **No External Dependencies**
- Uses Python standard library only
- No third-party packages
- Reduces supply chain attack risk
- All code is reviewable in repository

**Standard Library Modules Used:**
- `tkinter` - GUI framework
- `http.server` - HTTP server
- `threading` - Background server
- `json` - Configuration storage
- `os`, `sys`, `pathlib` - File system operations
- `datetime`, `time` - Timer functionality

## Known Security Limitations

### 1. HTTP Only (No HTTPS)
- Block page served over HTTP, not HTTPS
- HTTPS sites will show certificate warnings
- Cannot display block page for HTTPS without browser extension

### 2. Administrator Access Required
- Must run with elevated privileges
- Potential for system-wide impact if compromised
- Users should trust the application before running

### 3. No Password Protection
- Anyone with access to computer can unblock sites
- No authentication mechanism
- Consider adding password protection in future versions

### 4. Local Network Exposure
- HTTP server accessible to other devices on local network
- Block page visible to network users
- **Recommendation**: Use firewall to restrict port 80 access

### 5. No Encryption
- Configuration file stored in plain text
- Blocked sites list readable by anyone with file access
- No sensitive data, but lack of privacy

## Reporting a Vulnerability

### How to Report

If you discover a security vulnerability, please report it responsibly:

1. **DO NOT** open a public GitHub issue
2. **Email**: [Your email for security reports]
   - Subject: "Website Blocker Security Vulnerability"
   - Include detailed description
   - Steps to reproduce
   - Potential impact assessment

3. **Expected Response Time**:
   - Initial response: Within 48 hours
   - Status update: Within 7 days
   - Fix timeline: Depends on severity

### What to Include

- **Vulnerability type** (e.g., code injection, privilege escalation)
- **Affected component** (which file/function)
- **Steps to reproduce**
- **Proof of concept** (if applicable)
- **Potential impact** (what could happen)
- **Suggested fix** (optional)

### Disclosure Policy

- **Coordinated Disclosure**: We will work with you to understand and fix the issue
- **Timeline**: Aim to release fix within 30 days
- **Credit**: You will be credited in release notes (unless you prefer anonymity)
- **Public Disclosure**: After fix is released

## Security Best Practices

### For Users

1. ✅ **Review source code** before running with admin privileges
2. ✅ **Download from official repository** only
3. ✅ **Verify file integrity** (check file hashes if provided)
4. ✅ **Run with least privilege** when possible (future versions may not require admin)
5. ✅ **Keep Python updated** to latest stable version
6. ✅ **Monitor hosts file** for unexpected changes
7. ✅ **Use firewall** to restrict port 80 access to local machine only

### For Developers/Contributors

1. ✅ **Code review** all pull requests
2. ✅ **Run quality checks** (`python tests/run_quality_checks.py`)
3. ✅ **Validate inputs** (URL sanitization already implemented)
4. ✅ **Use type hints** for type safety
5. ✅ **Avoid** `eval()`, `exec()`, `__import__()`
6. ✅ **Handle exceptions** gracefully
7. ✅ **Document security implications** of changes

## Threat Model

### In Scope

- ✅ Hosts file corruption/manipulation
- ✅ Code injection vulnerabilities
- ✅ Privilege escalation
- ✅ Path traversal attacks
- ✅ Denial of service (local)

### Out of Scope

- ❌ Physical access attacks
- ❌ Social engineering
- ❌ Browser vulnerabilities
- ❌ Operating system vulnerabilities
- ❌ Network-level attacks (MITM, etc.)

## Security Checklist

Before running Website Blocker:

- [ ] Downloaded from official repository
- [ ] Reviewed source code (at minimum: `src/website_blocker.py`, `src/proxy_server.py`)
- [ ] Understand admin privilege implications
- [ ] Backed up hosts file manually (optional extra safety)
- [ ] Configured firewall to restrict port 80 if needed
- [ ] Python installation is up-to-date

## Acknowledgments

We appreciate responsible disclosure of security issues. Contributors who report valid vulnerabilities will be acknowledged here:

- *No vulnerabilities reported yet*

---

## Questions?

For security-related questions (not vulnerabilities):
- Open a GitHub Discussion
- Tag with `security` label

For actual vulnerabilities:
- **Email**: [Your security contact email]
- **Do not** open public issues

---

**Last Updated**: 2025-11-24
**Version**: 1.0.0
