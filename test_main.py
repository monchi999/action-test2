import unittest
from main import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Flaskのテストクライアントをセットアップ
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # '/' エンドポイントのテスト
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

if __name__ == "__main__":
    unittest.main()