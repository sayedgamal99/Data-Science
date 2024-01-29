# Outline

- [1 - Problem Statement](#11)
- [2 - About the Dataset](#12)

### Exploratory Data Analysis
- [3 - In Mind Questions](#13)
- [4 - EDA Conclusion](#15)

### Machine Learning

- [5 - Best Model](#1best)

<a name ='11'></a>

# 1- Problem Statement

### Context
- Identify customer satisfaction is a key element for modern businesses as it can significantly contribute to a continuing effort of service quality improvement. In order to meet customer expectations and achieve higher quality levels, airlines needs to develop a specific mechanism of passenger satisfaction measurement.

- This is a <font color = 'steelblue' size=4>classification</font> supervised machine learning project, Predicting Satisfaction of Airline Passengers.


<br>

<a name ='12'></a>

# 2- About the Dataset :

This dataset contains an airline passenger satisfaction survey. What factors are highly correlated to a satisfied (or dissatisfied) passenger? Can you predict passenger satisfaction?

This dataset is obtained from Kaggle: [Airline Passenger Satisfaction](https://www.kaggle.com/datasets/mysarahmadbhat/airline-passenger-satisfaction)

____________________________________________________________________________
## 2.1 Data Description :

<br>

`Gender`: Gender of the passengers (Female, Male)

`Customer Type`: The customer type (Loyal customer, disloyal customer)

`Age`: The actual age of the passengers

`Type of Travel`: Purpose of the flight of the passengers (Personal Travel, Business Travel)

`Class`: Travel class in the plane of the passengers (Business, Eco, Eco Plus)

`Departure Delay in Minutes`: Minutes delayed when departure

`Arrival Delay in Minutes`: Minutes delayed when Arrival
    
`Departure/Arrival time convenient`: Satisfaction level of Departure/Arrival time convenient

`Flight distance`: The flight distance of this journey

`Inflight wifi service`: Satisfaction level of the inflight wifi service (0:Not Applicable;1-5)

`Ease of Online booking`: Satisfaction level of online booking

`Gate location`: Satisfaction level of Gate location

`Food and drink`: Satisfaction level of Food and drink

`Online boarding`: Satisfaction level of online boarding

`Seat comfort`: Satisfaction level of Seat comfort

`Inflight entertainment`: Satisfaction level of inflight entertainment

`On-board service`: Satisfaction level of On-board service

`Leg room service`: Satisfaction level of Leg room service

`Baggage handling`: Satisfaction level of baggage handling

`Check-in service`: Satisfaction level of Check-in service

`Inflight service`: Satisfaction level of inflight service

`Cleanliness`: Satisfaction level of Cleanliness

`Satisfaction`: Airline satisfaction level(Satisfaction, neutral or dissatisfaction)
_________________________________________________________________________________

<a name ='13'></a>

# 3- In Mind Questions
- General Questions related to the existence of
  - missing values?
  - wrong datatypes for columns?
  - complete duplicates in the data?
  - outliers in each column?

- `Univariate Analysis`
1. What is the most common type of travel among passengers?
2. What is the average age of passengers?
3. What is the distribution of flight distances?
4. What percentage of passengers face delays between 20 minutes to 60 minutes?
5. Which services received good ratings from passengers?
6. Which services received poor ratings from passengers?
7. What is the overall satisfaction level of passengers?


- `Bivariate Questions`

1. How does age distribution differ among passengers based on their type of travel, satisfaction level, customer type, and class?
2. What are the characteristics of older and younger passengers?
3. How does flight distance distribution differ among passengers based on their type of travel, satisfaction level, customer type, and class?
4. What are the characteristics of passengers who traveled long distances?
5. How does customer satisfaction differ between returning and first-time customers?
6. How does customer satisfaction differ among passengers based on their class and type of travel?
7. Which services received the best and worst ratings from passengers?
8. How does service rating differ among passengers based on their flight class, customer type, satisfaction level, gender, and type of travel?
9. Is there a relationship between departure and arrival delay times?
10. Does total time delay have any relation with type of travel, satisfaction, gender, class, or customer type?




______________________________________________________________________________________

<a name ='15'></a>

# 4- Conclusion

### Age Distributions for Passengers
- `Older Passengers` tend to be:
    - `Satisfied`, `Returning Customers`, `Business Class`.

- `Younger Passengers` tend to be:
    - `Dissatisfied`, `First time Customers`, `Economy Class`.
- Age Distributed `Equally` for Passengers `Gender`.

### Flight distance Distributions for Passengers
- `Business` type of travel, `Satisfied` Passengers, `Business Class`, `Returning Customers`. All traveled long distances.

- `Gender` and `Total Time Delay` Categories have the same distribution for Kilometers Traveled.

### Categories
- `Returning` Customer type is almost `Equally` (satisfied & dissatisfied), but `First time` Customers `not satisfied at all`.

- `Business Class` is `More Satisfied`, unlike `Economy & Eco Plus` Class which is mostly `not satisfied`.

- `Business` Type of Travel is `More Satisfied`, unlike `Personal` type which is mostly `not satisfied`.

- `Gender` is almost `Equally` for Satisfied (or not) Men and Women.

### Services
- `In-Flight Service`, `Baggage Handling`, and `Seat Comfort` are the best 3 Services by Passengers Rating.

- `Wifi`, `Ease of Online Booking`, `Gate Location` services received poor ratings from Passengers.
- Service Rating for `Flight Classes`:
    - Overview: `Busniness Class` gives `higher ratings` for services.
    - `Gate location` got poor rating by `business class`.
    - `Time Delays` got poor rating by `business class`.
    - `Wifi` got `worst` rating by `economy class`, same as `online booking`.

- Service Rating for `Type of Customer`:
    - Overview: `Returning Customers` give `higher ratings`.
    - `Online boarding`, `Seat Comfort`, `In flight entertainment` received `High rating` for `Returning customers`, while got `poor Rating` for `first time customers`.

- Service Rating for `Satisfaction`:
    - Overview: `Satisfied` Passengers give `High Ratings` for services.
    - `Gate Location` service got `Moderate and Equal Rate` for both (Satisfied and dissatisfied) Passengers.

- Service Rating for `Gender`:
    - Overview: almost all services got `close rates` for both genders.

- Service Rating for `Type of Travel`:
    - Overview: `Busniness` gives `higher ratings` for services.
    - `Delay Times` got `Excellent rate` by `Personal Type`, Unlike for `Business type`.
    - `Check in Service` got `Moderate and Equal Rate` for both (Personal and Business) type of Passengers.

### Delays
- `Strong` Relationship between Departure and Arrival Delay Times.

- `Total time delay` has no Relation with any of (type of Travel, Satisfaction, Gender, Class and Customer type), and is `distributed equally`.



______________________________________________________________________________________

<a name = '1best'></a>

# 5- 💡 Best Model

- `Tree` based models exhibited a good fit for the data.
- The `XGBOOST` classifier achieved the highest training and validation `f1-scores`: `%95` and `%93`, respectively.
- The model tuning process was effective, selecting `11` as the `max-depth`, `100` for the number of `estimators`, and `0.1` as the `learning rate`.
- Model tuning resulted in impressive accuracy (f1-score) for both training and validation: `%98` and `%96`, respectively.
- Performance evaluation on the test dataset indicates the model's fitting capability, yielding `%96`, which suggests that the model doesn't suffer from overfitting and `fits well`.

<br>
<br>

---




