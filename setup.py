import subprocess
import sys

def install(package, package_name=None):
    if package_name is None:
        package_name = package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# List of required packages and their pip names
required_packages = {
    "pandas": "pandas",
    "numpy": "numpy",
    "tqdm": "tqdm",
    "sklearn": "scikit-learn",
    "nltk": "nltk"
}

# Check and install each package if needed
for module, pkg in required_packages.items():
    try:
        __import__(module)
    except ImportError:
        install(module, pkg)

# Download NLTK stopwords if not already downloaded
import nltk
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')





