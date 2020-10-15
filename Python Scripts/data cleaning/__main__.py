#This is a program that runs as a GUI in a separate window. For use on other devices, you'll need to install
#BOX Drive and change the file path, and change the location where the set-up .txt file will be saved. You can also
#customize the strings that signal where the headline, guest info, and intro copy start and end. This way, the program
#can be used for different shows, and adjusted as set-up formats change.
#
# Author: Scot Nielson, 2020
#
#TODO: construct the GUI as a class and call it in main()

import os
import zipfile
from datetime import datetime
from titlecase import titlecase
from tkinter import *
from tkinter.font import Font

BOX_FILE_PATH = '//Users/scot/Box/BYU Radio/Top of Mind/2020 Setup Sheets/'
SETUP_PATH = '//Users/scot/Desktop/Setups/WebsiteAuto/'
MAX_NUM_ROWS = 10
EPISODE_NUM = 6

def GetFileName(slug):  # this takes a slug and returns the filename, capitalization doesn't matter
    if slug == "":
        return slug
    setups = os.listdir(BOX_FILE_PATH)
    setupsLower = [x.lower() for x in setups]  # makes all titles in listdir lowercase for cap-free searching
    fileName = str([s for s in setupsLower if slug.lower() in s])
    if len(fileName) == 2:
        setupSheet = "NO FILE FOUND WITH \"" + slug + "\" IN NAME"
    elif fileName.count(".docx") > 1:
        setupSheet = "MORE THAN ONE POSSIBLE FILE: " + fileName
    else:
        cleanName = setupsLower.index(fileName[2:len(fileName) - 2])
        setupSheet = setups[cleanName]  # returns properly capitalized filename based on index
    return setupSheet


def CleanWord(fileSlug):
    fileName = GetFileName(fileSlug)
    if fileName == "":
        return fileName
    doc = zipfile.ZipFile(BOX_FILE_PATH + fileName)
    content = doc.read('word/document.xml').decode('utf-8')  # .decode() turns type bytes into string for easy manipulation
    cleaned = re.sub('<(.|\n)*?>', '', content)
    return cleaned


def GetHeadline(cleaned):
    # get headline
    headline = cleaned[cleaned.find("HEADLINE: ") + len("HEADLINE: "):cleaned.find("SEGMENT")]
    return headline


def GetGuest(cleaned):
    # get name and title of guest--should be reviewed for proper formatting
    nameAndTitle = "Name and Title of Guest(s): "
    if cleaned.find("Pronunciation:") != -1:  # if "Pronunciation has been deleted, the string will stop at "Pre-Record:"
        guest = cleaned[cleaned.find(nameAndTitle) + len(nameAndTitle):cleaned.find("Pronunciation:")]
    elif cleaned.find("Pre-Record") != -1:
        guest = cleaned[cleaned.find(nameAndTitle) + len(nameAndTitle):cleaned.find("Pre-Record:")]
    else:
        guest = cleaned[cleaned.find(nameAndTitle) + len(nameAndTitle):cleaned.find("FOR AIR:")]
    return guest


def GetIntroCopy(cleaned):
    # gets intro, goes until it finds specified ending phrases and cuts the string at those points
    indexIntroCopyLeft = ""

    introCopyLeft = ["OUT CUE: I’m Julie Rose.", "INTRO COPY (LIVE-READ, WRITTEN-TO-SOUND). ",
                         "INTRO COPY (LIVE-READ, WRITTEN-TO-SOUND).", "INTRO COPY"]
    for introCopy in introCopyLeft:
        if cleaned.find(introCopy) != -1:
#             introCopySet = introCopy
            indexIntroCopyLeft = cleaned.find(introCopy) + len(introCopy)
            break
    intro = cleaned[indexIntroCopyLeft:len(cleaned)]

    #add phrases that mark the end of the intro to "endlines"
    endlines = ["on the line", "joins me now", "in the studio", "QUESTIONS:", "Welcome. ", ", welcome.", ". Welcome ",
                "OUTRO COPY"]
    for endline in endlines:
        if intro.find(endline) != -1:
            intro = intro[0:intro.find(endline)]

    return intro


def ScrapeWord(fileSlug):  # this goes into a word document and returns titlecase headline, guest info, and intro copy
    if fileSlug == "":
        return fileSlug

    cleaned = CleanWord(fileSlug)

    headline = GetHeadline(cleaned)
    guest = GetGuest(cleaned)
    intro = GetIntroCopy(cleaned)

    # if it's for Prime Cuts, this gives the original air date
    if cleaned.find("PRIME CUTS") != -1:  # GetFileName(fileSlug).find("PRIME CUTS") != -1: <- I might need this
        forAir = cleaned[cleaned.find("FOR AIR") + len("FOR AIR: "):len(cleaned)]
        origAired = "(Originally aired" + forAir[0:forAir.find("PRIME")] + ")"
    else:
        origAired = ""

    # concatenate info, titlecase headline and guest
    info = titlecase(headline) + "\n" + "Guest: " + titlecase(guest) + "\n" + intro + " " + origAired + "\n\n"
    return info


def GetEpisodeInfo(fileName):  # returns titlecase headline, guest info, and intro copy from word
    cleaned = CleanWord(fileName)

    # get name and title of guest--should be reviewed for proper formatting
    nameAndTitle = "Name and Title of Guest(s): "
    if cleaned.find("Pronunciation:") != -1:  # if "Pronunciation has been deleted, the string stops at "Pre-Record:"
        guest = cleaned[cleaned.find(nameAndTitle) + len(nameAndTitle):cleaned.find("Pronunciation:")]
    else:
        guest = cleaned[cleaned.find(nameAndTitle) + len(nameAndTitle):cleaned.find("Pre-Record:")]

    info = guest[0:guest.find(",")] + " of " + guest[guest.find(","):len(guest)] + " on " + fileName.lower() + "."
    return info


def ListSlugs():
    slugs = []
    for entry in entries:
        slugs.append(entry.get())
    return slugs


def PrintSlugs():
    slugs = enumerate(ListSlugs())

    for index,slug in slugs:
        if len(slug) == 0:
            slugInfo[index].config(text = "NO SLUG ENTERED")
        else:
            slugInfo[index].config(text = GetFileName(slug))
    create_txt_done.config(text="")


def InsertTxt(webText):  # this opens/creates a new .txt file, writes webText to it, closes .txt file
    now = datetime.now()
    today = now.strftime("%m-%d-%Y")
    file = SETUP_PATH + today + ".txt"
    f = open(file, "w+")
    f.write(webText)
    f.close()


def EpInfo():
    slugs = ListSlugs()
    episodeInfo = ''
    for i in slugs:
        episodeInfo += GetEpisodeInfo(GetFileName(i))
    e = Entry(root)
    e.grid(row=get_ep_info.grid_info()['row']+1, column=2)
    e.insert(0, episodeInfo)


def CreateTxt():
    slugs = ListSlugs()
    text = ""
    for x in slugs:
        text += ScrapeWord(x)
    InsertTxt(text)
    print(text)
    create_txt_done.config(text="Done!")
    create_txt_done.grid(row=create_txt.grid_info()['row']+1, column=1)


def CreateNewEpisode():
    numRows = len(labels)
    if numRows >= MAX_NUM_ROWS:
        return 0

    labels.append(Label(root, text="Enter Slug " + str(numRows + 1) + ":"))
    labels[numRows].grid(row=numRows+1, column=0)

    entries.append(Entry(root))
    entries[numRows].grid(row=numRows+1, column=1)

    slugInfo.append(Label(root, text=""))
    slugInfo[numRows].grid(row=numRows+1, column=2)


def RemoveEpisode():
    numRows = len(labels)-1
    labels[numRows].grid_forget()
    entries[numRows].grid_forget()
    slugInfo[numRows].grid_forget()

    labels.pop()
    entries.pop()
    slugInfo.pop()

# generate GUI
# print("How many episodes air today?")
# episodeNum = int(input("How many episodes air today?"))

root = Tk()
# general_font = ('Helvetica', 14)
# root.option_add('*Font', general_font)
# root['bg']='#2b4651'

root.title("BYU Top of Mind Website Content Generator")
Label(root, text="Top of Mind with Julie Rose", compound=CENTER).grid(row=0, column=0)
Button(root, text="Add slot", compound=CENTER, command=CreateNewEpisode).grid(row=0, column=1)
Button(root, text="Remove slot", compound=LEFT, command=RemoveEpisode).grid(row=0, column=2)

labels = [] #build entry labels
entries = [] #build entry fields
slugInfo = [] #this holds the labels for the filename info so they can be cleared

for i in range(EPISODE_NUM):
    label_text = "Enter Slug " + str(i + 1) + ":"
    labels.append(Label(root, text=label_text))
    labels[i].grid(row=i+1, column=0)

    entries.append(Entry(root))
    entries[i].grid(row=i+1, column=1)

    slugInfo.append(Label(root, text=""))
    slugInfo[i].grid(row=i+1, column=2)

get_filenames_button = Button(root, text="Check filenames", command=PrintSlugs)
create_txt = Button(root, text="Create .txt file", command=CreateTxt)
create_txt_done = Label(root, text="Done!")
get_ep_info = Button(root, text="Get Episode Info", command=EpInfo)
#TODO add a clear button to destroy the filename labels...or just clear them anytime you call Check filename

get_filenames_button.grid(row=MAX_NUM_ROWS+1, column=0)
create_txt.grid(row=MAX_NUM_ROWS+1, column=1)
get_ep_info.grid(row=MAX_NUM_ROWS+1, column=2)

root.mainloop()

# if __name__ == "__main__":
#     main()
