# StegaSnoop

## Overview
StegaSnoop is a lightweight educational tool for detecting potential image steganography.
It uses simple heuristic techniques to analyze images for suspicious patterns.

## How It Works
StegaSnoop applies the following heuristic checks:
- Least Significant Bit (LSB) analysis
- Shannon entropy calculation
- Adjacent pixel correlation analysis

These techniques help highlight anomalies that may indicate hidden data.

## What This Tool Does NOT Do
- It does not guarantee detection of all steganography techniques
- It is not a forensic or enterprise-grade security tool
- It should not be used as the sole decision-making mechanism

## How to Run
```bash
python stegasnoop.py image.png
## Contributing
Contributions are welcome!

To contribute:
1. Fork this repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Open a pull request describing what you changed
