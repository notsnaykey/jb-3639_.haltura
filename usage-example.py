# Visual Vulnerabilities Framework - Colab Usage Example

# Step 1: Clone the repository from GitHub
!git clone https://github.com/yourusername/visual-vulnerabilities.git
%cd visual-vulnerabilities

# Step 2: Install dependencies
!pip install -r requirements.txt

# Step 3: Import modules and create toolkit
from visual_vulnerabilities.core.image_manipulator import VisualAttackToolkit
from visual_vulnerabilities.core.text_manipulator import TextManipulator
from visual_vulnerabilities.examples.challenge_demo import run_challenge

# Create the toolkit
toolkit = VisualAttackToolkit()

# Step 4: Run a specific challenge
# This will prompt for an image upload and generate attacks for the specified challenge
results = run_challenge("visual_prompt_injection", toolkit)

# Step 5: Download results
# You can download any of the generated images for use in the challenge
toolkit.save_image(results["multimodal_attacks"]["complementary"]["image"], "complementary_attack.png")

# Step 6: Print text prompts to use with the images
print("\nText prompts to use with the images:")
for strategy, data in results["multimodal_attacks"].items():
    print(f"{strategy}: {data['text_prompt']}")
