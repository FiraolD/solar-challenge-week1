# MoonLight Energy Solutions - Solar Challenge Week 1

**Description**: This Data Analysis project is implemented In particular,  to present a strategy focusing on identifying high-potential regions for solar installation that align with the company's long-term sustainability goals. so, we will first analyze the datas from the 3 countries by cleaning and implementing EDA to each country and then finally comparing them to see which region has the highest potential for solar grids to be installed in the region.

⚙️ Steps: 
1.Initialize GitHub Repository

•Create repo named solar-challenge-week1 on GitHub.
•Clone it locally:
bash
git clone https://github.com/FiraolD/solar-challenge-week1.git 

cd solar-challenge-week1

🛠️ Development Environment Setup

- Python 3.11.0 installed
- Git installed
- VScode Installed and Extensions installed
- All requirements installed

📁 Project Structure & Organization

-data/ folder is in .gitignore (no raw CSVs committed)
-Folders: notebooks/, scripts/, app/, tests/, src/, etc., are clean and well-named
-Only cleaned/exported data is read from local files in notebooks and app

  
 📊 Notebooks

-Each EDA notebook (benin_eda.ipynb, etc.) starts with a title and objective
-Code cells are ordered, readable, and documented with markdown explanation
-Visualizations are labeled with axis titles and legends
-Outliers and missing values handled and explained
-Final cleaned CSVs saved (but not committed)
-Cross-Country Comparison performed
- Using the result of the comparison strategies drawn to identifying high-potential regions for solar installation

⚙️ CI/CD

-.github/workflows/ci.yml runs pip install -r requirements.txt successfully
-Workflow passes for every push or PR to main

📈 Dashboard (Streamlit App)

-Interactive elements (e.g., dropdown to select country)
-Visualizations like GHI boxplot, top region insights, etc.
-App loads cleaned data locally (data/<country>_clean.csv)
-App runs without errors (streamlit run app/main.py)
