from pyAudioAnalysis import audioTrainTest as aT

result = aT.file_classification("test.wav", "svmSMtemp","svm")

print(result)