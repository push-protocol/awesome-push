#! /bin/bash

pip install bs4
pip install requests
python scripts/scrap_project_details.py
python scripts/build_project.py
python scripts/scrap_yt_medium.py
python scripts/create_readme.py