from setuptools import setup

setup(
    name="regressionproject",
    version="0.1",
    description="Regression project",
    url="http://github.com/storborg/funniest",
    author="Algopaul",
    author_email="info@algopaul.com",
    license="MIT",
    packages=["regressionproject"],
    install_requires=["numpy", "parameterized", "pytest"],
    zip_safe=False,
)
