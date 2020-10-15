from pydub import AudioSegment

files_path = '/Users/scot/Desktop/'
file_name = 'brtop-2019-255'

startMin = 19
startSec = 8

endMin = 38
endSec = 49.5

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

# Opening file and extracting segment
print("Importing mp3 file")
song = AudioSegment.from_mp3(files_path+file_name+'.mp3')
print("mp3 file imported")
print("Trimming file")
extract = song[startTime:endTime]
print("File trimmed")

# Saving
print("Saving file")
extract.export('/Users/scot/Desktop/momentous/assets/snail_interview.mp3', format="mp3")
print("File saved")
