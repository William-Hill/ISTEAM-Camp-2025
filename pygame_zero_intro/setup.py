#!/usr/bin/env python3
"""
Setup script for Pygame Zero Tutorial Game.
This script installs dependencies and generates game assets automatically.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"   {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9 or higher is required!")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible!")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\n📦 Installing dependencies...")
    
    # Install pgzero
    if not run_command("pip install pgzero", "Installing Pygame Zero"):
        return False
    
    # Install Pillow for sprite generation
    if not run_command("pip install Pillow", "Installing Pillow"):
        return False
    
    return True

def generate_assets():
    """Generate game sprites and sounds"""
    print("\n🎨 Generating game assets...")
    
    # Generate alien sprites and sound
    if not run_command("python3 create_alien_sprites.py", "Generating alien sprites and sounds"):
        return False
    
    return True

def test_installation():
    """Test if Pygame Zero is working"""
    print("\n🧪 Testing installation...")
    
    # Try to import pgzero
    try:
        import pgzero
        print("✅ Pygame Zero imported successfully!")
        return True
    except ImportError:
        print("❌ Failed to import Pygame Zero!")
        return False

def main():
    """Main setup function"""
    print("👽 Welcome to Pygame Zero Tutorial Game Setup!")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation!")
        print("   Try running: pip install pgzero Pillow")
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print("\n❌ Setup failed during testing!")
        sys.exit(1)
    
    # Generate assets
    if not generate_assets():
        print("\n❌ Setup failed during asset generation!")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("   1. Run the game: pgzrun intro.py")
    print("   2. Click on the alien to make it hurt!")
    print("   3. Read README.md for learning resources")
    print("   4. Try the learning challenges!")
    print("\n🚀 Have fun learning Python game development!")

if __name__ == "__main__":
    main() 