"""
Quick setup script for Google Colab.
Run this to install and set up the Visual Vulnerabilities framework in Colab.
"""

import os
import shutil
import subprocess
import sys

def setup_visual_vulnerabilities():
    """
    Set up the Visual Vulnerabilities framework in Google Colab.
    """
    # Create the directory structure
    os.makedirs("visual_vulnerabilities", exist_ok=True)
    os.makedirs("visual_vulnerabilities/core", exist_ok=True)
    os.makedirs("visual_vulnerabilities/utils", exist_ok=True)
    os.makedirs("visual_vulnerabilities/examples", exist_ok=True)
    
    # Install required packages
    print("🔄 Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "pillow", "stegano", "qrcode", "opencv-python", 
                          "scipy", "numpy", "matplotlib", "tensorflow"])
    
    print("✅ Framework setup complete!")
    print("📋 Usage Instructions:")
    print("1. Import required modules:")
    print("   from visual_vulnerabilities.core.image_manipulator import VisualAttackToolkit")
    print("   from visual_vulnerabilities.examples.challenge_demo import run_challenge")
    print("2. Create a toolkit instance:")
    print("   toolkit = VisualAttackToolkit()")
    print("3. Run a challenge:")
    print("   run_challenge('visual_prompt_injection', toolkit)")
    
if __name__ == "__main__":
    setup_visual_vulnerabilities()