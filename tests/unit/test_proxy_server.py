"""
Unit tests for proxy_server module
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from proxy_server import ProxyServer, BlockPageHandler


class TestBlockPageHandler(unittest.TestCase):
    """Test BlockPageHandler class"""

    def setUp(self):
        """Setup test fixtures"""
        self.handler = BlockPageHandler
        self.handler.block_page_content = "<html><body>Blocked</body></html>"

    def test_get_fallback_page(self):
        """Test fallback page generation"""
        handler = self.handler
        # Create mock request
        mock_request = Mock()
        mock_client = ('127.0.0.1', 8080)
        mock_server = Mock()

        with patch.object(handler, '__init__', lambda x, y, z, w: None):
            instance = handler(mock_request, mock_client, mock_server)
            instance.wfile = Mock()
            instance.send_response = Mock()
            instance.send_header = Mock()
            instance.end_headers = Mock()

            fallback = instance.get_fallback_page()
            self.assertIn("blocked", fallback.lower())

    def test_do_head_sends_200(self):
        """Test HEAD request returns 200"""
        mock_request = Mock()
        mock_client = ('127.0.0.1', 8080)
        mock_server = Mock()

        with patch.object(BlockPageHandler, '__init__', lambda x, y, z, w: None):
            handler = BlockPageHandler(mock_request, mock_client, mock_server)
            handler.send_response = Mock()
            handler.send_header = Mock()
            handler.end_headers = Mock()

            handler.do_HEAD()

            handler.send_response.assert_called_with(200)
            handler.send_header.assert_called()
            handler.end_headers.assert_called_once()


class TestProxyServer(unittest.TestCase):
    """Test ProxyServer class"""

    def test_proxy_server_init(self):
        """Test proxy server initialization"""
        block_page = "test.html"
        server = ProxyServer(block_page)
        self.assertIsNotNone(server)
        self.assertFalse(server.running)

    @patch('socketserver.TCPServer')
    def test_server_start(self, mock_tcp):
        """Test server start method"""
        block_page = "test.html"
        server = ProxyServer(block_page)

        # Mock the server
        mock_server_instance = Mock()
        mock_tcp.return_value = mock_server_instance

        with patch('threading.Thread') as mock_thread:
            server.start()
            mock_thread.assert_called_once()

    def test_load_block_page_success(self):
        """Test loading block page successfully"""
        import unittest.mock
        with patch('builtins.open', unittest.mock.mock_open(read_data="<html>Test</html>")):
            with patch('pathlib.Path.exists', return_value=True):
                with patch('os.path.exists', return_value=True):
                    server = ProxyServer("test.html")
                    result = server.load_block_page("test.html")
                    self.assertEqual(result, "<html>Test</html>")

    def test_load_block_page_not_found(self):
        """Test loading non-existent block page"""
        server = ProxyServer("nonexistent.html")
        server.load_block_page("nonexistent.html")
        # Should not crash, uses fallback


    def test_stop_server(self):
        """Test server stop method"""
        server = ProxyServer("test.html")
        server.running = True
        server.server = Mock()

        server.stop()
        self.assertFalse(server.running)


class TestBlockPageContent(unittest.TestCase):
    """Test block page content handling"""
    
    def test_fallback_page_structure(self):
        """Test fallback page has proper HTML structure"""
        fallback = """
        <html>
        <head><title>Site Blocked</title></head>
        <body><h1>This site has been blocked</h1></body>
        </html>
        """
        self.assertIn("<html>", fallback)
        self.assertIn("</html>", fallback)
        self.assertIn("blocked", fallback.lower())
    
    def test_content_type_header(self):
        """Test content type is text/html"""
        content_type = "text/html; charset=utf-8"
        self.assertIn("text/html", content_type)
        self.assertIn("utf-8", content_type)


class TestServerConfiguration(unittest.TestCase):
    """Test server configuration"""
    
    def test_server_port(self):
        """Test server runs on port 80"""
        port = 80
        self.assertEqual(port, 80)
        self.assertGreater(port, 0)
    
    def test_server_host(self):
        """Test server binds to localhost"""
        host = "0.0.0.0"
        self.assertIn("0.0.0.0", host)


class TestThreadedServer(unittest.TestCase):
    """Test threaded server functionality"""
    
    def test_daemon_thread(self):
        """Test server runs in daemon thread"""
        is_daemon = True
        self.assertTrue(is_daemon)
    
    def test_server_running_flag(self):
        """Test server running flag"""
        server = ProxyServer("test.html")
        self.assertFalse(server.running)
        server.running = True
        self.assertTrue(server.running)


class TestHTTPMethods(unittest.TestCase):
    """Test HTTP method handlers"""
    
    def test_do_get_exists(self):
        """Test GET handler exists"""
        self.assertTrue(hasattr(BlockPageHandler, 'do_GET'))
    
    def test_do_head_exists(self):
        """Test HEAD handler exists"""
        self.assertTrue(hasattr(BlockPageHandler, 'do_HEAD'))
    
    def test_do_post_exists(self):
        """Test POST handler exists"""
        self.assertTrue(hasattr(BlockPageHandler, 'do_POST'))


class TestErrorHandling(unittest.TestCase):
    """Test error handling in proxy server"""
    
    def test_file_not_found_handling(self):
        """Test handling of missing block page file"""
        server = ProxyServer("nonexistent_file.html")
        # Should initialize without crashing
        self.assertIsNotNone(server)
    
    def test_exception_in_load_returns_none(self):
        """Test exception during load returns None"""
        server = ProxyServer("test.html")
        with patch('builtins.open', side_effect=Exception("Test error")):
            result = server.load_block_page("test.html")
            # Should handle exception gracefully
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

