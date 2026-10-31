# 📊 Poll Results Visualizer

## Project Overview
Poll Results Visualizer is a Python-based data analytics project that processes survey responses, cleans data, performs exploratory data analysis, and creates visualizations through an interactive Streamlit dashboard.

## Features
- Generates sample poll data
- Cleans missing and duplicate records
- Analyses programming tool preferences
- Calculates average satisfaction ratings
- Creates charts using Matplotlib and Seaborn
- Provides an interactive Streamlit dashboard
- Supports age-group filtering

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- WordCloud

## Project Structure
```text
Poll-Results-Visualizer/
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── charts/
│   └── reports/
├── src/
│   ├── __init__.py
│   ├── data_generator.py
│   ├── cleaning.py
│   ├── analysis.py
│   └── visualization.py
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Generate sample data:

```bash
python -m src.data_generator
```

5. Run the analysis:

```bash
python main.py
```

6. Start the dashboard:

```bash
streamlit run app.py
```

## Sample Results
- Total survey responses: 200
- Most popular programming tool: Java
- Average satisfaction rating: 3.12/5

*These results are based on generated sample data.*

## Future Improvements
- Upload custom CSV files
- Add more interactive filters
- Generate downloadable reports
- Add sentiment analysis for feedback
- Deploy the dashboard online

## Author
Meghana