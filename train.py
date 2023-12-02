from pyAudioAnalysis import audioTrainTest as aT

print("Starting training")
aT.extract_features_and_train(["dataset/female","dataset/male"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
print("Training complete. Testing")
