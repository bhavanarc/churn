{
 "cells": [
  {
   "cell_type": "code",
   "id": "33f54920-667f-48e9-9f4b-e79eb73dcb27",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load the pre-trained model\n",
    "model_path = 'C:\\Users\\BHAVANA\\Documents\\PP\\rf_model.pkl'\n",
    "with open(C:\\Users\\BHAVANA\\Documents\\PP\\rf_model.pkl, 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "st.title(\"Telecom Customer Churn Prediction\")\n",
    "st.write(\"This app predicts the likelihood of a customer churning based on their usage data.\")\n",
    "\n",
    "# Input fields\n",
    "state = st.selectbox('State', ['AK', 'AL', 'AR', 'CA', 'TX'])  # Add all states\n",
    "account_length = st.number_input(\"Account Length (days)\", min_value=1)\n",
    "voice_plan = st.selectbox(\"Voice Plan\", [\"yes\", \"no\"])\n",
    "voice_messages = st.number_input(\"Voice Messages\", min_value=0)\n",
    "intl_plan = st.selectbox(\"International Plan\", [\"yes\", \"no\"])\n",
    "intl_mins = st.number_input(\"International Minutes\", min_value=0.0)\n",
    "intl_calls = st.number_input(\"International Calls\", min_value=0)\n",
    "intl_charge = st.number_input(\"International Charge\", min_value=0.0)\n",
    "day_mins = st.number_input(\"Day Minutes\", min_value=0.0)\n",
    "day_calls = st.number_input(\"Day Calls\", min_value=0)\n",
    "day_charge = st.number_input(\"Day Charge\", min_value=0.0)\n",
    "eve_mins = st.number_input(\"Evening Minutes\", min_value=0.0)\n",
    "eve_calls = st.number_input(\"Evening Calls\", min_value=0)\n",
    "eve_charge = st.number_input(\"Evening Charge\", min_value=0.0)\n",
    "night_mins = st.number_input(\"Night Minutes\", min_value=0.0)\n",
    "night_calls = st.number_input(\"Night Calls\", min_value=0)\n",
    "night_charge = st.number_input(\"Night Charge\", min_value=0.0)\n",
    "customer_calls = st.number_input(\"Customer Service Calls\", min_value=0)\n",
    "\n",
    "# Prepare input data\n",
    "input_data = np.array([[state, account_length, 1 if voice_plan == \"yes\" else 0, voice_messages, \n",
    "                        1 if intl_plan == \"yes\" else 0, intl_mins, intl_calls, intl_charge,\n",
    "                        day_mins, day_calls, day_charge, eve_mins, eve_calls,\n",
    "                        eve_charge, night_mins, night_calls, night_charge,\n",
    "                        customer_calls]])\n",
    "\n",
    "# Prediction\n",
    "if st.button(\"Predict Churn\"):\n",
    "    prediction = model.predict(input_data)\n",
    "    if prediction[0] == 1:\n",
    "        st.write(\"This customer is likely to churn.\")\n",
    "    else:\n",
    "        st.write(\"This customer is likely to stay.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
