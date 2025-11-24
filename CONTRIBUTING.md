# Contributing to Website Blocker

Thank you for considering contributing to Website Blocker! 🎉

## How to Contribute

### Reporting Bugs 🐛

1. **Check existing issues** - Someone may have already reported it
2. **Create a new issue** with:
   - Clear title
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version, OS version
   - Screenshots if applicable

### Suggesting Features 💡

1. **Check existing feature requests**
2. **Create a new issue** with:
   - Clear description of the feature
   - Use cases / why it's needed
   - Potential implementation approach

### Submitting Pull Requests 🔀

#### Setup Development Environment

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Website-Blocker.git
cd Website-Blocker

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests to verify setup
python tests/run_quality_checks.py
```

#### Making Changes

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Follow existing code style
   - Add tests for new features
   - Update documentation

3. **Run quality checks**
   ```bash
   python tests/run_quality_checks.py
   ```
   Ensure all 10 checks pass:
   - ✅ Unit Tests
   - ✅ Integration Tests
   - ✅ E2E Tests
   - ✅ System Tests
   - ✅ Coverage (minimum 40%)
   - ✅ Pylint (minimum 9.0/10)
   - ✅ Flake8
   - ✅ Bandit
   - ✅ MyPy
   - ✅ Black

4. **Commit changes**
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in PR template

## Code Style Guidelines

### Python Code

- Follow **PEP 8** style guide
- Use **type hints** where appropriate
- Write **docstrings** for functions and classes
- Keep functions **small and focused** (single responsibility)
- Use **meaningful variable names**

**Example:**
```python
def sanitize_url(self, url: str) -> str:
    """
    Remove protocol and www from URL.
    
    Args:
        url: Raw URL string
        
    Returns:
        Cleaned domain name
    """
    url = url.lower()
    url = url.replace("https://", "").replace("http://", "")
    url = url.replace("www.", "")
    return url.split('/')[0]
```

### Testing

- Write tests for new features
- Maintain or improve code coverage
- Use descriptive test names

**Example:**
```python
def test_sanitize_url_removes_https_and_www(self):
    """Test URL sanitization removes protocol and www prefix"""
    result = blocker.sanitize_url("https://www.facebook.com")
    self.assertEqual(result, "facebook.com")
```

### Documentation

- Update README if adding features
- Add docstrings to new functions
- Update CHANGELOG.md

## Pull Request Process

1. **Ensure all tests pass**
2. **Update documentation** as needed
3. **Add entry to CHANGELOG.md** under "Unreleased"
4. **Fill out PR template** completely
5. **Wait for review** - maintainer will review within 48 hours
6. **Address feedback** - make requested changes
7. **Merge** - once approved, PR will be merged

## Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Tests added/updated
```

## Development Guidelines

### Project Structure

```
src/          - Source code only
tests/        - All tests
docs/         - Documentation
config/       - Configuration files
assets/       - Static files (HTML, images)
```

### Commit Messages

Use clear, descriptive commit messages:

**Good:**
- `Add timer functionality for temporary blocking`
- `Fix hosts file permission error on Windows`
- `Update README with installation instructions`

**Bad:**
- `fixed stuff`
- `update`
- `wip`

### Branch Naming

- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `docs/what-changed` - Documentation only
- `refactor/what-changed` - Code refactoring

## Testing Standards

### Required Coverage

- **Minimum coverage: 40%**
- New features should include tests
- Bug fixes should include regression tests

### Test Categories

1. **Unit Tests** (`tests/unit/`)
   - Test individual functions
   - Use mocking for dependencies

2. **Integration Tests** (`tests/integration/`)
   - Test component interactions
   - Minimal mocking

3. **E2E Tests** (`tests/e2e/`)
   - Test complete workflows
   - No mocking

4. **System Tests** (`tests/system/`)
   - Test real system integration
   - Validate actual behavior

## Code Review Criteria

Reviewers will check:

- ✅ **Functionality** - Does it work as intended?
- ✅ **Tests** - Are there adequate tests?
- ✅ **Code quality** - Is it clean and maintainable?
- ✅ **Documentation** - Is it well documented?
- ✅ **Style** - Does it follow guidelines?
- ✅ **Performance** - Is it efficient?
- ✅ **Security** - Are there security concerns?

## Getting Help

- 💬 **Discussions** - Ask questions, share ideas
- 🐛 **Issues** - Report bugs, request features
- 📧 **Email** - For security issues (see SECURITY.md)

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on what's best for the project
- Accept constructive criticism gracefully

## Recognition

Contributors will be:
- Added to README contributors section
- Mentioned in release notes
- Recognized in project documentation

## Questions?

Feel free to:
- Open a discussion
- Create an issue with question label
- Comment on related PR/issue

---

**Thank you for contributing! 🙏**

Every contribution, no matter how small, helps make this project better!
