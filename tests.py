from pyAudioAnalysis import audioTrainTest as aT
import os

directory = "dataset/male_test/"

print("Starting")

c1 = 0
c2 = 0
count = 0
file_names = os.listdir(directory);
for file_name in file_names:
    result = aT.file_classification(directory + file_name, "svmSMtemp","svm")
    if result[1][0] > result[1][1]:
        c1 += 1
    else:
        c2 += 1
    count += 1
    print(f"{count}/{len(file_names)}:   {c1} vs {c2}",end="\r")

print(f"\n{c1} vs {c2}")