# Tweet Sentiment Analysis

A lightweight Python application that performs sentiment analysis on tweets using **VADER** (Valence Aware Dictionary and sEntiment Reasoner). VADER is specifically attuned to sentiments expressed in social media, handling emojis, slang, capitalization, and punctuation effectively.

## Features

- **Sentiment Classification**: Labels tweets as **Positive**, **Neutral**, or **Negative** based on their compound sentiment score.
- **VADER Sentiment Analysis**: Computes compound polarity scores for each text input.
- **Emoji and Unicode Support**: Properly displays and analyzes emojis commonly found in tweets.
- **Sample Dataset**: Includes a built-in set of sample tweets representing various sentiment categories for quick testing.

## Prerequisites

- **Python**: Version 3.6 or higher.
- **Dependencies**: Listed in [requirements.txt](file:///c:/Users/SRIJONI%20GHOSH/Documents/Coding/tweets-analysis/requirements.txt).

## Installation

1. **Clone or Navigate** to the project directory:
   ```bash
   cd tweets-analysis
   ```

2. **Create and Activate a Virtual Environment** (Recommended):
   ```powershell
   # Create a virtual environment named .venv
   python -m venv .venv

   # Activate on Windows (PowerShell)
   .venv\Scripts\Activate.ps1

   # Activate on Windows (Command Prompt)
   .venv\Scripts\activate.bat

   # Activate on macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the sentiment analysis script:
```bash
python sentiment_analysis.py
```

### Example Output

```text
--- Starting Twitter Sentiment Analysis ---

Tweet 1: "I love the new design of this app! It's so intuitive. 😍"
Sentiment: Positive (Compound Score: 0.8271)
------------------------------------------------------------
Tweet 2: "This update is literally the worst. It keeps crashing on my phone."
Sentiment: Negative (Compound Score: -0.6249)
------------------------------------------------------------
Tweet 3: "Just had my morning coffee. Time to start the day."
Sentiment: Neutral (Compound Score: 0.0)
------------------------------------------------------------

...

--- Analysis Complete ---
```

## How It Works

The script classifies sentiment based on the VADER compound score (which ranges from `-1.0` extremely negative to `1.0` extremely positive):
- **Positive**: Compound score $\ge 0.05$
- **Negative**: Compound score $\le -0.05$
- **Neutral**: Compound score between $-0.05$ and $0.05$
