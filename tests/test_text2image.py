
from grpc_api.generated import text2image_pb2, text2image_pb2_grpc  # Now it will work

import unittest
from app.text2image import TextToImageGenerator

class TestTextToImage(unittest.TestCase):
    def setUp(self):
        self.generator = TextToImageGenerator()

    def test_generate_image_valid_prompt(self):
        prompt = "A cat sitting on a chair"
        output = self.generator.generate(prompt)
        self.assertTrue(output.endswith(".png") or output.endswith(".jpg"))

    def test_generate_image_empty_prompt(self):
        with self.assertRaises(ValueError):
            self.generator.generate("")


if __name__ == "__main__":
    unittest.main()

