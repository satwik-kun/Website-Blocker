# Website Blocker

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-44%20passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-40.36%25-yellow)
![Code Quality](https://img.shields.io/badge/pylint-9.15%2F10-brightgreen)
![Platform](https://img.shields.io/badge/platform-Windows-blue)

A professional Python-based website blocker with GUI for Windows. Block distracting websites to improve productivity.

## Project Structure

```
Website Blocker/
├── src/                          # Source code
│   ├── website_blocker.py        # Main GUI application
│   └── proxy_server.py           # HTTP server for block page
│
├── tests/                        # Test suite (44 tests)
│   ├── unit/                     # Unit tests (27 tests)
│   ├── integration/              # Integration tests (9 tests)
│   ├── e2e/                      # End-to-end tests (8 tests)
│   ├── system/                   # System tests (10 tests)
│   └── run_quality_checks.py    # Quality check runner
│
├── config/                       # Configuration files
│   └── blocked_sites.json        # Blocked websites list
│
├── assets/                       # Static assets
│   └── block_page.html           # Custom block page
│
├── docs/                         # Documentation
│   ├── README.md                 # Main documentation
│   ├── BROWSER_SETUP.md          # Browser configuration
│   └── TEST_SUMMARY.md           # Test documentation
│
├── .github/workflows/            # CI/CD
│   └── tests.yml                 # GitHub Actions pipeline
│
├── .coveragerc                   # Coverage config (40.36%)
├── .pylintrc                     # Pylint config (9.15/10)
├── .flake8                       # Flake8 config
├── .bandit                       # Security config
├── mypy.ini                      # Type checking config
├── pytest.ini                    # Pytest config
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## Features

- 🚫 Block websites by modifying Windows hosts file
- 🎨 Modern tkinter GUI
- ⏰ Timer-based blocking (30min, 1hr, 2hr, 4hr)
- 🔄 Toggle individual sites on/off
- 📝 Persistent configuration
- 🌐 Blocks all domain variations (www, m, mobile, app, api)
- 🔒 HTTP block page display
- ⚡ Aggressive DNS cache flushing

## Installation

### Prerequisites

- Python 3.8 or higher
- Windows 10/11
- Administrator privileges

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd "Website Blocker"
```

2. Install dependencies (optional):
```bash
pip install -r requirements.txt
```

3. Run as Administrator:
```bash
python src/website_blocker.py
```

## Usage

### Basic Usage

1. **Start the application** as Administrator
2. **Add websites** by typing domain name (e.g., `facebook.com`)
3. **Click "Add & Block"** or press Enter
4. Website is immediately blocked

### Features

- **Toggle Block**: Double-click or select and click "Toggle Selected"
- **Remove Site**: Select and press Delete or click "Remove Selected"
- **Quick Add**: Click preset buttons for popular sites
- **Timer Block**: Click timer buttons (30m, 1h, 2h, 4h) to block temporarily

### Viewing Blocked Sites

- Visit `http://blocked-site.com` in browser
- Press **Ctrl+Shift+R** (hard refresh) to see block page
- HTTPS sites will show "Can't connect" (normal behavior)

## Project Structure

```
Website Blocker/
├── src/                    # Source code
│   ├── website_blocker.py  # Main application
│   └── proxy_server.py     # HTTP server for block page
├── tests/                  # Test suite
│   ├── test_unit.py        # Unit tests
│   ├── test_integration.py # Integration tests
│   └── test_all.py         # System tests
├── config/                 # Configuration files
│   └── blocked_sites.json  # Blocked sites list
├── assets/                 # Static assets
│   └── block_page.html     # Block page HTML
├── docs/                   # Documentation
│   ├── README.md           # This file
│   └── BROWSER_SETUP.md    # Browser configuration
├── main.py                 # Entry point
└── requirements.txt        # Python dependencies
```

## Testing

### Run All Quality Checks

```bash
python tests/run_quality_checks.py
```

**Results: 10/10 Checks Passing ✅**

- ✅ Unit Tests: 27 tests
- ✅ Integration Tests: 9 tests  
- ✅ E2E Tests: 8 tests
- ✅ System Tests: 10 tests
- ✅ Coverage: 40.36%
- ✅ Pylint: 9.15/10
- ✅ Flake8: PASSED
- ✅ Bandit: PASSED
- ✅ MyPy: PASSED
- ✅ Black: PASSED

### Run Individual Tests

```bash
# Unit tests
python -m unittest discover tests/unit -v

# Integration tests
python -m unittest discover tests/integration -v

# E2E tests
python -m unittest discover tests/e2e -v

# System tests
python tests/system/test_all.py
```

### Test Coverage

**Total: 40.36% (website_blocker.py: 38.71%, proxy_server.py: 44.35%)**

Test coverage includes:
- Core blocking/unblocking logic
- Configuration management
- URL sanitization
- Domain variation generation
- Hosts file operations
- Timer functionality
- DNS operations
- Admin privilege checks
- HTTP server functionality

## Development

### Code Quality

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation

### Architecture

- **MVC Pattern**: Separation of UI and logic
- **Configuration Management**: JSON-based persistence
- **Modular Design**: Separate server and blocker logic

## Technical Details

### Blocking Mechanism

1. Modifies Windows hosts file: `C:\Windows\System32\drivers\etc\hosts`
2. Redirects blocked domains to `127.0.0.1`
3. HTTP server on port 80 serves block page
4. Flushes DNS cache for immediate effect

### DNS Cache Flushing

```powershell
ipconfig /flushdns
nbtstat -R
nbtstat -RR
arp -d *
```

### Domain Variations Blocked

For `example.com`:
- `example.com`
- `www.example.com`
- `m.example.com`
- `mobile.example.com`
- `app.example.com`
- `api.example.com`

## Troubleshooting

### Sites Not Blocking

1. **Run as Administrator**
2. **Press Ctrl+Shift+R** in browser (hard refresh)
3. **Disable DNS over HTTPS** (see `docs/BROWSER_SETUP.md`)
4. **Check hosts file** manually

### Block Page Not Showing

- Only works for HTTP sites
- HTTPS sites show "Can't connect" (normal)
- Requires Ctrl+Shift+R refresh

### Tests Failing

- Ensure app is running for integration tests
- Run PowerShell as Administrator
- Check port 80 is not in use

## License

MIT License - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create feature branch
3. Write tests for new features
4. Submit pull request

## Support

For issues and questions, open an issue on GitHub.
