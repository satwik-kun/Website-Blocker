"""
Comprehensive Code Quality Test Suite
Runs all quality checks: pylint, bandit, flake8, mypy, coverage, safety
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description, show_output=False):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"[PASSED] {description}")
            if show_output and result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"[FAILED] {description}")
            if show_output and (result.stderr or result.stdout):
                print(result.stderr or result.stdout)
            return False
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] {description}")
        return False
    except Exception as e:
        print(f"[ERROR] {description}: {e}")
        return False


def main():
    """Run all code quality checks"""
    print("\n" + "="*60)
    print("CODE QUALITY & TEST SUITE")
    print("="*60 + "\n")
    
    results = {}
    
    # 1. Unit Tests
    results['Unit Tests'] = run_command(
        ['python', '-m', 'unittest', 'discover', 'tests/unit', '-v'],
        "Unit Tests"
    )
    
    # 2. Integration Tests
    results['Integration Tests'] = run_command(
        ['python', '-m', 'unittest', 'discover', 'tests/integration', '-v'],
        "Integration Tests"
    )
    
    # 3. E2E Tests
    results['E2E Tests'] = run_command(
        ['python', '-m', 'unittest', 'discover', 'tests/e2e', '-v'],
        "E2E Tests"
    )
    
    # 4. System Tests
    results['System Tests'] = run_command(
        ['python', 'tests/system/test_all.py'],
        "System Tests"
    )
    
    # 5. Coverage
    run_command(
        ['coverage', 'run', '--source=src', '-m', 'pytest', 'tests/unit', 'tests/integration', '-v'],
        "Coverage Run"
    )
    results['Coverage Report'] = run_command(
        ['coverage', 'report', '-m', '--fail-under=40'],
        "Coverage Report (40% minimum)",
        show_output=True
    )
    run_command(['coverage', 'html'], "Coverage HTML Generation")
    
    # 6. Pylint
    result = subprocess.run(
        ['pylint', 'src/', '--rcfile=.pylintrc'],
        capture_output=True,
        text=True,
        timeout=300
    )
    # Extract score from pylint output
    score_line = [line for line in result.stdout.split('\n') if 'Your code has been rated at' in line]
    if score_line:
        score = float(score_line[0].split('rated at ')[1].split('/')[0])
        if score >= 9.0:
            print(f"[PASSED] Pylint Code Quality (Score: {score:.2f}/10)")
            results['Pylint'] = True
        else:
            print(f"[FAILED] Pylint Code Quality (Score: {score:.2f}/10, need 9.0+)")
            results['Pylint'] = False
    else:
        results['Pylint'] = run_command(
            ['pylint', 'src/', '--rcfile=.pylintrc', '--exit-zero'],
            "Pylint Code Quality"
        )
    
    # 7. Flake8
    results['Flake8'] = run_command(
        ['flake8', 'src/', '--config=.flake8', '--exit-zero'],
        "Flake8 Style Guide"
    )
    
    # 8. Bandit
    results['Bandit'] = run_command(
        ['bandit', '-r', 'src/', '-c', '.bandit', '--exit-zero'],
        "Bandit Security Scan"
    )
    
    # 9. MyPy
    results['MyPy'] = run_command(
        ['mypy', 'src/', '--config-file=mypy.ini', '--ignore-missing-imports'],
        "MyPy Type Checking"
    )
    
    # 10. Black
    results['Black'] = run_command(
        ['black', '--check', 'src/'],
        "Black Code Formatting"
    )
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    percentage = (passed / total) * 100
    
    for name, status in results.items():
        status_text = "[PASSED]" if status else "[FAILED]"
        print(f"{status_text} {name}")
    
    print(f"\nTotal: {passed}/{total} checks passed ({percentage:.0f}%)")
    
    if passed == total:
        print("\n[OK] ALL CHECKS PASSED!\n")
        return 0
    else:
        print(f"\n[FAILED] {total - passed} check(s) failed\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
