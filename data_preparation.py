import os
import shutil

#Path of the original LibriSpeech dataset folder which contains the speakers in each subfolder
original_dataset_directory = "../LibriSpeech/dev-clean"
#The folder in which male and female speakers' audios will be copied to
final_dataset_directory = "dataset"
#The file containing the speakers info
speakers_info_path = "../LibriSpeech/SPEAKERS.TXT"


# Function that, taken the speaker_id, goes to the speakers info file and returns "F" if it is a female user and "M" otherwise.
# If user doesnt exist returns None
def findUserGender(speaker_id):
    with open(speakers_info_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == ';':
                continue
            space_index = line.find(' ')
            if speaker_id == line[0:space_index]:
                F_index = line.find('F')
                M_index = line.find('M')
                if F_index == -1:
                    return "M"
                elif M_index == -1:
                    return "F"
                elif F_index < M_index:
                    return "F"
                else:
                    return "M"
        return None

counter = 0

copy = False

male_transcripts = open(final_dataset_directory + "/male/transcripts.txt",'w')
female_transcripts = open(final_dataset_directory + "/female/transcripts.txt",'w')

#Go through all speakers
for speaker_id in os.listdir(original_dataset_directory):

    #Get their gender
    user_gender = findUserGender(speaker_id)

    #Go through all their books
    for book_path in os.listdir(original_dataset_directory + "/" + speaker_id):
        #And all audio files
        for file_name in os.listdir(original_dataset_directory + "/" + speaker_id + "/" + book_path):
            #And copy them to the respective directory
            if file_name.endswith("flac"):
                if user_gender == "F" and copy:
                    shutil.copy2(original_dataset_directory + "/" + speaker_id + "/" + book_path + "/" + file_name,final_dataset_directory + "/female/" + file_name)
                elif user_gender == "M" and copy:
                    shutil.copy2(original_dataset_directory + "/" + speaker_id + "/" + book_path + "/" + file_name,final_dataset_directory + "/male/" + file_name)
                else:
                    print("Error in gender type")
        
        #Add transcripts
        transcripts = open(original_dataset_directory + "/" + speaker_id + "/" + book_path + "/" + speaker_id + "-" + book_path + ".trans.txt",'r').read()
        if user_gender == "M":
            male_transcripts.write(transcripts)
        else:
            female_transcripts.write(transcripts)

    counter += 1

print(f"SUCCESS. Imported {counter} speakers")
