__author__ = 'Minghao'
# This module is for converting this app into exe.

from cx_Freeze import setup, Executable

setup(
    name="Poker_Solitaire",
    version="1.0.0",
    description="trial",
    executables=[Executable("entrypoint.py")],
)
