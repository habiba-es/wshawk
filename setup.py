from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Collect all payload files
payload_files = []
payloads_dir = "payloads"
if os.path.exists(payloads_dir):
    for filename in os.listdir(payloads_dir):
        if filename.endswith(".txt"):
            payload_files.append(os.path.join(payloads_dir, filename))

setup(
    name="wshawk",
    version="1.0.0",
    author="Regaan",
    author_email="webdevelopment123.0.0.1@gmail.com",
    description="Advanced WebSocket security scanner with 22,000+ attack payloads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noobforanonymous/wshawk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "wshawk=wshawk:main",
            "wshawk-interactive=wshawk_interactive:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["payloads/*.txt"],
    },
    keywords="websocket security scanner penetration-testing bug-bounty vulnerability",
    project_urls={
        "Bug Reports": "https://github.com/noobforanonymous/wshawk/issues",
        "Source": "https://github.com/noobforanonymous/wshawk",
    },
)
