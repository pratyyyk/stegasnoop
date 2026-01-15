import argparse
import sys
import math
from PIL import Image

def calculate_entropy(image):
    """Calculates the Shannon entropy of the image."""
    histogram = image.histogram()
    histogram_length = sum(histogram)
    samples_probability = [float(h) / histogram_length for h in histogram]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

def analyze_lsb(image):
    """Placeholder for Least Significant Bit (LSB) analysis."""
    # Logic to be improved in future issues
    print("[-] Performing LSB Analysis... (Basic check)")
    return "No obvious LSB anomalies found (Placeholder)"

def check_adjacent_correlation(image):
    """Placeholder for Adjacent Pixel Correlation analysis."""
    # Logic to be improved in future issues
    print("[-] Checking adjacent pixel correlation...")
    return "Correlation normal (Placeholder)"

def main():
    # --- SOLUTION FOR ISSUE #1: CLI ARGUMENT SUPPORT ---
    parser = argparse.ArgumentParser(description="StegaSnoop: Lightweight Steganography Detector")
    
    # This line allows the user to pass the image path directly
    parser.add_argument("image_path", help="Path to the image file to analyze")
    
    # Optional: Prepare for Issue #4 (Configurable threshold)
    parser.add_argument("--threshold", type=float, default=7.5, help="Entropy threshold for detection")

    args = parser.parse_args()
    # ---------------------------------------------------

    print(f"[*] Scanning image: {args.image_path}")

    try:
        img = Image.open(args.image_path)
        
        # 1. Entropy Check
        entropy = calculate_entropy(img)
        print(f"[-] Shannon Entropy: {entropy:.4f}")
        
        # Simple heuristic for entropy (can be refined later)
        if entropy > args.threshold:
            print(f"[!] WARNING: High entropy detected! Possible compressed or encrypted data.")
        
        # 2. LSB Analysis
        analyze_lsb(img)

        # 3. Correlation Check
        check_adjacent_correlation(img)

        print("[*] Scan complete.")

    except FileNotFoundError:
        print(f"[x] Error: The file '{args.image_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[x] An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()