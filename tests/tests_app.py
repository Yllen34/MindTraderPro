"""
Tests unitaires pour les endpoints de base de l'application.
"""

import unittest
from backend.app import create_app

class TestApp(unittest.TestCase):
    """Classe de tests pour les routes principales."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_ping_endpoint(self):
        """Teste le endpoint /ping."""
        response = self.client.get('/api/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'pong')

if __name__ == '__main__':
    unittest.main()
