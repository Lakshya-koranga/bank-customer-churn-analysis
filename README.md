# Bank Customer Churn Analysis | Excel, Python, Power BI

**Business problem:** Which customer segments are most likely to leave the bank, and where should the Retention Team act first?

**Skills demonstrated:** Data cleaning, exploratory data analysis (EDA), pivot tables, pandas, DAX measures, Power BI dashboard design, business insights and recommendations

## Results at a glance
| Finding | Result |
|---|---|
| Overall churn rate | 20.4% (2,038 of 10,000 customers) |
| Highest-churn country | Germany, 32.4% (France 16.2%, Spain 16.7%) |
| Highest-churn age group | 48-57, 55.3% |
| Inactive vs active members | 27% vs 14% |
| Female vs male customers | 25.1% vs 16.5% |
| High-risk segment | Inactive customers in Germany aged 48-67: 238 customers, 83.6% churn |

## Recommendation
Prioritise inactive customers aged 48-67 in Germany for a re-activation campaign, and review why customers holding 3 or more products leave.

## Approach
1. **Excel:** cleaned the data and built pivot tables for churn by country, age, activity, products and tenure.
2. **Python (pandas, Google Colab):** reproduced the results with `groupby`, created age bands, isolated the high-risk segment and saved charts.
3. **Power BI (in progress):** interactive dashboard with DAX measures (Churn Rate, Churned Customers, High-Risk Churn), slicers, donut, bar and column charts. A screenshot will be added when it is finished.

## Tools
Microsoft Excel, Python (pandas, matplotlib), Google Colab, Power BI, DAX

## Limitations
- `Complain` is almost perfectly linked to churn (99.5% vs 0.05%), so it was treated as an outcome, not a cause.
- The dataset has no date fields, so the analysis shows who is at risk, not when they leave.
- The 3- and 4-product groups are small (266 and 60 customers).

## How to run the Python script
1. Download the dataset from Kaggle (link below) and keep the CSV in the same folder as the script.
2. Install the libraries: `pip install -r requirements.txt`
3. Run: `python LakshyaKoranga_BankChurnAnalysis.py --data "Customer-Churn-Records.csv"`

The script prints the churn tables and saves charts into an `images` folder.

## Charts
![Churn rate by age group](images/churn_by_age.png)

## Files
- `LakshyaKoranga_BankChurnAnalysis.py` - Python analysis script
- `LakshyaKoranga_ProjectReport.docx` - project report
- `excel/bank_churn_analysis.xlsx` - Excel pivot tables, chart and findings
- `requirements.txt` - Python libraries needed
- `images/` - charts created by the Python script

## Data source
[Kaggle - Bank Customer Churn](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)
