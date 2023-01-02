# Where are my customers going?!?!?!
# A Telco customer churn analysis

# Project Description:
The telecommunication industry is massive generating greater than 1.7 billion dollars in 2021 and is expected to almost double by 2028. Companies are constantly looking at customer retention (churn) in order to glean as much as possible from this billion dollar industry. Determining wether a customer will churn or not allows a business to make changes in an attempt to retain their customers. Using the telco_churn dataset, I will identify drivers and determine how they relate to customer churn at the company and hypothisize how to reduce their customer churn.

# Project Goals:
* Get more comfortable using the datascience pipeline
* Find drivers for customer churn at Telco. Why are customers churning?
* Use the drivers identified in exploration to develop a machine learning classification model to accurately predict customer churn
* This information will be used to generate a final report, that a non-data scientist can read, to advise Telco on potential solutions to reduce customer churn, identify the steps taken and why, and document final outcomes and takeaways

# Initial Hypothesis:
I have minimally explored this dataset and my initial hypothisis is that churn is related to monthly charges.

# Project Plan:

* Acquire the data from the Codeup SQL server

* Prepare data
   * Drop columns
       * customer_id
       * contract_type_id
       * payment_type_id
       * internet_service_type_id
   * Get dummies
       * gender
       * dependents
       * partner
       * phone_service
       * multiple_lines
       * online_security
       * online_backup
       * device_protection
       * tech_support
       * streaming_tv
       * streaming_movies
       * paperless_billing
       * contract_type
       * internet_service_type
       * payment_type

* Separate into train, validate, and test datasets
 
* Explore the train data in search of drivers of churn
   * Answer the following initial questions
       * Does higher monthly charges cause churn?
       * Does wether customers have dependents cause them to churn more or less?
       * Does having DSL cause customers to churn more or less?
       * Are customers with a lower tenure more or less likely to churn?
       * Is internet service causing churn?
       * Is no online security causing churn?
      
* Develop a model to predict if a customer will churn or not
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions

# Data Dictionary:

| Feature | Definition |
|:--------|:-----------|
|gender| Male or Female, gender of the customer|
|senior_citizen| 0 or 1, wether the customer is a senior citizen or not|
|partner| Yes or No, wether the customer has a partner or not|
|dependents| Yes or No, wether the customer has dependents or not|
|tenure| how long the customer has been with Telco|
|phone_service| Yes or No, wether the customer has phone service or not|
|mutiple_lines| Yes or No, wether the customer has multiple lines or not|
|online_security| Yes or No, wether the customer has online security or not|
|online_backup| Yes or No, wether the customer has online backup or not|
|device_protection| Yes or No, wether the customer has device_protection or not|
|tech_support| Yes or No, wether the customer has tech_support or not|
|streaming_tv| Yes or No, wether the customer has tv streaming or not|
|streaming_movies| Yes or No, wether the customer has movie streaming or not|
|paperless_billing| Yes or No, wether the customer has enrolled in paperless billing or not|
|monthly_charges| how much each customer pays per month|
|total_charges| how much each customer has payed in their tenure|
|churn| Yes or No, wether the customer has left the company or not|
|contract_type| current contract length of each customer|
|internet_service_type| the type of internet each customer is paying for|
|payment_type| how each customer is sending their payment to Telco|
|signup_date| date of each customers enrollment with Telco|
|churn_month| month that the customer left Telco. 'None' if the customer is still enrolled|

# Steps to Reproduce
### -instructions for reproducing your work. i.e. Running your notebook on someone else's computer.
