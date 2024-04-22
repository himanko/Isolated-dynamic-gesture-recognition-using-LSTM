import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Isolated-dynamic-gesture-recognition-using-LSTM"
AUTHOR_USER_NAME = "himanko"
SRC_REPO = "LSTMSignLanguageTranslator"
AUTHOR_EMAIL = "himankoboruah@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="The model undergoes training utilizing two ISL datasets and one ASL dataset. ISL comprises an INCLUDE dataset along with a smaller local one, while ASL refers to the WLASL dataset. We employed an LSTM architecture to train the available datasets.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)