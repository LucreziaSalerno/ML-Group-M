#  Group Members

* Lucrezia Salerno, 70098
* Guilherme Morgado, 56857
* Miguel Teixeira, 56529
* Isaac Carvalho, 57045
* Amal Bouilla, 70973
* Guilherme Carvalho, 70364

---

#  Business Problem

*Football clubs waste too much money on overpriced transfers. The global transfer market exceeds billions of euros, yet quite a few high-value signings fail to deliver within two years.*

Mid-tier clubs (€50M–€200M budgets) face the biggest challenge. They cannot afford expensive scouting networks, yet they need to manage their budgets more carefully than elite clubs. Traditional scouting creates market inefficiencies where clubs overpay for hyped players while missing out on hidden gems.

We need a data-driven approach to identify fair player values and uncover undervalued talent before other clubs find them.

 #  Main Insights
 
 The core issue is not the lack of talent, but the inability to correctly identify its true market value.



#  Business Context and Proposed Solution

We position ourselves as a sports analytics startup helping mid-tier football clubs compete with wealthier rivals through data-driven recruitment.

Our solution is a Machine Learning model that predicts fair market values for professional players based on performance, age, league quality, and contract situations.

text
| Component        | Description                                                  |
|-----------------|--------------------------------------------------------------|
| Target client    | Mid-tier clubs with limited scouting budgets                |
| Core product     | ML model predicting fair market values                      |
| Key inputs       | Performance stats, age, league quality, contract situation  |
| Key output       | Ranked list of undervalued players                          |


By identifying players whose statistical performance suggests they are undervalued compared to their market price, the model supports smarter and more efficient transfer decisions.

#  Main insights 

 The model transforms raw data into a competitive advantage in the transfer market.



#  1 Introduction

The football transfer market is a highly competitive and financially intensive environment, where clubs invest billions of euros in player acquisitions every year. Despite this, many transfers fail to deliver the expected return, particularly in the case of high-value players.

This inefficiency is especially problematic for mid-tier clubs, where financial errors have a larger impact. Traditional scouting methods are often subjective and limited, leading to systematic overvaluation of visible players and undervaluation of hidden talent.

This project introduces a Machine Learning-based approach to estimate player market value and identify inefficiencies in the transfer market.

#  Main insights

Data-driven decision-making is essential to reduce risk and improve recruitment efficiency.



#  2 Project Architecture

The project follows a modular Machine Learning pipeline:

text
Raw Data → Data Loading → Data Cleaning → Feature Engineering → Modeling → Evaluation


ML-Group-M/
│
├── data/
├── notebooks/
├── data_loading.py
├── data_cleaning.py
├── feature_engineering.py


#  Main insights 

A modular pipeline ensures reproducibility and makes the system scalable and maintainable.



#  3 Dataset Construction

The dataset is built by merging multiple data sources, each contributing a different dimension of player information.


| Source Type        | Description                          |
|-------------------|--------------------------------------|
| Player Profiles   | Age, position, club                  |
| Performance Data  | Goals, assists, minutes              |
| Market Values     | Historical and current values        |
| Injuries          | Injury frequency                     |
| Team & League     | Competition level                    |


#  Main insights 

Combining multiple sources allows the model to capture both performance and context, which are essential for accurate valuation.



#  4 Data Preprocessing

The dataset undergoes several transformations to ensure consistency and reliability:


| Step                     | Description                           |
|--------------------------|---------------------------------------|
| League normalization     | Standardizes competition names        |
| Missing values handling  | Performance → 0, categorical → "Unknown" |
| Date conversion          | Enables time-based features           |
| Feature filtering        | Removes irrelevant columns            |


#  Main insights 

Clean data is fundamental — without it, model predictions would be unreliable.



#  5 Feature Engineering

Feature engineering is a key strength of the project and significantly enhances model performance.


| Feature Group        | Examples                            |
|---------------------|--------------------------------------|
| Age & Career        | Age, age², career phase              |
| Contract            | Contract duration, free agent status |
| League Context      | League quality score                 |
| Performance         | Goals/90, assists/90                 |
| Health              | Injury proneness                     |


Advanced features and interaction terms allow the model to capture complex relationships.

#  Main insights 

Strong feature engineering is the main driver of predictive performance in this project.



#  6 Machine Learning Approach

The problem is formulated as a regression task, where the goal is to predict player market value.

The models are trained on engineered features that combine performance, context, and career information.

#  Main insights 

Regression allows direct estimation of financial value, making the model highly applicable in real-world decisions.



# 7  Model Evaluation


| Metric | Description                          |
|--------|--------------------------------------|
| MAE    | Average prediction error             |
| MSE    | Penalizes large errors               |
| R²     | Variance explained                   |


#  Main insights 

Using multiple metrics ensures a robust and reliable evaluation of model performance.



#  8 Results and Insights

The model successfully captures key relationships between player attributes and market value.

Feature engineering, particularly normalized performance and league quality, plays a major role in improving predictions.

#  Main insights 

The model not only predicts values but also identifies market inefficiencies, enabling the discovery of undervalued players.



#  9 Business Impact

The model provides a practical tool for improving recruitment strategies.

It enables clubs to:

* Identify undervalued players
* Avoid overpriced transfers
* Optimize resource allocation

#  Main insights 

The project bridges the gap between data analysis and real-world decision-making.



#  10 Future Work

Future improvements may include advanced metrics, real-time data integration, and more sophisticated models.

#  Main insights 

The current solution is strong but has clear potential for further development and real-world deployment.



#  11 Final Conclusion


This project demonstrates how Machine Learning can be effectively applied to a real-world problem in sports analytics, specifically in the context of football player valuation and recruitment.

By combining multiple data sources, a structured preprocessing pipeline, and extensive feature engineering, we transformed raw football data into a meaningful and predictive representation of player value. The model leverages performance metrics, contextual variables such as league quality, and career-related features to estimate market value with a strong degree of realism.

More importantly, the value of this project lies beyond prediction itself. By comparing predicted values with actual market prices, the system enables the identification of inefficiencies in the transfer market, highlighting players who may be undervalued or overpriced. This directly supports smarter and more strategic decision-making.

From a technical perspective, the project showcases:

* A modular and reproducible Machine Learning pipeline
* Strong data integration and preprocessing practices
* High-quality feature engineering grounded in domain knowledge
* A regression-based approach aligned with real financial outcomes

From a business perspective, the project delivers:

* A scalable tool for player valuation
* A framework for identifying undervalued talent
* A data-driven alternative to traditional scouting limitations

To sum up the conclusion on our work we think the key achievement of this project is not only building a predictive model, but creating a system that converts complex football data into actionable insights, enabling clubs to reduce risk, optimize investments, and gain a competitive advantage in the transfer market.
