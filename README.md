# Automatic Speech Recognition Model for Gender Distinction

In this project, an Automatic Speech Recognition (ASR) model is created to be able to distinguish between genders (male and female in this case).

To train the model, the LibriSpeech dataset is used and PyAudioAnalysis. 

## File description

- data_preparation.py takes a LibriSpeech dataset and separates male speakers from female speakers

- model.py trains a model based on the data created by the previous script. Should run the command `pip install -r requirements.txt`

