MARKET PULSE
Video Demo: https://youtu.be/xmmlPW7XUeU
Description:

# Market Pulse

Market Pulse is a web-based market dashboard designed to provide a simplified reading of the global market environment.

The application retrieves real market data and combines major equity indexes, market volatility, the US Dollar Index, commodities, and Bitcoin into a market regime score and final diagnosis.

## Features

* Real-time market data retrieval through Yahoo Finance
* Monitoring of major global equity indexes
* Market regime classification:
  * Risk-on
  * Risk-on with caution
  * Neutral / mixed signals
  * Risk-off
  * Risk-off with reversal signals
* VIX and DXY monitoring
* Gold, silver, copper, WTI and Brent analysis
* Bitcoin market direction
* Detection of confirmations and divergences
* Dedicated methodology page explaining the scoring system
* Timestamp showing the latest market data update

## How It Works

The Market Pulse methodology is built around four main stages:

### 1. Equity Market Score

The application monitors 13 major equity indexes from different regions of the world.

Each index with a positive daily variation contributes one point to the equity score, resulting in a score from 0 to 13.

The score is interpreted as follows:

| Score | Market Regime     |
| ----- | ----------------- |
| 0–2   | Strong Risk-off   |
| 3–5   | Moderate Risk-off |
| 6–8   | Neutral           |
| 9–10  | Moderate Risk-on  |
| 11–13 | Strong Risk-on    |

### 2. Market Indicators

After establishing the primary equity-market regime, Market Pulse evaluates additional indicators:

* **VIX:** market volatility and stress
* **DXY:** US dollar strength
* **Gold:** protection
* **Silver:** growth
* **Copper:** economic activity
* **WTI and Brent:** energy market signals
* **Bitcoin:** risk appetite

### 3. Divergences

The application compares the behavior of these indicators with the primary market regime.

For example, if the equity markets indicate a risk-on environment while the VIX is rising, this is treated as a divergence.

The objective is not to interpret each indicator in isolation, but to identify whether different parts of the market are sending consistent or conflicting signals.

### 4. Final Diagnosis

The number of identified divergences is combined with the primary market regime to produce the final diagnosis.

A small number of divergences may be treated as noise, while multiple divergences lead to a more cautious interpretation.

## Project Structure

The project is organized as follows:

* **`app.py`** — Main Flask application. It defines the routes, handles user requests, retrieves market data, and sends information to the templates.

  * **`layout.html`** — Base template shared by the other pages. It contains the common structure of the website, such as the navigation bar and page layout.
  * **`index.html`** — Displays 13 stock exchanges, 6 commodities, BTC, VIX and DXY, in addition to their current values and variations. 
  * **`metodologia.html`** — Displays the methodology behind Market Pulse.
  * **`score.html`** — Main page of the Market Pulse dashboard.

  * **`styles.css`** — Defines the visual appearance and layout of the application.

* **`diagnostico.py`** — The engine behind Market Pulse diagnosis, taking into account the market data and the divergences.

* **`market_data.py`** — Contains the functions responsible for retrieving and processing financial market data used by the application.

* **`score.py`** — Contains the functions responsible for analyzing market indicators and calculating the Market Pulse score and classification based on their performance.

## Technologies

* Python
* Flask
* Jinja
* HTML
* CSS
* yfinance

## Purpose

Market Pulse was developed as a CS50 Final Project.

The project is intended as a market-reading and educational tool. It is not designed to provide investment recommendations or financial advice.

## Author

**Arthur Di Doné**

GitHub: ArthurDiDone
edX: arthur_di_done
