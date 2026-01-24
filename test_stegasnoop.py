import unittest
import random
from PIL import Image
import stegasnoop  # Importing the main script module

class TestStegaSnoop(unittest.TestCase):

    def setUp(self):
        # 1. Create a solid color image (Zero Entropy)
        self.solid_img = Image.new("L", (50, 50), color=0)
        
        # 2. Create a simple gradient image (Low Entropy)
        self.gradient_img = Image.new("RGB", (50, 50))
        pixels = self.gradient_img.load()
        for x in range(50):
            for y in range(50):
                pixels[x, y] = (x, y, 100)

        # 3. Create a random noise image (High Entropy)
        # Random noise usually has entropy close to 8.0 
        self.noise_img = Image.new("RGB", (50, 50))
        noise_pixels = self.noise_img.load()
        for x in range(50):
            for y in range(50):
                noise_pixels[x, y] = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )

    def test_calculate_entropy_solid(self):
        """Test that a solid grayscale image has 0.0 entropy."""
        entropy = stegasnoop.calculate_entropy(self.solid_img)
        self.assertEqual(entropy, 0.0, "Solid image should have 0 entropy")

    def test_calculate_entropy_gradient(self):
        """Test that a gradient image has valid positive entropy."""
        entropy = stegasnoop.calculate_entropy(self.gradient_img)
        self.assertGreater(entropy, 0.0, "Gradient image should have positive entropy")

    def test_calculate_entropy_high(self):
        """Test that a random noise image has high entropy (> 7.0)."""
        entropy = stegasnoop.calculate_entropy(self.noise_img)
        self.assertGreater(entropy, 7.0, "Random noise should have high entropy")

    def test_small_image(self):
        """Edge Case: Test that a 1x1 image is handled without crashing."""
        tiny_img = Image.new("RGB", (1, 1), color=(255, 255, 255))
        try:
            entropy = stegasnoop.calculate_entropy(tiny_img)
            self.assertIsNotNone(entropy)
        except Exception as e:
            self.fail(f"calculate_entropy crashed on 1x1 image: {e}")

    def test_analyze_lsb_placeholder(self):
        """Test the LSB placeholder function returns expected string."""
        result = stegasnoop.analyze_lsb(self.solid_img)
        self.assertEqual(result, "No obvious LSB anomalies found (Placeholder)")

    def test_check_adjacent_correlation_placeholder(self):
        """Test the correlation placeholder function returns expected string."""
        result = stegasnoop.check_adjacent_correlation(self.solid_img)
        self.assertEqual(result, "Correlation normal (Placeholder)")

if __name__ == '__main__':
    unittest.main()