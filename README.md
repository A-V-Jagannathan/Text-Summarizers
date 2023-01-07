# Abstractive-Text-Summarizer
Abstractive text summarizer built from collecting important words which make up a sentence and then feeding it to a t5 model to generate a summary

## Introduction
![Final_Summarizer](https://user-images.githubusercontent.com/98120916/211164271-a8671f43-771d-483b-84ae-60955a7d750c.jpg)

This model was inspired by the SumBasic Extractive summarization model.  takes a probabilistic approach to determine which words are most likely to be included as a part of the summary.A Random forest classifier predicts probability of a word being present in summary, given a certain set of features. words having high probability are then taken in and fed to a fine tuned t5 NLG model to generate coherent sentences.Then each of the sentence is fed to a Grammar checker model to generate grammatically correct sentences

Model was trained on the CNN/Daily mail dataset .Functions with clear documentation is provided as to make this model be deployed for some other summarization task.

## Downloading the required files and packages

Due to file upload size limit in github, for the primary version 0.0 im using Google drive to store my pre trained models. Make sure to have the finalized_model.sav, loading.gif and model folder under the same directory as Abstractive_Summarization_model.py 


The notebook file of Abstractive_Summarization_model, contains the documentation for every function so it is easier to modify it and use. A demo is provided at the end of the notebook file about how to run it.

pip install keytotext

pip install gramformer

## Resolving package issues.-IMPORTANT

install package keytotext  and locate trainer.py under keytotext package, Ctrl+f to find progress_bar_refresh_rate and remove that line


install package gramformer and under errant folder, replace the __init__.py file with the file uploaded under Gramformer Fixes . under gramformer, replace the gramformer.py file with the gramformer.py file uploaded under Gramformer Fixes



