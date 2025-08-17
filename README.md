Just wrapped up a small but practical automation challenge in Python! 🐍

I built a Folder Synchronization Script that keeps two directories in sync (source → replica), copying new/updated files and logging changes along the way.

The best part? It only uses Python’s standard library (os, shutil, filecmp, argparse, logging) — no external dependencies needed.

This project gave me hands-on experience with:
✅ Command-line interfaces with argparse
✅ Logging for real-world debugging
✅ File system operations in Python

To execute the script, run this in Command Prompt (with the Python file available locally):
python sync_script.py <source_directory> <replica_directory> -l <log_file_path>

NOTES

<source_directory>: Folder you want to copy files from. Must exist.

<replica_directory>: Folder to sync to. If it doesn’t exist, the script will create it.

-l <log_file_path>: Full path to the log file where changes will be recorded.

A small step, but an important one as I continue growing in Python, Machine Learning, and Data Science. 💻

Check it out on GitHub 🔗 https://github.com/Novek1
