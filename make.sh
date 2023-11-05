#! /bin/bash

pip install -r requirements.txt
python scripts/scrap_project_details.py
python scripts/build_project.py
python scripts/scrap_yt_medium.py
python scripts/create_readme.py