from setuptools import setup, find_packages

setup(
    name="my-auto-codebase-documenter",
    version="1.2",
    packages=["my_auto_codebase_documenter"],
    install_requires=["openai", "python-dotenv", "PyYAML"],
    entry_points={
        "console_scripts": [
            "auto-codebase-documenter = my_auto_codebase_documenter.auto_documenter:main",
            "create_config = my_auto_codebase_documenter.auto_documenter:create_documenter_config"
        ],
    },
    author="Laurent Nopoly",
    author_email="laurentnopoly@gmail.com",
    description="Automatic codebase documentation tool using OpenAI GPT models and forked from the original repository of Alex Bryant https://github.com/abryant710/auto-codebase-documenter version = 1.2",
    long_description="This tool utilizes OpenAI GPT models to automatically assess and document a codebase by generating written assessments for each file.",
    long_description_content_type="text/markdown",
    url="https://github.com/LauNop/auto-codebase-documenter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    platforms=["any"],
)
