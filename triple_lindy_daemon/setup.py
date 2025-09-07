#!/usr/bin/env python3
"""
Setup script for Triple Lindy daemon and client
"""
from setuptools import setup, find_packages

setup(
    name="triple-lindy-daemon",
    version="1.0.0",
    description="Triple Lindy Live Execution Loop - Daemon and Client",
    author="Triple Lindy Team",
    python_requires=">=3.9",
    packages=find_packages(),
    install_requires=[
        "websockets>=10.0",
        "websocket-client>=1.0",
    ],
    entry_points={
        "console_scripts": [
            "tl-daemon=triple_lindy_daemon.daemon:main",
            "tl-cli=triple_lindy_daemon.tl_client:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
