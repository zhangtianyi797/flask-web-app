import unittest
import sys
from pathlib import Path

# 把项目根目录加入 Python 搜索路径
sys.path.append(str(Path(__file__).parent.parent))
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_neu(self):
        # 测试返回值是否为 Hello, NEU!（必须和 app.py 一致，否则测试失败）
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, NEU!')

if __name__ == '__main__':
    unittest.main()
