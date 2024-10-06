# Diabetes Risk Prediction App

## Overview
The Diabetes Risk Prediction App is designed to help users assess their risk of Type II Diabetes based on a set of health-related factors. The app employs a Decision Tree model trained on survey data to provide risk estimations. This project is intended to raise public awareness and encourage individuals at risk to seek medical advice.

## Features
- **User-Friendly Interface**: Utilizes Streamlit for a clean and interactive user experience.
- **Data Input**: Users input their weight, height, age, and other health conditions.
- **BMI Calculation**: Automatically converts weight and height to BMI.
- **Risk Prediction**: Provides a risk assessment using a Decision Tree model.
- **Performance Metrics**: Model accuracy and recall performance are highlighted.

## Installation
To run the application, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/faisal-fida/Diabetes-Risk-Prediction.git
    cd Diabetes-Risk-Prediction
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    streamlit run diabetes_app.py
    ```

## How It Works
1. **Data Collection**: The user inputs their weight, height, age, cholesterol levels, blood pressure, and general health status.
2. **BMI Calculation**: The app calculates the user's BMI based on their weight and height.
3. **Data Preparation**: The input data is transformed to match the format required by the Decision Tree model.
4. **Model Prediction**: The pre-trained Decision Tree model predicts the user's risk level and provides the probability of being at low or high risk for prediabetes.

## Model Training
- **Training Data**: The model is trained on data from the CDC's Behavioral Risk Factor Surveillance System (BRFSS).
- **Feature Engineering**: The model uses features such as BMI, age, high cholesterol, high blood pressure, and general health status.
- **Performance**: The model has an accuracy rate of 70%, with a high focus on recall to identify as many potential diabetes cases as possible.

## Challenges

### Data Quality
- **Issue**: The BRFSS data had missing values and outliers.
- **Solution**: Implemented data cleaning techniques such as imputing missing values and removing outliers to improve model performance.

### Feature Selection
- **Issue**: Selecting the most relevant features for the model was challenging.
- **Solution**: Conducted feature importance analysis and iterative testing to identify the key features.

### Model Performance
- **Issue**: Achieving a balance between accuracy and recall.
- **Solution**: Focused on high recall to ensure the model identifies as many potential diabetes cases as possible, even if it means sacrificing some accuracy.

## Future Work
- **Model Improvement**: Experiment with other machine learning algorithms to improve performance.
- **Additional Features**: Incorporate more health-related features to enhance predictions.
- **User Feedback**: Collect user feedback to continuously improve the app's usability and accuracy.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements or new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- The CDC's Behavioral Risk Factor Surveillance System (BRFSS) for the training data.
- The Streamlit team for their excellent library that made the app development straightforward.

## Contact
For questions or comments, please contact [Faisal Fida](https://github.com/faisal-fida).
