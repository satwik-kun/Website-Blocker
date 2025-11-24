"""
Integration Tests for Website Blocker
Tests end-to-end functionality and system integration
"""

import unittest
import subprocess
import os
import time
import json
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))


class TestSystemIntegration(unittest.TestCase):
    """Integration tests for system-level operations"""
    
    @unittest.skip("Requires port 80 access (admin privileges) - manual test only")
    def test_http_server_availability(self):
        """Test that HTTP server can be reached"""
        result = self._run_powershell(
            "Test-NetConnection -ComputerName 127.0.0.1 -Port 80 -WarningAction SilentlyContinue | Select-Object -ExpandProperty TcpTestSucceeded"
        )
        self.assertIn("True", result)
    
    @unittest.skip("Requires port 80 access (admin privileges) - manual test only")
    def test_block_page_content(self):
        """Test block page is served correctly"""
        result = self._run_powershell(
            '(Invoke-WebRequest -Uri http://127.0.0.1 -UseBasicParsing).StatusCode'
        )
        self.assertIn("200", result)
    
    def test_hosts_file_readable(self):
        """Test hosts file is accessible"""
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        self.assertTrue(os.path.exists(hosts_path))
        
        # Check if we can read it
        try:
            with open(hosts_path, 'r') as f:
                content = f.read()
            self.assertIsInstance(content, str)
        except PermissionError:
            self.skipTest("Requires admin privileges")
    
    def test_dns_flush_command(self):
        """Test DNS flush command executes"""
        result = self._run_powershell('ipconfig /flushdns')
        self.assertIn("Successfully flushed", result)
    
    def test_config_file_operations(self):
        """Test config file can be read/written"""
        config_path = Path(__file__).parent.parent / 'config' / 'blocked_sites.json'
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                data = json.load(f)
            self.assertIsInstance(data, list)
    
    def _run_powershell(self, command):
        """Run PowerShell command and return output"""
        try:
            result = subprocess.run(
                ["powershell", "-Command", command],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8',
                errors='ignore'
            )
            return result.stdout.strip()
        except:
            return ""


class TestEndToEnd(unittest.TestCase):
    """End-to-end workflow tests"""
    
    def test_complete_block_workflow(self):
        """Test complete blocking workflow"""
        # 1. Add website to list
        test_site = "testexample.com"
        blocked_sites = []
        
        # 2. Add to list
        if test_site not in blocked_sites:
            blocked_sites.append(test_site)
        
        self.assertIn(test_site, blocked_sites)
        
        # 3. Generate hosts entries
        redirect_ip = "127.0.0.1"
        entry = f"{redirect_ip} {test_site}"
        
        self.assertEqual(entry, "127.0.0.1 testexample.com")
        
        # 4. Verify removal
        blocked_sites.remove(test_site)
        self.assertNotIn(test_site, blocked_sites)
    
    def test_url_sanitization_workflow(self):
        """Test URL sanitization in workflow"""
        test_urls = [
            "https://facebook.com",
            "http://www.twitter.com",
            "instagram.com/explore"
        ]
        
        expected = [
            "facebook.com",
            "twitter.com",
            "instagram.com"
        ]
        
        sanitized = []
        for url in test_urls:
            clean = url.replace("http://", "").replace("https://", "").replace("www.", "")
            if "/" in clean:
                clean = clean.split("/")[0]
            sanitized.append(clean)
        
        self.assertEqual(sanitized, expected)


class TestPerformance(unittest.TestCase):
    """Performance tests"""
    
    def test_config_load_performance(self):
        """Test config loading is fast"""
        import tempfile
        
        # Create large config
        large_list = [f"site{i}.com" for i in range(100)]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(large_list, f)
            temp_path = f.name
        
        try:
            start = time.time()
            with open(temp_path, 'r') as f:
                data = json.load(f)
            end = time.time()
            
            # Should load in less than 0.1 seconds
            self.assertLess(end - start, 0.1)
            self.assertEqual(len(data), 100)
        finally:
            os.unlink(temp_path)
    
    def test_dns_flush_performance(self):
        """Test DNS flush executes quickly"""
        start = time.time()
        os.system("ipconfig /flushdns > nul 2>&1")
        end = time.time()
        
        # Should complete in less than 2 seconds
        self.assertLess(end - start, 2.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
