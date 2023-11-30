from pyAudioAnalysis import audioTrainTest as aT
aT.extract_features_and_train(["dataset/female","dataset/female"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
aT.file_classification("dataset/84-121123-0000.flac", "svmSMtemp","svm")