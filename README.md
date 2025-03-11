# Project: Stock Market Data and Analysis

## Description
This project aims to analyze and explore the relationship between news headlines and stock market movements. By performing Exploratory Data Analysis (EDA) on news data, the project seeks to uncover insights such as sentiment trends, publication patterns, and publisher activity. Additionally, technical indicators and quantitative analysis will be integrated using financial data to examine stock price movements.

## Key Objectives
- **Task 1**: Set up Git version control, CI/CD workflows, and a Python development environment.
- **Task 2**: Perform exploratory data analysis (EDA) on news headline data, focusing on descriptive statistics, sentiment analysis, and time series trends.
- **Task 3**: Quantify the correlation between news sentiment and stock price movements (upcoming).

### Task 1: Git and GitHub
- A GitHub repository was created with a structured folder layout:
  ```
  ├── .vscode/
  │   └── settings.json
  ├── .github/
  │   └── workflows
  │       └── unittests.yml
  ├── requirements.txt
  ├── README.md
  ├── src/
  │   └── __init__.py
  ├── notebooks/
  │   └── README.md
  ├── tests/
  │   └── __init__.py
  └── scripts/
      └── README.md
  ```
- Implemented CI/CD using GitHub Actions with a `unittests.yml` workflow to automate testing on each commit.
- Created and actively used a dedicated branch for Task 1 (`task-1`), committing changes with clear and descriptive messages.

### Task 2: Exploratory Data Analysis (Partial Progress)
#### Methodology:
1. **Descriptive Statistics**:
   - Analyzed headline lengths and counted articles per publisher to identify active contributors.
   - Investigated trends in publication dates, revealing spikes during significant market events.

2. **Text Analysis**:
   - Performed sentiment analysis using `TextBlob` to classify headlines as positive, negative, or neutral.
   - Extracted common keywords and topics using Natural Language Processing (NLP) techniques.

3. **Time Series Analysis**:
   - Plotted publication frequency over time to detect spikes and patterns.
   - Analyzed publishing times to identify peak activity periods.


