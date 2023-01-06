# Abstractive-Text-Summarizer
Abstractive text summarizer built from collecting important words which make up a sentence and then feeding it to a t5 model to generate a summary

## Introduction
![WhatsApp Image 2023-01-06 at 06 04 13](https://user-images.githubusercontent.com/98120916/210906631-6db79c0f-462c-4a3b-b4b6-638d8d4286a9.jpg)

This model was inspired by the SumBasic Extractive summarization model.  takes a probabilistic approach to determine which words are most likely to be included as a part of the summary.A Random forest classifier predicts probabilities of the words being present in summary given a certain features. words having high probability are then taken in and fed to a fine tuned t5 NLG model to generate coherent sentences.A major drawback to this project is the abscence of grammar checkers for the final summary.

Model was trained on the CNN/Daily mail dataset .Functions with clear documentation is provided as to make this model be deployed for some other summarization task.

## Description of files
