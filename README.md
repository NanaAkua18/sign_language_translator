Sign Language Translator Project

Overview

The Sign Language Translator is a software application designed to bridge the communication gap between individuals who use sign language and those who do not. This tool specifically focuses on translating American Sign Language (ASL) hand gestures into corresponding text, making it easier for non-signers to communicate effectively with the Deaf and Hard of Hearing (HoH) community.

Problem Statement

Communication between Deaf/HoH individuals and the hearing community often faces challenges due to language barriers. This project addresses these challenges by providing a system that recognizes ASL gestures and translates them into text, thus promoting inclusivity and understanding.

Objectives

The main objectives of this project are:

To develop a software system capable of recognizing ASL hand gestures and converting them into text.
To create a robust Convolutional Neural Network (CNN) model that can accurately identify ASL gestures from a diverse dataset.
To implement practical training for participants to gain a deeper understanding of ASL and enhance cultural awareness of the Deaf community.

Key Features

Hand Gesture Recognition: Uses a CNN-based model to identify and translate ASL gestures.
Real-time Translation: Provides immediate conversion of gestures to text for ease of communication.
Comprehensive ASL Dataset: Includes a wide variety of hand movements to ensure the system's accuracy and adaptability.
User-friendly Interface: Simple and accessible interface for both personal and professional use.

Development Tools and Environment

Programming Languages: Python, TensorFlow, Keras
Libraries/Frameworks: OpenCV, NumPy, Matplotlib
Environment: Jupyter Notebook or any Python IDE
Data Preprocessing: Data cleaning, normalization, and augmentation techniques for dataset preparation.
System Architecture

The system leverages a deep learning architecture with CNNs, which consist of layers optimized for feature extraction, pooling, and classification. The CNN model is trained using supervised learning to recognize ASL gestures accurately.

Installation

Install the necessary packages:
pip install -r requirements.txt
Run the application:
python app.py

Usage

Launch the software and allow access to your device's camera.
Perform ASL gestures in front of the camera.
The system will process the gestures and display the corresponding text on the screen.

Future Work

Expansion to other sign languages: Adding support for ISL (Indian Sign Language), BSL (British Sign Language), etc.
Mobile Application: Development of a mobile version for easier use in various settings.
Enhanced Features: Incorporating voice output and gesture feedback for better user interaction.
