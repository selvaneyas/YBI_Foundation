import subprocess
import sys

# Function to install a specific package
def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"✅ Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install '{package_name}':", e)

if __name__ == "__main__":
    #install_package("streamlit")
    #install_package("numpy")
    #install_package("scipy")
    install_package("nltk")
    install_package("seaborn")
#    install_package("numpy==1.26.4")
 #   install_package("scipy==1.11.4")          # compiled for NumPy 1.26
  #  install_package("scikit-learn==1.4.2")     # or the version you trained with
   # install_package("matplotlib==3.8.4")       # optional, cleans the “-atplotlib” warning

