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
I have minimally explored this dataset and my initial hypothisis is that churn is due to the cost associated with services, resulting in a higher monthly payment and concequently higher total payments.

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

 
* Explore data in search of drivers of churn
   * Answer the following initial questions
       * Does higher monthly charges cause churn?
       * Does a higher number of services cause customers to churn more or less?
       * Does having DSL cause customers to churn more or less?
       * Are customers with a lower tenure more or less likely to churn?
       * Is there a service that is associated with more churn than expected?
      
* Develop a model to predict if a customer will churn or not
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions

# Data Dictionary:
### -Column names and descriptions here.

# Steps to Reproduce
### -instructions for reproducing your work. i.e. Running your notebook on someone else's computer.
