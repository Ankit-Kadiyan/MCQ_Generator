from setuptools import find_packages,setup

setup(
    name='MCQ Generator',
    version='0.0.1',
    author='Ankit Kadiyan',
    author_email='kadiyanankit11@gmail.com',
    packages=find_packages(),
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","pandas","numpy"]
)