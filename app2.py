# import streamlit as st
# import numpy as np
# import pandas as pd
# import pickle
# import requests
# from PIL import Image
# from io import BytesIO
# import cv2
# from main_code import input_image1
# from application_both_models import all_task
# from sqlalchemy import create_engine, Column, Integer, String, Float, Date
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import datetime
# import requests
# # https://inloop.github.io/sqlite-viewer/
#
# Base = declarative_base()
#
# class Prescription(Base):
#     __tablename__ = 'Prescriptions'
#     id = Column(Integer, primary_key=True)
#     date = Column(Date, default=datetime.datetime.now)
#     username = Column(String)  # New field to store username
#     doctor_name = Column(String)
#     medicine_name = Column(String)
#     company_name = Column(String)
#     price = Column(Float)
#
# engine = create_engine('sqlite:///Mediscan.db')
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# def clear_prescriptions_db():
#     """Clear all entries from the 'prescriptions' table."""
#     try:
#         # Delete all records from the Prescription table
#         session.query(Prescription).delete()
#         # Commit the changes to the database
#         session.commit()
#         print("All records have been deleted successfully from the database.")
#     except Exception as e:
#         # If an error occurs, rollback any changes and print the error
#         session.rollback()
#         print(f"An error occurred: {e}")
#
# clear_prescriptions_db()
#
# # Telegram credentials
# TOKEN = "7047754135:AAG8fFEA1lDVe21bQYYTozv3gb_wpf3-5hs"  # Use an environment variable or secure method to store this
# chat_id = "1893904443"  # Use an environment variable or secure method to store this
#
# def send_telegram_message(report_message):
#     """Send a message to a predefined Telegram chat."""
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={report_message}"
#     response = requests.get(url)
#     return response.json()
#
# def create_report_and_send():
#     """Generate a report from the database and send it via Telegram for the three most recent prescriptions."""
#     # Fetch the last three added prescriptions based on the highest ID
#     recent_prescriptions = session.query(Prescription).order_by(Prescription.id.desc()).limit(3).all()
#     for prescription in recent_prescriptions:
#         message = (f"Username: {prescription.username}\n"
#                    f"Date: {prescription.date}\n"
#                    f"Doctor: {prescription.doctor_name}\n"
#                    f"Medicine: {prescription.medicine_name}\n"
#                    f"Company: {prescription.company_name}\n"
#                    f"Price: ${prescription.price:.2f}")
#         # Send the message for each of the three most recent prescriptions
#         send_telegram_message(message)
#
#
#
# st.set_page_config(page_title="Mediscan", layout="wide")
#
# users = {
#     "Ravi": {"password": "Ravi123", "doctor_name": "Dr. Gupta"},
#     "Pragathi": {"password": "Pragathi123", "doctor_name": "Dr. Kapoor"},
#     "Vinay": {"password": "Vinay123", "doctor_name": "Dr. Reddy"},
#     "Naveetha": {"password": "Naveetha123", "doctor_name": "Dr. Kaur"},
#     "Namratha": {"password": "Namratha123", "doctor_name": "Dr. Patel"},
#     "Ankitha": {"password": "Ankitha123", "doctor_name": "Dr. Mehta"},
#     "Arun": {"password": "Arun123", "doctor_name": "Dr. Sharma"},
#     "Ranjith": {"password": "Ranjith123", "doctor_name": "Dr. Chandra"},
#     "Arpitha": {"password": "Arpitha123", "doctor_name": "Dr. Iyer"},
#     "Mounesh": {"password": "Mounesh123", "doctor_name": "Dr. Desai"},
#     "Sanjay": {"password": "Sanjay123", "doctor_name": "Dr. Joshi"},
#     "Vineetha": {"password": "Vineetha123", "doctor_name": "Dr. Bhat"},
#     "Kruthi": {"password": "Kruthi123", "doctor_name": "Dr. Anand"},
#     "Praneeth": {"password": "Praneeth123", "doctor_name": "Dr. Srinivasan"},
#     "Ramesh": {"password": "Ramesh123", "doctor_name": "Dr. Thakur"},
#     "Rakshitha": {"password": "Rakshitha123", "doctor_name": "Dr. Ramesh"},
# }
#
#
#
# def check_login(username, password):
#     """Check if the username and password are in the simulated database and if the doctor_name matches."""
#     user_info = users.get(username)
#     if user_info and user_info['password'] == password:
#         return True, user_info['doctor_name']
#     else:
#         return False, ""
#
#
#
# # Initialize session state variables
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False
#     st.session_state['username'] = ""
#     st.session_state['doctor_name'] = ""
#
# # Sidebar for login
# if not st.session_state['logged_in']:
#     st.sidebar.title("Login")
#     st.markdown("""
#                          <h1 style='text-align: center; color: gray;'>
#                              DOCTOR MEDICAL PRESCRIPTION RECOGNITION
#                          </h1>
#                          """, unsafe_allow_html=True)
#     st.sidebar.image("Streamlit Images/sidebar_logo.png", use_column_width=True)
#     st.image('Streamlit Images/Cover page.png')
#
#
#     st.markdown("""
#             <div style='font-family: Arial, sans-serif;'>
#                 <h3>Welcome to Your Digital Prescription Assistant!</h3>
#                 <strong>Transforming Healthcare with Advanced AI Technology</strong>
#                 <p>
#                     Our platform specializes in the digital transformation of handwritten medical prescriptions into accurately digitized formats. Powered by cutting-edge artificial intelligence and machine learning technologies, our solution offers a seamless and reliable way to interpret and manage prescriptions written by doctors.
#                 </p>
#                 <h4>Key Features:</h4>
#                 <ul>
#                     <li><strong>Precision Recognition:</strong> Utilize our state-of-the-art optical character recognition (OCR) technology that expertly handles the intricacies of diverse handwriting styles, ensuring high accuracy in translating handwritten notes to digital text.</li>
#                     <li><strong>Instant Digitization:</strong> Convert handwritten prescriptions into digital formats in real-time, reducing the waiting time and potential errors associated with manual data entry.</li>
#                     <li><strong>Enhanced Accessibility:</strong> Access digitized prescriptions anytime and anywhere, fostering better communication between pharmacies, healthcare providers, and patients.</li>
#                     <li><strong>Secure and Compliant:</strong> Adhering to the strictest data protection standards, our platform guarantees the confidentiality and security of all medical documents.</li>
#                     <li><strong>User-Friendly Interface:</strong> Whether you're a doctor, pharmacist, or a healthcare administrator, our platform is designed for ease of use without requiring specialized training.</li>
#                 </ul>
#                 <h4>Benefits for Healthcare Professionals and Patients:</h4>
#                 <ul>
#                     <li><strong>Error Reduction:</strong> Minimize the risks of prescription misinterpretation due to illegible handwriting, ensuring patients receive the correct medications.</li>
#                     <li><strong>Efficiency Improvements:</strong> Streamline the prescription processing workflow, saving valuable time for healthcare professionals and enhancing patient care.</li>
#                     <li><strong>Data Integration:</strong> Easily integrate digitized data with existing electronic health records (EHRs), improving record-keeping and patient management.</li>
#                 </ul> """,unsafe_allow_html=True)
#
#     st.image('Streamlit Images/login2.png')
#
#     st.markdown("""
#         <div style='font-family: Arial, sans-serif;'>
#         <h4>Who Can Benefit?</h4>
#                 <ul>
#                     <li><strong>Medical Practitioners:</strong> Doctors who wish to improve the clarity and management of their prescriptions.</li>
#                     <li><strong>Pharmacists:</strong> Pharmacy staff looking to enhance prescription accuracy and customer service.</li>
#                     <li><strong>Healthcare Institutions:</strong> Hospitals and clinics aiming to modernize patient care and administrative processes.</li>
#                     <li><strong>Patients:</strong> Individuals seeking a better understanding and management of their prescribed treatments.</li>
#                 </ul>
#                 <p><strong>Join us in revolutionizing the management of medical prescriptions. Our platform bridges the gap between traditional handwriting and digital healthcare, enhancing the efficiency and accuracy of medical services worldwide.</strong></p>
#                 <p><strong>Experience the future of healthcare—digitized, streamlined, and error-free.</strong></p>
#             </div> """,unsafe_allow_html=True)
#
#
#     username = st.sidebar.text_input("Username")
#     password = st.sidebar.text_input("Password", type="password")
#     doctor_name = st.sidebar.text_input("Doctor's Name")
#
#     if st.sidebar.button("Login"):
#         valid, doctor = check_login(username, password)
#         if valid and doctor_name.strip().lower() == doctor.lower():
#             st.session_state['logged_in'] = True
#             st.session_state['username'] = username
#             st.session_state['doctor_name'] = doctor
#             st.success(f"Logged in as {username}")
#         else:
#             st.error("Invalid credentials or doctor's name does not match")
#
#     # Main app functionality
# if st.session_state['logged_in']:
#     st.markdown("""
#                              <h1 style='text-align: center; color: gray;'>
#                                  DOCTOR MEDICAL PRESCRIPTION RECOGNITION
#                              </h1>
#                              """, unsafe_allow_html=True)
#
#     st.image('Streamlit Images/login.png', use_column_width=True)
#     uploaded_file = st.file_uploader("Choose an image...", type="jpeg")
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption='Uploaded Image.', use_column_width=True)
#         try:
#             prediction = all_task()
#             with open('medicine_names.txt', 'r') as file:
#                 actual_medicine_names = [line.strip() for line in file]
#
#             def get_best_match(predicted_name, actual_names):
#                 matches = process.extractOne(predicted_name, actual_names, scorer=fuzz.token_sort_ratio)
#                 return matches
#
#             improved_predictions = []
#             for predicted_name in prediction:
#                 best_match, similarity_score = get_best_match(predicted_name, actual_medicine_names)
#                 improved_predictions.append(best_match)
#
#             for prediction in improved_predictions:
#                 st.markdown(f"<h3>{prediction}</h3>", unsafe_allow_html=True)
#
#             medicine_data = pd.read_csv('medicine_data.csv')
#             lowest_price_details = []
#             for medicine_name in improved_predictions:
#                 filtered_data = medicine_data[medicine_data['medicine_name'] == medicine_name]
#                 if not filtered_data.empty:
#                     lowest_price_row = filtered_data.loc[filtered_data['price'].idxmin()]
#                     lowest_price_details.append({
#                         'medicine_name': medicine_name,
#                         'company_name': lowest_price_row['company_name'],
#                         'price': lowest_price_row['price']
#                     })
#                     new_prescription = Prescription(username=st.session_state['username'], doctor_name=st.session_state['doctor_name'], medicine_name=medicine_name, company_name=lowest_price_row['company_name'], price=lowest_price_row['price'])
#                     session.add(new_prescription)
#             session.commit()
#
#             lowest_price_details_df = pd.DataFrame(lowest_price_details)
#             st.write("# Best Companies and Best Price for the Following Medicines:")
#             st.dataframe(lowest_price_details_df)
#
#             if st.button("Send the Report"):
#                 create_report_and_send()
#                 st.success("Report sent to Registered User!")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#             session.rollback()


import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
from PIL import Image
from io import BytesIO
import cv2
from main_code import input_image1
from application_both_models import all_task
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import requests

Base = declarative_base()

class Prescription(Base):
    __tablename__ = 'Prescription'
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.datetime.now)
    doctor_name = Column(String)
    medicine_name = Column(String)
    company_name = Column(String)
    price = Column(Float)

engine = create_engine('sqlite:///Mediscan.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Telegram credentials
TOKEN = "7047754135:AAG8fFEA1lDVe21bQYYTozv3gb_wpf3-5hs"  # Use an environment variable or secure method to store this
chat_id = "1893904443"  # Use an environment variable or secure method to store this

def send_telegram_message(report_message):
    """Send a message to a predefined Telegram chat."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={report_message}"
    response = requests.get(url)
    return response.json()

def clear_prescriptions_db():
    """Clear all entries from the 'prescriptions' table."""
    try:
        # Delete all records from the Prescription table
        session.query(Prescription).delete()
        # Commit the changes to the database
        session.commit()
        print("All records have been deleted successfully from the database.")
    except Exception as e:
        # If an error occurs, rollback any changes and print the error
        session.rollback()
        print(f"An error occurred: {e}")

clear_prescriptions_db()

def create_report_and_send():
    """Generate a report from the database and send it via Telegram for the three most recent prescriptions."""
    # Fetch the last three added prescriptions based on the highest ID
    recent_prescriptions = session.query(Prescription).order_by(Prescription.id.desc()).limit(3).all()
    for prescription in recent_prescriptions:
        message = (f"Username: {prescription.username}\n"
                   f"Date: {prescription.date}\n"
                   f"Doctor: {prescription.doctor_name}\n"
                   f"Medicine: {prescription.medicine_name}\n"
                   f"Company: {prescription.company_name}\n"
                   f"Price: ${prescription.price:.2f}")
        # Send the message for each of the three most recent prescriptions
        send_telegram_message(message)

    # Send each prescription as a separate message or as a single message
    for message in report_messages:
        send_telegram_message(message)

st.set_page_config(page_title="Mediscan", layout="wide")

users = {
    "Ravi": {"password": "Ravi123", "doctor_name": "Dr. Gupta"},
    "Pragathi": {"password": "Pragathi123", "doctor_name": "Dr. Kapoor"},
    "Vinay": {"password": "Vinay123", "doctor_name": "Dr. Reddy"},
    "Naveetha": {"password": "Naveetha123", "doctor_name": "Dr. Kaur"},
    "Namratha": {"password": "Namratha123", "doctor_name": "Dr. Patel"},
    "Ankitha": {"password": "Ankitha123", "doctor_name": "Dr. Mehta"},
    "Arun": {"password": "Arun123", "doctor_name": "Dr. Sharma"},
    "Ranjith": {"password": "Ranjith123", "doctor_name": "Dr. Chandra"},
    "Arpitha": {"password": "Arpitha123", "doctor_name": "Dr. Iyer"},
    "Mounesh": {"password": "Mounesh123", "doctor_name": "Dr. Desai"},
    "Sanjay": {"password": "Sanjay123", "doctor_name": "Dr. Joshi"},
    "Vineetha": {"password": "Vineetha123", "doctor_name": "Dr. Bhat"},
    "Kruthi": {"password": "Kruthi123", "doctor_name": "Dr. Anand"},
    "Praneeth": {"password": "Praneeth123", "doctor_name": "Dr. Srinivasan"},
    "Ramesh": {"password": "Ramesh123", "doctor_name": "Dr. Thakur"},
    "Rakshitha": {"password": "Rakshitha123", "doctor_name": "Dr. Ramesh"}
}


def check_login(username, password):
    """Check if the username and password are in the simulated database."""
    user_info = users.get(username)
    if user_info and user_info['password'] == password:
        return True, user_info['doctor_name']
    else:
        return False, ""


# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""
    st.session_state['doctor_name'] = ""

# Sidebar for login
if not st.session_state['logged_in']:
    st.sidebar.title("Login")
    st.markdown("""
                     <h1 style='text-align: center; color: gray;'>
                         DOCTOR MEDICAL PRESCRIPTION RECOGNITION
                     </h1>
                     """, unsafe_allow_html=True)
    st.sidebar.image("Streamlit Images/sidebar_logo.png", use_column_width=True)
    st.image('Streamlit Images/Cover page.png')


    st.markdown("""
        <div style='font-family: Arial, sans-serif;'>
            <h3>Welcome to Your Digital Prescription Assistant!</h3>
            <strong>Transforming Healthcare with Advanced AI Technology</strong>
            <p>
                Our platform specializes in the digital transformation of handwritten medical prescriptions into accurately digitized formats. Powered by cutting-edge artificial intelligence and machine learning technologies, our solution offers a seamless and reliable way to interpret and manage prescriptions written by doctors.
            </p>
            <h4>Key Features:</h4>
            <ul>
                <li><strong>Precision Recognition:</strong> Utilize our state-of-the-art optical character recognition (OCR) technology that expertly handles the intricacies of diverse handwriting styles, ensuring high accuracy in translating handwritten notes to digital text.</li>
                <li><strong>Instant Digitization:</strong> Convert handwritten prescriptions into digital formats in real-time, reducing the waiting time and potential errors associated with manual data entry.</li>
                <li><strong>Enhanced Accessibility:</strong> Access digitized prescriptions anytime and anywhere, fostering better communication between pharmacies, healthcare providers, and patients.</li>
                <li><strong>Secure and Compliant:</strong> Adhering to the strictest data protection standards, our platform guarantees the confidentiality and security of all medical documents.</li>
                <li><strong>User-Friendly Interface:</strong> Whether you're a doctor, pharmacist, or a healthcare administrator, our platform is designed for ease of use without requiring specialized training.</li>
            </ul>
            <h4>Benefits for Healthcare Professionals and Patients:</h4>
            <ul>
                <li><strong>Error Reduction:</strong> Minimize the risks of prescription misinterpretation due to illegible handwriting, ensuring patients receive the correct medications.</li>
                <li><strong>Efficiency Improvements:</strong> Streamline the prescription processing workflow, saving valuable time for healthcare professionals and enhancing patient care.</li>
                <li><strong>Data Integration:</strong> Easily integrate digitized data with existing electronic health records (EHRs), improving record-keeping and patient management.</li>
            </ul> """,unsafe_allow_html=True)

    st.image('Streamlit Images/login2.png')

    st.markdown(""" 
    <div style='font-family: Arial, sans-serif;'>
    <h4>Who Can Benefit?</h4>
            <ul>
                <li><strong>Medical Practitioners:</strong> Doctors who wish to improve the clarity and management of their prescriptions.</li>
                <li><strong>Pharmacists:</strong> Pharmacy staff looking to enhance prescription accuracy and customer service.</li>
                <li><strong>Healthcare Institutions:</strong> Hospitals and clinics aiming to modernize patient care and administrative processes.</li>
                <li><strong>Patients:</strong> Individuals seeking a better understanding and management of their prescribed treatments.</li>
            </ul>
            <p><strong>Join us in revolutionizing the management of medical prescriptions. Our platform bridges the gap between traditional handwriting and digital healthcare, enhancing the efficiency and accuracy of medical services worldwide.</strong></p>
            <p><strong>Experience the future of healthcare—digitized, streamlined, and error-free.</strong></p>
        </div> """,unsafe_allow_html=True)


    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    doctor_name = st.sidebar.text_input("Doctor's Name")

    if st.sidebar.button("Login"):
        valid, doctor = check_login(username, password)
        if valid and doctor_name == doctor:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['doctor_name'] = doctor
            st.success(f"Logged in as {username}")
        else:
            st.error("Invalid credentials or doctor's name does not match")

# Main app functionality
if st.session_state['logged_in']:
    # Title of the app
    st.markdown("""
                         <h1 style='text-align: center; color: gray;'>
                             DOCTOR MEDICAL PRESCRIPTION RECOGNITION
                         </h1>
                         """, unsafe_allow_html=True)
    st.image('Streamlit Images/login.png',use_column_width=True)


    # File uploader allows user to add file
    uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

    if uploaded_file is not None:
        # Display the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Save the image to the server
        with open('input.png', 'wb') as f:
            f.write(uploaded_file.getvalue())

        try:
            # Call the processing function
            prediction = all_task()


            from fuzzywuzzy import fuzz, process

            # Load actual medicine names from the text file
            with open('medicine_names.txt', 'r') as file:
                actual_medicine_names = [line.strip() for line in file]


            # Function to get the best match and similarity score
            def get_best_match(predicted_name, actual_names):
                matches = process.extractOne(predicted_name, actual_names, scorer=fuzz.token_sort_ratio)
                return matches


            # Replace old names with the most similar names
            improved_predictions = []
            for predicted_name in prediction:
                best_match, similarity_score = get_best_match(predicted_name, actual_medicine_names)
                improved_predictions.append(best_match)

            st.markdown("""<h2 style='text-align: left; color: green;'>
                            Handwritten Text Digitize Predictions:
                        </h2>""", unsafe_allow_html=True)

            # Iterate through each prediction and display it
            for prediction in improved_predictions:
                st.markdown(f"<h3 style='text-align: left; color: blue; font-weight: bold;'>{prediction}</h3>",
                            unsafe_allow_html=True)

            # Load the medicine data from the CSV file
            medicine_data = pd.read_csv('medicine_data.csv')

            # Create an empty list to store the lowest price medicine details
            lowest_price_details = []

            # Iterate through each medicine in the improved predictions list
            for medicine_name in improved_predictions:
                filtered_data = medicine_data[medicine_data['medicine_names'] == medicine_name]
                if not filtered_data.empty:
                    lowest_price_row = filtered_data.loc[filtered_data['price'].idxmin()]
                    lowest_price_details.append({
                        'medicine_name': medicine_name,
                        'company_name': lowest_price_row['company_name'],
                        'price': lowest_price_row['price']
                    })

                    # Create a new Prescription object
                    new_prescription = Prescription(
                        username=st.session_state['username'],
                        doctor_name=st.session_state['doctor_name'],
                        medicine_name=medicine_name,
                        company_name=lowest_price_row['company_name'],
                        price=lowest_price_row['price']
                    )
                    # Add to the session and commit to the database
                    session.add(new_prescription)

            # Commit all the new prescriptions to the database
            session.commit()

            # Display the data table of lowest price medicine details
            lowest_price_details_df = pd.DataFrame(lowest_price_details)
            st.write(f"## User Name : {st.session_state['username']}")
            st.write(f"## Assigned Doctor: {st.session_state['doctor_name']}")
            st.write("# Best Companies and Best Price for the Following Medicines:")
            st.dataframe(lowest_price_details_df)

            if st.button("Send the Report"):
                create_report_and_send()
                st.success("Report sent to Registered User!")

        except Exception as e:
            st.error("An error occurred while saving to database or processing data: " + str(e))
            session.rollback()  # This resets the session if there's an error
