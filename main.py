#!/usr/bin/env python
"""
Main entry point for the Visual Vulnerabilities Testing Framework.
"""

from visual_vulnerabilities.core.image_manipulator import VisualAttackToolkit
from visual_vulnerabilities.examples.basic_demo import run_demo, run_multimodal_demo
from visual_vulnerabilities.examples.challenge_demo import run_challenge

def main():
    """Main entry point for the tool."""
    print("🚀 Visual Vulnerabilities Testing Framework")
    print("-------------------------------------------")
    print("A toolkit for researching multimodal AI vulnerabilities")
    print("\nPlease select an option:")
    print("1. Run Basic Demo (visual attacks only)")
    print("2. Run Multimodal Demo (combined visual and text attacks)")
    print("3. Visual Prompt Injection Challenge")
    print("4. Chem/Bio/Cyber Weaponization Challenge")
    print("5. Privacy Violations Challenge")
    print("6. Stereotyping Challenge")
    print("7. Exit")
    
    try:
        choice = input("\nEnter your choice (1-7): ")
        
        # Create toolkit instance
        toolkit = VisualAttackToolkit()
        
        if choice == "1":
            run_demo(toolkit)
        elif choice == "2":
            run_multimodal_demo(toolkit)
        elif choice == "3":
            run_challenge("visual_prompt_injection", toolkit)
        elif choice == "4":
            run_challenge("chem_bio_cyber", toolkit)
        elif choice == "5":
            run_challenge("privacy_violations", toolkit)
        elif choice == "6":
            run_challenge("stereotyping", toolkit)
        elif choice == "7":
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please try again.")
            main()  # Restart menu
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    
    # Ask if user wants to continue
    try:
        again = input("\nWould you like to run another test? (y/n): ")
        if again.lower() in ("y", "yes"):
            main()  # Restart menu
        else:
            print("Thank you for using the Visual Vulnerabilities Testing Framework!")
    except:
        print("\nExiting...")

if __name__ == "__main__":
    main()