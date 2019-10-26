# Submission Format:
We need to create a reusable library that can convert a paragraph of spoken english to written english. For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively. 

I have uploaded three files in the github and data has been taken from kaggle for third file
In one file I used google API to convert speech to text(speech_recognition_Task)
The other file is to make module in python(mymodule)
The last file is for converting speech to text with feature extraction and building the model.(Speech_Recognition_Assingment)

# What is sampling the signal and why is it required?
An audio signal is a continuous representation of amplitude as it varies with time. Here, time can even be in picoseconds. That is why an audio signal is an analog signal.
Analog signals are memory hogging since they have an infinite number of samples and processing them is highly computationally demanding. Therefore, we need a technique to convert analog signals to digital signals so that we can work with them easily.
Sampling the signal is a process of converting an analog signal to a digital signal by selecting a certain number of samples per second from the analog signal. 
# The Various features exracted are as follows :-
1.Time-domain:- The audio signal is represented by the amplitude as a function of time. It is a plot between amplitude and time. The features are the amplitudes which are recorded at different time intervals

2.Frequency domain:-In the frequency domain, the audio signal is represented by amplitude as a function of frequency. Simply put – it is a plot between frequency and amplitude. The features are the amplitudes recorded at different frequencies.

3.Silence Removal:- For feature extraction we can use VAD(Voice Activity Detection).Sometimes there is lot of silence in them .A decent VAD can reduce training size a lot, accelerating training speed significantly.

4.Resampling (Dimensionality reduction):-Another way to reduce the dimensionality of our data is to resample recordings.

5.Log spectrogram (or MFCC, or PLP)

6.Features normalization with mean and std

7.Stacking of a given number of frames to get temporal information
