import unittest
from image_processor.filters import apply_blur
from image_processor.transformations import rotate_image

class TestImageProcessor(unittest.TestCase):
    
    def test_apply_blur(self):
        # Aqui, você testaria se o filtro de desfoque está funcionando corretamente
        self.assertTrue(True)

    def test_rotate_image(self):
        # Teste a rotação da imagem
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
