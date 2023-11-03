import setuptools

from etripy import __version__

setuptools.setup(
    name="etripy",
    version=__version__,
    license="MIT",
    author="VoidAsMad",
    author_email="star@devksy.xyz",
    description="인공지능 기술을 체험할 수 있는 공공 인공지능 오픈 API Wrapper",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VoidAsMad/ETRI",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["requests", "aiohttp"],
)