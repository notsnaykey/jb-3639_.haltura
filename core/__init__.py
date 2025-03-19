# Core module initialization
from visual_vulnerabilities.core.image_manipulator import VisualAttackToolkit
from visual_vulnerabilities.core.text_manipulator import TextManipulator
from visual_vulnerabilities.core.multimodal import create_multimodal_attack

__all__ = ['VisualAttackToolkit', 'TextManipulator', 'create_multimodal_attack']