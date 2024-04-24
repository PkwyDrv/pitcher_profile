
# Pitcher Profile

This app analyzes individual MLB pitcher arsenals based on pitch type, featuring pitch usage, whiff percent, strike percent, and hard hit percent data for the 2023 MLB regular season.
    * **Python libraries:** streamlit, pandas, plotly.express, numpy, pybaseball, and seaborn
    * **Data source:** [baseballsavant.mlb.com](https://baseballsavant.mlb.com/)

## Link

- [Web App](https://pitcher-profile.onrender.com)


## Authors

- [@PkwyDrv](https://www.github.com/PkwyDrv)


## Installation

Install pitcher_profile from repository

Check your python version:
```bash
  > python -V
```
1. Install Git:

  Install Git: - [Git Downloads](https://git-scm.com/downloads)

2. Open a terminal or command prompt and navigate to the directory where the project will be stored. Then, use the git clone command followed by the repository URL to clone it to their local machine:

```bash
  git clone https://github.com/PkwyDrv/pitcher_profile
  python app.py
```

3. Navigate to the Project Directory:

```bash
  cd pitcher_profile
```

4. You can install the latest version of pip using the following. This command will automatically install the latest pip version:

  python(version#) -m pip install --user --upgrade pip

5. Set Up a Virtual Environment (Optional but Recommended):
It's a good practice to create a virtual environment to isolate the project's dependencies. Create a virtual environment using venv module if using Python 3:

  Install venv:
    python(version#) -m pip install --user virtualenv

  Create virtual environment:
    python(version#) -m venv venv
  
6. Activate your virtual environment
Before using your virtual environment on your project, you need to activate it using:

  Unix/MacOS:

  ```bash
  source venv/bin/activate
  ```
  Windows:

  venv\Scripts\activate

7. Install Dependencies:

```bash
  pip install requirements.txt
```
8. Run the Application:

```bash
  python app.py
```


## Requirements
python==3.12.0

pandas==2.2.2

scipy==1.13.0

streamlit==1.33.0

altair==5.3.0

plotly==5.21.0

pybaseball==2.2.7