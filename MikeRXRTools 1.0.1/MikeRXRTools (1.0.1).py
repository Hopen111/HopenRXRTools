VERSION = "1.0.1"
DISPLAYVERSION = "1.0.1"

def prRed(skk): print("\033[31m {}\033[00m" .format(skk))

def prYellow(skk): print("\033[33m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

print("""--MikeRXRTools """+VERSION+"""--""")
print("--Created by Hopen111--")

print("""
Please Fill Out The Info Below.""")

print("""
Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US-64.--

--Don't Forget To Add A "." At The End!
""")
crossing_name = input("Crossing Street Name? ") #Crossing Street

print("""
Crossing City Examples: 
--Dedham, IA--
--Nickerson, NE--
--Chicago, IL--
""")

crossing_city = input("Crossing City? ") #Crossing City

print("""
Creation Date Examples: 
--January 2023--
--May 2024--
--April 2022--
""")

crossingdate = input("Page Creation Date? ") #Month & Year
digits = len(crossingdate)

month = crossingdate[0:digits-5] #Sort Month
width = 60
if month == "January" or month == "january" or month == "Jan" or month == "jan":
    month = 1
    width = 99
elif month == "February" or month == "february" or month == "Feb" or month == "feb":
    month = 2
    width = 109
elif month == "March" or month == "march" or month == "Mar" or month == "mar":
    month = 3
    width = 72
elif month == "April" or month == "april" or month == "Apr" or month == "apr":
    month = 4
    width = 60
elif month == "May" or month == "may":
    month = 5
    width = 49
elif month == "June" or month == "june" or month == "Jun" or month == "jun":
    month = 6
    width = 57
elif month == "July" or month == "july" or month == "Jul" or month == "jul":
    month = 7
    width = 52
elif month == "August" or month == "august" or month == "Aug" or month == "aug":
    month = 8
    width = 88
elif month == "September" or month == "september" or month == "Sept" or month == "sept":
    month = 9
    width = 133
elif month == "October" or month == "october" or month == "Oct" or month == "oct":
    month = 10
    width = 100
elif month == "November" or month == "november" or month == "Nov" or month == "nov":
    month = 11
    width = 125
elif month == "December" or month == "december" or month == "Dec" or month == "dec":
    month = 12
    width = 123

#Month Sorted

year = crossingdate[digits-4:digits]

print("""
--If You Don't Know How To Get Your Crossing Accidents, First, Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/
--Next, Find Your Crossing, Click On It, And Then Scroll Down To "ACC_LINK" And Click "View" 
--This Will Download A PDF With The Amount Of Accidents Included
--If You Still Cannot Find The Number Of Accidents Or You Live In Canada, You Can Type "Unknown", "idk", Or "N/A"
""")

crossing_acc = input("Total Accidents? ") #Accidents
if crossing_acc == "N/A" or crossing_acc == "n/a" or crossing_acc == "Unknown" or crossing_acc == "unknown" or crossing_acc == "idk":
    crossing_acc = "Unknown"

crossingaccidentshtml = """<tr>
<td
style="vertical-align: middle; text-align: center; height: 40px;"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
src="http://www.rxrsignals.com/Graphics/Accidents/"""+crossing_acc+""".png"></font></font></strong></td>
</tr>"""

if crossing_acc =="":
    crossingaccidentshtml = ""

# Sort DOT

print("""
DOT Number Examples: 
--05032932G--
--30324648D--
--3247320F, 2139312B--

--If You Don't Know How To Get Your Crossing DOT, First Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/ 
--Next, Find Your Crossing, Click On It, And Then Under "CROSSING", It Will Show The DOT Number
--You Can Also Use Your Photos Of The DOT Number And Just Copy It Here
--If You Still Cannot Find The DOT Number Or You Live In Canada, You Can Type "UNKNOWN" In Full Caps
""")

dot = input("DOT Number(s)? ")
Dotdigits = len(dot)
dotlist = []
dotcommacheck = "DOT"

for i in range(Dotdigits):
    DotDigitSorted = dot[0+i:1+i]
    if DotDigitSorted == " ": #Adds Space? It also replaces letters with blank
        DotDigitSorted ="Blank"
    if DotDigitSorted == ",": #Adds Comma
        DotDigitSorted ="Comma"
        dotcommacheck = "DOTS"
    dotlist.append("https://www.rxrsignals.com/Graphics/DOT/"+DotDigitSorted+".png>")

dotlistlength = len(dotlist)

dothtml = ""
dotcommasizefix = "13"

for i in range(dotlistlength): #Should Create HTML
    dotsort = str(dotlist[0+i]) #Begin making HTML line 57
    dotcommasizefix = "13"
    if dotsort == "https://www.rxrsignals.com/Graphics/DOT/Comma.png>":
    	dotcommasizefix = "5"
    dothtml = dothtml+"""<img style="width: """+dotcommasizefix+"""px; height: 20px;" alt="" src="""+dotsort+""""""

dothtmlblank = """<tr>
<td style="vertical-align: middle; text-align: center;"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
src="http://www.rxrsignals.com/Graphics/DOT/"""+dotcommacheck+""".png"><img style="width: 10px; height: 20px;" alt="" src="https://www.rxrsignals.com/Graphics/DOT/Blank.png"> """+dothtml+"""</font></font></strong></td>
</tr>"""
if dot == "":
    dothtmlblank = ""

#DOT Sorted

#Sort Milepost

print("""
Milepost Examples: 
--20.25--
--89.77--
--255.78--

--If You Don't Know How To Get Your Crossing Milepost, First Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/ 
--Next, Find Your Crossing, Click On It, And Then Scroll Down
--And Then Under "MILEPOST", It Will Show The Milepost Number
""")

mp = input("Milepost? ")
mpdigits = len(mp)
mplist = []

for i in range(mpdigits):
    mpdigitsorted = mp[0+i:1+i]
    if mpdigitsorted == " ": #Adds Space? It also replaces letters with blank
        mpdigitsorted ="Blank"
    if mpdigitsorted == ".": #Adds Comma
        mpdigitsorted ="Decimal"
    mplist.append("http://www.rxrsignals.com/Graphics/Milepost_Numbers/"+mpdigitsorted+".PNG>")

mplistlength = len(mplist)

mphtml = ""
mpdecimalsizefix = "16"

for i in range(mplistlength): #Should Create HTML
    mpsort = str(mplist[0+i]) #Begin making HTML line 57
    mpdecimalsizefix = "16"
    if mpsort == "http://www.rxrsignals.com/Graphics/Milepost_Numbers/Decimal.PNG>":
    	mpdecimalsizefix = "8"
    mphtml = mphtml+"""<img style="width: """+mpdecimalsizefix+"""px; height: 20px;" alt="" src="""+mpsort+""""""

mpblankhtml = """<img style="width: 46px; height: 20px;" alt="" src="http://www.rxrsignals.com/Graphics/Milepost_Numbers/MP.PNG"><img style="width: 16px; height: 20px;" alt="" src="http://www.rxrsignals.com/Graphics/Milepost_Numbers/Blank.PNG">"""
if mp == "":
    mpblankhtml = ""

#Milepost Sorted

#Sort Railroads

print("""
Railroad Logo Examples: 
--BNSF.png--
--UP.PNG--
--CPKC.png--

--To Get More Railroad Logos, First Visit This Site:
http://www.rxrsignals.com/Graphics/Rail_Logos/ 
--Next, Use CTRL+F And Search For The Railroad Logo You Need (Use Reporting Markers Such As UP, or BNSF)
--And Then Copy And Paste Your Railroad Logo With The File Name Extension Too (Such As NS.gif or Metra.png
--For Multiple Railroads, You Can Type "BNSF.png CN.gif CSX.png"
--Add A Space When Differentiating Between Different Railroads, No Comma Needed! 
""")

rr = input("Railroad(s)? ")
rrdigits = len(rr)
rrlist = []
for index, rrdigitsorted in enumerate(rr.split()):
    rrlist.append("http://www.rxrsignals.com/Graphics/Rail_Logos/"+rrdigitsorted+">")
   
rrlistlength = len(rrlist)

rrhtml = ""
rrdecimalsizefix = "16"

for i in range(rrlistlength): #Should Create HTML
    mpsort = str(rrlist[0+i]) #Begin making HTML line 57
    #rrdecimalsizefix = "16"
    #if mpsort == "http://www.rxrsignals.com/Graphics/Milepost_Numbers/Decimal.PNG>":
    # rrdecimalsizefix = "8"
    rrhtml = rrhtml+"""<img alt="" src="""+mpsort+""""""

#Railroad Sorted

#Quiet Zone?

QZ = input("Quiet Zone? (Y/N) ")
quietzone = ""
if QZ == "Yes" or QZ == "Y" or QZ == "yes" or QZ == "y":
    quietzone = """<img src="http://www.rxrsignals.com/Graphics/QuietZone.png" width="151" height="32" alt="">"""
if QZ == "No" or QZ == "N" or QZ == "no" or QZ == "n" or QZ == "":
    quietzone = ""

#Quiet Zone Sorted

#Defunct Xing

DF = input("Defunct X-ing? (Y/N) ")
defunctxing = ""
if DF == "Yes" or DF == "Y" or DF == "yes" or DF == "y":
    defunctxing = """<p><img style="width: 450px; height: 60px;" alt="" src="https://www.rxrsignals.com/Graphics/Defunct.gif"></p>"""
if DF == "No" or DF == "N" or DF == "no" or DF == "n" or DF == "":
    defunctxing = ""

#Defunct Xing Sorted

print("""
--If You Don't Know How To Get Your Crossings Daily Train Count, First Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/ 
--Next, Find Your Crossing, Click On It, And Then Scroll Down To "INV_LINK" And Click "View" 
--This Will Download A PDF With The Amount Of Daily Trains Included
--If You Still Cannot Find The Number Of Daily Trains Or You Live In Canada, You Can Type "Unknown", "idk", Or "N/A"
""")

crossing_daily = input("Daily Trains? ") #Daily Trains
if crossing_daily == "N/A" or crossing_daily == "n/a" or crossing_daily == "Unknown" or crossing_daily == "unknown" or crossing_daily == "idk":
    crossing_daily = "Unknown"

print("""
As Of Examples: 
--2020--
--2019--
--2022--""")
crossing_asof = input("As Of? ") #As Of

fullname = crossing_name + " ("+ crossing_city +")"

#Check If User Is Ready

prYellow("""
!WARNING! 
Any Photos Proccessed By MikeRXRTools Cannot Be Undone! 
Make Sure To Have A Backup Folder With All The Photos In The Event You Make A Typo Or Want 
To Make The Page Again (Or If The Program Straight Up Crashes).

Also, If The Program Detects A Crossing/Folder With The Same Street Name Already 
In The Output Folder, MikeRXRTools WILL Crash.
""")

input("Press ENTER Twice To Begin Processing Photos")
input("Press ENTER Twice To Begin Processing Photos")

print("""
Processing Photos...""")

fullnamehtml = "index"

# importing os module
import os

#Make Folder

directory = fullname 

parent_dir = "Output/"

path = os.path.join(parent_dir, directory)

os.mkdir(path)

#Made Folder

"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

Filenamefix = """ " """
Filenamefix2 = Filenamefix[1:2]
name = 0
Filenamelist = []
FacingWest = False
FacingEast = False
FacingNorth = False
FacingSouth = False
North = False
South = False
East = False
West = False
FacingImageCount = 0
NorthImagehtml = ""
SouthImagehtml = ""
EastImagehtml = ""
WestImagehtml = ""

#Sort Facing North Photo

import shutil
import PIL
import glob

from PIL import Image

source = 'Overviews/Overview_Facing_North/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    FacingNorth = True
    FacingImageCount = FacingImageCount + 1
    NorthImagehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)


#Sorted Facing North Photo

#Sort Facing South Photo

source = 'Overviews/Overview_Facing_South/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    FacingSouth = True
    FacingImageCount = FacingImageCount + 1
    SouthImagehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing South Photo

#Sort Facing East Photo

source = 'Overviews/Overview_Facing_East/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    FacingEast = True
    FacingImageCount = FacingImageCount + 1
    EastImagehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing East Photo

#Sort Facing West Photo

source = 'Overviews/Overview_Facing_West/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    FacingWest = True
    FacingImageCount = FacingImageCount + 1
    WestImagehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing West Photo

#Sort Overview Photos

facingimagehtml = ""
NorthImageHeaderhtml = ""
SouthImageHeaderhtml = ""
EastImageHeaderhtml = ""
WestImageHeaderhtml = ""
FacingWidth = "100"

if FacingImageCount == 4:
    FacingWidth = "25"
if FacingImageCount == 3:
    FacingWidth = "33"
if FacingImageCount == 2:
    FacingWidth = "50"
if FacingImageCount == 1:
    FacingWidth = "100"

if FacingNorth == True:
    NorthImageHeaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">Overview facing north.</td>"""
if FacingSouth == True:
    SouthImageHeaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">Overview facing south.</td>"""
if FacingEast == True:
    EastImageHeaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">Overview facing east.</td>"""
if FacingWest == True:
    WestImageHeaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">Overview facing west.</td>"""

facingimagehtml = facingimagehtml+"""
"""+NorthImagehtml+"""
"""+SouthImagehtml+"""
"""+EastImagehtml+"""
"""+WestImagehtml+"""
</tr>
<tr>
"""+NorthImageHeaderhtml+"""
"""+SouthImageHeaderhtml+"""
"""+EastImageHeaderhtml+"""
"""+WestImageHeaderhtml+"""
</tr>
"""

if FacingNorth == True or FacingSouth == True or FacingEast == True or FacingWest == True:
    facingimagehtml = """<table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
<tbody>"""+facingimagehtml+"""</tbody>
</table>"""

"""Sorted Overview Photos ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

#Sort Northern Signal Photos

source = 'Northern_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
northernsignalcount = 0
for f in allfiles:
    name = name + 1
    northernsignalcount = northernsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    North = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

theinput = northernsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

evennumbertest1 = theinput/2
evennumbertest2 = theinput//2
make4columns = 0
make3columns = 0
make2columns = 0
make1column = 0
evensteven =""
#Begin Sort Photos
if evennumbertest2 == evennumbertest1:
    evensteven = "Even"
elif evennumbertest2 != evennumbertest1:
    evensteven = "Odd"

if evensteven == "Even":
    columns = theinput/4
    columnscheck = theinput//4
    if columnscheck == columns:
        oddtodd = "Even"
        make4columns = theinput/4
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput-6 >= 4:
            make3columns = 2
            make4columns = ((theinput-6)/4)
        elif theinput == 2:
            make2columns = 1
        elif theinput == 6:
            make3columns = 2
            
if evensteven == "Odd":
    columns = theinput/3
    columnscheck = theinput//3
    if columnscheck == columns:
        oddtodd = "Even"
        if theinput == 3:
            make3columns = 1
        elif theinput == 9:
            make3columns = 3
        elif theinput != 3:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput == 1:
            make1column = 1
        elif theinput == 5:
            make3columns = 1
            make2columns = 1
        elif theinput-3 >= 3 and (theinput-3)/4 == (theinput-3)//4:
            columns = (theinput-3)/4
            columnscheck = (theinput-3)//4
            make3columns = 1
            make4columns = ((theinput-3)/4)
        elif (theinput-3)/4 != (theinput-3)//4:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
make4columns = int(make4columns)
#Photos Sorted

northernsignalhtml = ""
northernsignalbegincount = name-northernsignalcount
northernsignalcounter = 0

for i in range(make1column):
    northernsignalcounter = northernsignalcounter + 1
    northernsignalhtml = northernsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
    </tr>
  </tbody>
</table>
"""

for i in range(make2columns):
    northernsignalcounter = northernsignalcounter + 1
    northernsignalhtml = northernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    northernsignalcounter = northernsignalcounter + 1

for i in range(make3columns):
    northernsignalcounter = northernsignalcounter + 1
    northernsignalhtml = northernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    northernsignalcounter = northernsignalcounter + 2

for i in range(make4columns):
    northernsignalcounter = northernsignalcounter + 1
    northernsignalhtml = northernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" "><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+""" "><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+""" "><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+3]+""" "><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+3]+""" "
alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    northernsignalcounter = northernsignalcounter + 3
if northernsignalhtml !="":
    northernsignalhtml = northernsignalhtml+ """
    <table width="100%" border="1">
      <tbody>
        <tr>
          <td align="center" valign="middle">The northern signal.</td>
        </tr>
      </tbody>
    </table>
    """

#Northern Signal Sorted

#Sort Southern Signal Photos

source = 'Southern_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
southernsignalcount = 0
for f in allfiles:
    name = name + 1
    southernsignalcount = southernsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    South = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

theinput = southernsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

evennumbertest1 = theinput/2
evennumbertest2 = theinput//2
make4columns = 0
make3columns = 0
make2columns = 0
make1column = 0
evensteven =""
#Begin Sort Photos
if evennumbertest2 == evennumbertest1:
    evensteven = "Even"
elif evennumbertest2 != evennumbertest1:
    evensteven = "Odd"

if evensteven == "Even":
    columns = theinput/4
    columnscheck = theinput//4
    if columnscheck == columns:
        oddtodd = "Even"
        make4columns = theinput/4
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput-6 >= 4:
            make3columns = 2
            make4columns = ((theinput-6)/4)
        elif theinput == 2:
            make2columns = 1
        elif theinput == 6:
            make3columns = 2
            
if evensteven == "Odd":
    columns = theinput/3
    columnscheck = theinput//3
    if columnscheck == columns:
        oddtodd = "Even"
        if theinput == 3:
            make3columns = 1
        elif theinput == 9:
            make3columns = 3
        elif theinput != 3:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput == 1:
            make1column = 1
        elif theinput == 5:
            make3columns = 1
            make2columns = 1
        elif theinput-3 >= 3 and (theinput-3)/4 == (theinput-3)//4:
            columns = (theinput-3)/4
            columnscheck = (theinput-3)//4
            make3columns = 1
            make4columns = ((theinput-3)/4)
        elif (theinput-3)/4 != (theinput-3)//4:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
make4columns = int(make4columns)
#Photos Sorted

southernsignalhtml = ""
southernsignalbegincount = name-southernsignalcount
southernsignalcounter = 0

for i in range(make1column):
    southernsignalcounter = southernsignalcounter + 1
    southernsignalhtml = southernsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
    </tr>
  </tbody>
</table>
"""

for i in range(make2columns):
    southernsignalcounter = southernsignalcounter + 1
    southernsignalhtml = southernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+""" "><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    southernsignalcounter = southernsignalcounter + 1

for i in range(make3columns):
    southernsignalcounter = southernsignalcounter + 1
    southernsignalhtml = southernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    southernsignalcounter = southernsignalcounter + 2

for i in range(make4columns):
    southernsignalcounter = southernsignalcounter + 1
    southernsignalhtml = southernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+3]+""" "
alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    southernsignalcounter = southernsignalcounter + 3
if southernsignalhtml !="":
    southernsignalhtml = southernsignalhtml+ """
    <table width="100%" border="1">
      <tbody>
        <tr>
          <td align="center" valign="middle">The southern signal.</td>
        </tr>
      </tbody>
    </table>
    """
#Southern Signal Sorted

#Sort Eastern Signal Photos

source = 'Eastern_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
easternsignalcount = 0
for f in allfiles:
    name = name + 1
    easternsignalcount = easternsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    East = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

theinput = easternsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

evennumbertest1 = theinput/2
evennumbertest2 = theinput//2
make4columns = 0
make3columns = 0
make2columns = 0
make1column = 0
evensteven =""
#Begin Sort Photos
if evennumbertest2 == evennumbertest1:
    evensteven = "Even"
elif evennumbertest2 != evennumbertest1:
    evensteven = "Odd"

if evensteven == "Even":
    columns = theinput/4
    columnscheck = theinput//4
    if columnscheck == columns:
        oddtodd = "Even"
        make4columns = theinput/4
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput-6 >= 4:
            make3columns = 2
            make4columns = ((theinput-6)/4)
        elif theinput == 2:
            make2columns = 1
        elif theinput == 6:
            make3columns = 2
            
if evensteven == "Odd":
    columns = theinput/3
    columnscheck = theinput//3
    if columnscheck == columns:
        oddtodd = "Even"
        if theinput == 3:
            make3columns = 1
        elif theinput == 9:
            make3columns = 3
        elif theinput != 3:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput == 1:
            make1column = 1
        elif theinput == 5:
            make3columns = 1
            make2columns = 1
        elif theinput-3 >= 3 and (theinput-3)/4 == (theinput-3)//4:
            columns = (theinput-3)/4
            columnscheck = (theinput-3)//4
            make3columns = 1
            make4columns = ((theinput-3)/4)
        elif (theinput-3)/4 != (theinput-3)//4:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
make4columns = int(make4columns)
#Photos Sorted

easternsignalhtml = ""
easternsignalbegincount = name-easternsignalcount
easternsignalcounter = 0

for i in range(make1column):
    easternsignalcounter = easternsignalcounter + 1
    easternsignalhtml = easternsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
    </tr>
  </tbody>
</table>
"""

for i in range(make2columns):
    easternsignalcounter = easternsignalcounter + 1
    easternsignalhtml = easternsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    easternsignalcounter = easternsignalcounter + 1

for i in range(make3columns):
    easternsignalcounter = easternsignalcounter + 1
    easternsignalhtml = easternsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    easternsignalcounter = easternsignalcounter + 2

for i in range(make4columns):
    easternsignalcounter = easternsignalcounter + 1
    easternsignalhtml = easternsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+3]+""" "
alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    easternsignalcounter = easternsignalcounter + 3
if easternsignalhtml !="":
    easternsignalhtml = easternsignalhtml+ """
    <table width="100%" border="1">
      <tbody>
        <tr>
          <td align="center" valign="middle">The eastern signal.</td>
        </tr>
      </tbody>
    </table>
    """
#Sorted Eastern Signal

#Sort Western Signal Photos

source = 'Western_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
westernsignalcount = 0
for f in allfiles:
    name = name + 1
    westernsignalcount = westernsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    West = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

theinput = westernsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

evennumbertest1 = theinput/2
evennumbertest2 = theinput//2
make4columns = 0
make3columns = 0
make2columns = 0
make1column = 0
evensteven =""
#Begin Sort Photos
if evennumbertest2 == evennumbertest1:
    evensteven = "Even"
elif evennumbertest2 != evennumbertest1:
    evensteven = "Odd"

if evensteven == "Even":
    columns = theinput/4
    columnscheck = theinput//4
    if columnscheck == columns:
        oddtodd = "Even"
        make4columns = theinput/4
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput-6 >= 4:
            make3columns = 2
            make4columns = ((theinput-6)/4)
        elif theinput == 2:
            make2columns = 1
        elif theinput == 6:
            make3columns = 2
            
if evensteven == "Odd":
    columns = theinput/3
    columnscheck = theinput//3
    if columnscheck == columns:
        oddtodd = "Even"
        if theinput == 3:
            make3columns = 1
        elif theinput == 9:
            make3columns = 3
        elif theinput != 3:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
    elif columnscheck != columns:
        oddtodd = "Odd"
        if theinput == 1:
            make1column = 1
        elif theinput == 5:
            make3columns = 1
            make2columns = 1
        elif theinput-3 >= 3 and (theinput-3)/4 == (theinput-3)//4:
            columns = (theinput-3)/4
            columnscheck = (theinput-3)//4
            make3columns = 1
            make4columns = ((theinput-3)/4)
        elif (theinput-3)/4 != (theinput-3)//4:
            while theinput >= 5 and theinput != 5:
                make4columns = make4columns+1
                theinput = theinput-4
            if theinput == 1:
                make1column = 1
            elif theinput == 3:
                make3columns = 1
            elif theinput == 5:
                make3columns = 1
                make2columns = 1
make4columns = int(make4columns)
#Photos Sorted

westernsignalhtml = ""
westernsignalbegincount = name-westernsignalcount
westernsignalcounter = 0

for i in range(make1column):
    westernsignalcounter = westernsignalcounter + 1
    westernsignalhtml = westernsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
    </tr>
  </tbody>
</table>
"""

for i in range(make2columns):
    westernsignalcounter = westernsignalcounter + 1
    westernsignalhtml = westernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+""" " style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
</tr>
<tr>
</tbody>
</table>
"""
    westernsignalcounter = westernsignalcounter + 1

for i in range(make3columns):
    westernsignalcounter = westernsignalcounter + 1
    westernsignalhtml = westernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+""" " alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+""" " alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    westernsignalcounter = westernsignalcounter + 2

for i in range(make4columns):
    westernsignalcounter = westernsignalcounter + 1
    westernsignalhtml = westernsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+""" "
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src=" """ "T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+3]+""" "
alt=""></font></font></strong></a></span></td>
</tr>
</tbody>
</table>
"""
    westernsignalcounter = westernsignalcounter + 3
if westernsignalhtml !="":
    westernsignalhtml = westernsignalhtml+ """
    <table width="100%" border="1">
      <tbody>
        <tr>
          <td align="center" valign="middle">The western signal.</td>
        </tr>
      </tbody>
    </table>
    """
#Sorted Western Signal

"""Sort Relay Case And Grade Photo ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

RelayCase = False
Grade = False
Relaycaseimagecount = 0
RelayCasehtml = ""
Gradehtml = ""

source = 'Relay_Case/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    RelayCase = True
    Relaycaseimagecount = Relaycaseimagecount + 1
    RelayCasehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)


#Sorted Relay Case Photo

#Sort Grade Photo

source = 'Grade/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    Grade = True
    Relaycaseimagecount = Relaycaseimagecount + 1
    Gradehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing South Track Photo

#Sort Relay Case and Grade Photos

relayandgradehtml = ""
relayheaderhtml = ""
gradeheaderhtml = ""
FacingWidth = "100"

if Relaycaseimagecount == 4:
    FacingWidth = "25"
if Relaycaseimagecount == 3:
    FacingWidth = "33"
if Relaycaseimagecount == 2:
    FacingWidth = "50"
if Relaycaseimagecount == 1:
    FacingWidth = "100"

if RelayCase == True:
    relayheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The relay case.</td>"""
if Grade == True:
    gradeheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""

relayandgradehtml = relayandgradehtml+"""
"""+RelayCasehtml+"""
"""+Gradehtml+"""
</tr>
<tr>
"""+relayheaderhtml+"""
"""+gradeheaderhtml+"""
</tr>
"""

if RelayCase == True or Grade == True:
    relayandgradehtml = """<table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
<tbody>"""+relayandgradehtml+"""</tbody>
</table>"""

#Sorted Relay Case And Grade Photos

"""Sort Facing North Track Photo ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

TFacingNorth = False
TFacingSouth = False
TFacingEast = False
TFacingWest = False
TFacingImageCount = 0
TFacingNorthhtml = ""
TFacingSouthhtml = ""
TFacingEasthtml = ""
TFacingWesthtml = ""

source = 'Track_Views/Track_View_North/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    TFacingNorth = True
    TFacingImageCount = TFacingImageCount + 1
    TFacingNorthhtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)


#Sorted Facing North Track Photo

#Sort Facing South Track Photo

source = 'Track_Views/Track_View_South/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    TFacingSouth = True
    TFacingImageCount = TFacingImageCount + 1
    TFacingSouthhtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing South Track Photo

#Sort Facing East Track Photo

source = 'Track_Views/Track_View_East/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    TFacingEast = True
    TFacingImageCount = TFacingImageCount + 1
    TFacingEasthtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing East Track Photo

#Sort Facing West Track Photo

source = 'Track_Views/Track_View_West/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    name = name + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    TFacingWest = True
    TFacingImageCount = TFacingImageCount + 1
    TFacingWesthtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src=" """ "T"+Filenamelist[name-1]+""" "></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    if f[0] == "T": 
      image = Image.open('Output/'+fullname+"/"+filename)
      image.thumbnail((160, 160))
      image.save('Output/'+fullname+"/"+filename)

#Sorted Facing West Track Photo

#Sort Header Photo

source = 'Header'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)

HeaderFilename = ""
 
# iterate on all files to move them to destination folder
for f in allfiles:
    filename = f
    HeaderFilename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files

    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, f)
    os.rename(src_path, dst_path)

#Sorted Header Photo


if name != 1:
    prGreen("""
Processed """+str(name)+""" Photos!
""")
if name == 0:
    prRed("""0 Photos Were Detected, Make Sure You Put Your Photos In The Correct Folders!
""")
if name == 1:
    prGreen("""
Processed 1 Photo!
""")

#Sort Track Overview Photos

trackfacinghtml = ""
TNorthImageHeaderhtml = ""
TSouthImageHeaderhtml = ""
TEastImageHeaderhtml = ""
TWestImageHeaderhtml = ""
FacingWidth = "100"

if TFacingImageCount == 4:
    TFacingWidth = "25"
if TFacingImageCount == 3:
    TFacingWidth = "33"
if TFacingImageCount == 2:
    TFacingWidth = "50"
if TFacingImageCount == 1:
    TFacingWidth = "100"

if TFacingNorth == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name North Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US-64.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TNorthStreet = input("Track view facing north towards: ")
    if TNorthStreet != "":
        print("""
--This Might Be A Little Hard, You Will Have To Make A Link. Examples Are Listed Below

Crossing Link Examples:

--Cherry Grove Rd.--
--http://www.rxrsignals.com/Illinois/L-Q/Mason_City/Cherry_Grove/--

--80th Ave--
--http://www.rxrsignals.com/Iowa/A-K/Agency/80/--

--Barron St.--
--http://www.rxrsignals.com/Ohio/A-K/Eaton/Barron/--

--Sohl Ave. #2--
--http://www.rxrsignals.com/Indiana/A-K/Hammond/Sohl2/--

--Waldron St.--
--https://www.rxrsignals.com/Mississippi/A-F/Corinth/Waldron/--

--Don't Forget To Add The Correct City In The Link!
""")
        TNorthStreetLink = input("Crossing Link? ")
        TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north towards <a href=" """+TNorthStreetLink+""" ">"""+TNorthStreet+"""</a></td>"""

    elif TNorthStreet == "":
        TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north.</td>"""

if TFacingSouth == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name South Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US-64.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TSouthStreet = input("Track view facing south towards: ")
    if TSouthStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Examples Are Listed Below!

Crossing Link Examples:

--Cherry Grove Rd.--
--http://www.rxrsignals.com/Illinois/L-Q/Mason_City/Cherry_Grove/--

--80th Ave--
--http://www.rxrsignals.com/Iowa/A-K/Agency/80/--

--Barron St.--
--http://www.rxrsignals.com/Ohio/A-K/Eaton/Barron/--

--Sohl Ave. #2--
--http://www.rxrsignals.com/Indiana/A-K/Hammond/Sohl2/--

--Waldron St.--
--https://www.rxrsignals.com/Mississippi/A-F/Corinth/Waldron/--

--Don't Forget To Add The Correct City In The Link!
""")
        TSouthStreetLink = input("Crossing Link? ")
        TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south towards <a href=" """+TSouthStreetLink+""" ">"""+TSouthStreet+"""</a></td>"""

    elif TSouthStreet == "":
        TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south.</td>"""

if TFacingEast == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name East Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US-64.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TEastStreet = input("Track view facing east towards: ")
    if TEastStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Examples Are Listed Below!

Crossing Link Examples:

--Cherry Grove Rd.--
--http://www.rxrsignals.com/Illinois/L-Q/Mason_City/Cherry_Grove/--

--80th Ave--
--http://www.rxrsignals.com/Iowa/A-K/Agency/80/--

--Barron St.--
--http://www.rxrsignals.com/Ohio/A-K/Eaton/Barron/--

--Sohl Ave. #2--
--http://www.rxrsignals.com/Indiana/A-K/Hammond/Sohl2/--

--Waldron St.--
--https://www.rxrsignals.com/Mississippi/A-F/Corinth/Waldron/--

Don't Forget To Add The Correct City In The Link!
""")
        TEastStreetLink = input("Crossing Link? ")
        TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east towards <a href=" """+TEastStreetLink+""" ">"""+TEastStreet+"""</a></td>"""

    elif TEastStreet == "":
        TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east.</td>"""

if TFacingWest == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name West Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US-64.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TWestStreet = input("Track view facing west towards: ")
    if TWestStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Examples Are Listed Below!

Crossing Link Examples:

--Cherry Grove Rd.--
--http://www.rxrsignals.com/Illinois/L-Q/Mason_City/Cherry_Grove/--

--80th Ave--
--http://www.rxrsignals.com/Iowa/A-K/Agency/80/--

--Barron St.--
--http://www.rxrsignals.com/Ohio/A-K/Eaton/Barron/--

--Sohl Ave. #2--
--http://www.rxrsignals.com/Indiana/A-K/Hammond/Sohl2/--

--Waldron St.--
--https://www.rxrsignals.com/Mississippi/A-F/Corinth/Waldron/--

--Don't Forget To Add The Correct City In The Link!
""")
        TWestStreetLink = input("Crossing Link? ")
        TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west towards <a href=" """+TWestStreetLink+""" ">"""+TWestStreet+"""</a></td>"""

    elif TWestStreet == "":
        TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west.</td>"""

trackfacinghtml = trackfacinghtml+"""
"""+TFacingNorthhtml+"""
"""+TFacingSouthhtml+"""
"""+TFacingEasthtml+"""
"""+TFacingWesthtml+"""
</tr>
<tr>
"""+TNorthImageHeaderhtml+"""
"""+TSouthImageHeaderhtml+"""
"""+TEastImageHeaderhtml+"""
"""+TWestImageHeaderhtml+"""
</tr>
"""

if TFacingSouth == True or TFacingNorth == True or TFacingEast == True or TFacingWest == True:
    trackfacinghtml = """<table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
<tbody>"""+trackfacinghtml+"""</tbody>
</table>"""

"""Sorted Track Overview Photos ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

#Photo Dates And Credit

print("""--When Were These Photos Taken?

Date Examples: 
--Feburary 20, 2023--
--April 19, 2025--
--October 3, 2021--

--Don't Forget To NOT (I REPEAT DO NOT) Add A "." or "," At The End!""")
PhotoDates = input("""
Pictures 1-"""+str(name)+""" were taken on """)

print("""
--Who Took These Photos? (Probably You)

Username Examples: 
--Hopen65--
--Baahcause--
--Tommyinit--
--ExpensiveBrickProductions--
--MOKC Railfan--
--Kyle the Railfanner--

--Basically Input The Name You Use To Refer To Yourself Or Something.
""")
Username = input("""Pictures 1-"""+str(name)+""" were taken on """+PhotoDates+""", by """)

print("""
--Who Created This Page (Definitely You)

Creator Name Examples: 
--Hopen65--
--Baahcause--
--Tommyinit--
--ExpensiveBrickProductions--
--MOKC Railfan--
--Kyle the Railfanner--

--Basically Input The Name You Use To Refer To Yourself Or Something Again.
""")
Creator = input("Page Created By? ")

pagecreatedhtml = """Page created by """+Creator+""" (with MikeRXRTools """+DISPLAYVERSION+""")."""
if Creator == "":
    pagecreatedhtml =""

print("""
--What Is The Railroad Subdivision?

Subdivision Examples: 
--BNSF Bayard Subdivision--
--UP Clinton Subdivision--
--NS Chicago District--
--CPKC Chicago Subdivision--
--CN Champaign Subdivision--
--CSX Alleghany Subdivision--

If The Railroad Is A Class III Railroad Without Subdivisions, Then Type The Full Railroad Name Like This:
--Iowa River Railroad--
--Iowa Traction Railroad--
--Cincinnati Eastern Railroad--
--Boone and Scenic Valley Railroad--
--Deseret Power Railway--
--Strasburg Railroad--

Don't Forget To NOT (I REPEAT DO NOT) Add A "." or "," At The End!
""")

Subdivision = input("This crossing is located on the ")

#Make Video Embeded

print("""
--Basically Just Paste In A Youtube Link And Then Press ENTER. Next It Will Ask For A Second Video
--Repeat Until You Have No More Videos, Then Press ENTER without Inputing Anything
""")

VideoHTML = ""
Videoi = 1
VideoInput = " "
while VideoInput != "":
    VideoInput = input("Youtube Video "+str(Videoi)+" " )
    if VideoInput != "":
        Videoi = Videoi + 1
        VideoLength = len(VideoInput)
        if VideoInput[0:17] == "https://youtu.be/":
            VideoHTMLInput = VideoInput[17:VideoLength-15]
        elif VideoInput[0:17] != "https://youtu.be/":
            VideoHTMLInput = VideoInput[32:VideoLength]
        VideoHTML = VideoHTML+"""</div><div style="text-align: center;"><iframe src="https://www.youtube.com/embed/"""+VideoHTMLInput+""" " allowfullscreen="" frameborder="0" height="540" width="960">&amp;lt;br&amp;gt;
</iframe>
</div>
<br>"""
#Made Video Embeded

#Make Crossing Table

if North == True or South == True or East == True or West == True:
    print("""
--Now, You Need To Fill In The Blanks For What Crossing Parts Are At This Crossing
--First, You Start With The Northern Signal, Then Southern, Eastern, And Western Signal, Then You Are Done!
--You Will Need To Use Your Photos To Find Out What Crossing Parts Make Up Each Signal
--If You Aren't Familiar With Crossing Parts, You Can Use The /102/ Page On The Site To Guide You:
http://www.rxrsignals.com/102/
--Some Examples For Crossing Parts Listed On This Table Are:

-----------------------------------------
   Bell:       | N/A
   Base:       | Modern Industries
Light Brackets:| Safetran
  Lights:      | 4 - 8"x20" Safetran incandescents
Gate Lights:   | 4" RECO
Gate Mechanism:| Safetran Late 1970's
Gate Striping: | Vertical Striping
-----------------------------------------

-----------------------------------------
   Bell:       | GS Type 2 E-Bell
   Base:       | Safetran 5" Single Sided
Light Brackets:| Safetran
  Lights:      | 4 - 12"x20" Safetran w/ Dialight Ball LEDs
 Gate Lights:  | 3 - 4" RECO LEDs
Gate Mechanism:| Siemens Imprinted
Gate Striping: | Diagonal Striping
-----------------------------------------

--You Can Also Look Around In The Site To Find More Examples Like These
--If There Is No Cantilever On Any Of The Signals At This Crossing, Just Press ENTER Every Time You Are Asked 
--For The Cantilever And Then The Cantilever Row Will Not Appear On The Table At All!

--If You Don't Want To Do This Part, Just Press ENTER Until You Reach The End 
--Then Edit Out The Crossing Table With An HTML Editor Such As KompoZer
""")

tableheaderhtml = ""

northbellhtml = ""
north_cant_html = ""
north_base_html = ""
north_bracket_html = ""
north_lights_html = ""
north_gate_lights_html = ""
north_gate_html = ""
north_gate_str_html = ""

north_cant = ""
north_gate_lights = ""
north_gate = ""
north_gate_str = ""

southbellhtml = ""
south_cant_html = ""
south_base_html = ""
south_bracket_html = ""
south_lights_html = ""
south_gate_lights_html = ""
south_gate_html = ""
south_gate_str_html = ""

south_cant = ""
south_gate_lights = ""
south_gate = ""
south_gate_str = ""

eastbellhtml = ""
east_cant_html = ""
east_base_html = ""
east_bracket_html = ""
east_lights_html = ""
east_gate_lights_html = ""
east_gate_html = ""
east_gate_str_html = ""

east_cant = ""
east_gate_lights = ""
east_gate = ""
east_gate_str = ""

westbellhtml = ""
west_cant_html = ""
west_base_html = ""
west_bracket_html = ""
west_lights_html = ""
west_gate_lights_html = ""
west_gate_html = ""
west_gate_str_html = ""

west_cant = ""
west_gate_lights = ""
west_gate = ""
west_gate_str = ""

if North == True:
    print("--Northern Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Northern Signal</em></strong></td>"""
    northbell = input("Northern Bell? ")
    northbellhtml = """<td style="text-align: center">"""+northbell+"""</td>"""
    north_cant = input("Northern Cantilever? ")
    north_cant_html = """<td style="text-align: center">"""+north_cant+"""</td>"""
    north_base = input("Northern Base? ")
    north_base_html = """<td style="text-align: center">"""+north_base+"""</td>"""
    north_bracket = input("Northern Light Bracket? ")
    north_bracket_html = """<td style="text-align: center">"""+north_bracket+"""</td>"""
    north_lights = input("Northern Lights? ")
    north_lights_html = """<td style="text-align: center">"""+north_lights+"""</td>"""
    north_gate_lights = input("Northern Gate Lights? ")
    north_gate_lights_html = """<td style="text-align: center">"""+north_gate_lights+"""</td>"""
    north_gate = input("Northern Gate Mechanism? ")
    north_gate_html = """<td style="text-align: center">"""+north_gate+"""</td>"""
    north_gate_str = input("Northern Gate Striping? ")
    north_gate_str_html = """<td style="text-align: center">"""+north_gate_str+"""</td>"""
if South == True:
    print("--Southern Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Southern Signal</em></strong></td>"""
    southbell = input("Southern Bell? ")
    southbellhtml = """<td style="text-align: center">"""+southbell+"""</td>"""
    south_cant = input("Southern Cantilever? ")
    south_cant_html = """<td style="text-align: center">"""+south_cant+"""</td>"""
    south_base = input("Southern Base? ")
    south_base_html = """<td style="text-align: center">"""+south_base+"""</td>"""
    south_bracket = input("Southern Light Bracket? ")
    south_bracket_html = """<td style="text-align: center">"""+south_bracket+"""</td>"""
    south_lights = input("Southern Lights? ")
    south_lights_html = """<td style="text-align: center">"""+south_lights+"""</td>"""
    south_gate_lights = input("Southern Gate Lights? ")
    south_gate_lights_html = """<td style="text-align: center">"""+south_gate_lights+"""</td>"""
    south_gate = input("Southern Gate Mechanism? ")
    south_gate_html = """<td style="text-align: center">"""+south_gate+"""</td>"""
    south_gate_str = input("Southern Gate Striping? ")
    south_gate_str_html = """<td style="text-align: center">"""+south_gate_str+"""</td>"""
if East == True:
    print("--Eastern Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Eastern Signal</em></strong></td>"""
    eastbell = input("Eastern Bell? ")
    eastbellhtml = """<td style="text-align: center">"""+eastbell+"""</td>"""
    east_cant = input("Eastern Cantilever? ")
    east_cant_html = """<td style="text-align: center">"""+east_cant+"""</td>"""
    east_base = input("Eastern Base? ")
    east_base_html = """<td style="text-align: center">"""+east_base+"""</td>"""
    east_bracket = input("Eastern Light Bracket? ")
    east_bracket_html = """<td style="text-align: center">"""+east_bracket+"""</td>"""
    east_lights = input("Eastern Lights? ")
    east_lights_html = """<td style="text-align: center">"""+east_lights+"""</td>"""
    east_gate_lights = input("Eastern Gate Lights? ")
    east_gate_lights_html = """<td style="text-align: center">"""+east_gate_lights+"""</td>"""
    east_gate = input("Eastern Gate Mechanism? ")
    east_gate_html = """<td style="text-align: center">"""+east_gate+"""</td>"""
    east_gate_str = input("Eastern Gate Striping? ")
    east_gate_str_html = """<td style="text-align: center">"""+east_gate_str+"""</td>"""
if West == True:
    print("--Western Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Western Signal</em></strong></td>"""
    westbell = input("Western Bell? ")
    westbellhtml = """<td style="text-align: center">"""+westbell+"""</td>"""
    west_cant = input("Western Cantilever? ")
    west_cant_html = """<td style="text-align: center">"""+west_cant+"""</td>"""
    west_base = input("Western Base? ")
    west_base_html = """<td style="text-align: center">"""+west_base+"""</td>"""
    west_bracket = input("Western Light Bracket? ")
    west_bracket_html = """<td style="text-align: center">"""+west_bracket+"""</td>"""
    west_lights = input("Western Lights? ")
    west_lights_html = """<td style="text-align: center">"""+west_lights+"""</td>"""
    west_gate_lights = input("Western Gate Lights? ")
    west_gate_lights_html = """<td style="text-align: center">"""+west_gate_lights+"""</td>"""
    west_gate = input("Western Gate Mechanism? ")
    west_gate_html = """<td style="text-align: center">"""+west_gate+"""</td>"""
    west_gate_str = input("Western Gate Striping? ")
    west_gate_str_html = """<td style="text-align: center">"""+west_gate_str+"""</td>"""

removecantileverhtml = """<tr>
      <td height="22" style="text-align: center">Cantilever:</td>
       """+north_cant_html+"""
       """+south_cant_html+"""
       """+east_cant_html+"""
       """+west_cant_html+"""
      </tr>"""
if north_cant == "" and south_cant == "" and east_cant == "" and west_cant == "":
    removecantileverhtml = ""
    
removegatelightshtml = """<tr>
      <td height="22" style="text-align: center">Gate Lights:</td>
      """+north_gate_lights_html+"""
      """+south_gate_lights_html+"""
      """+east_gate_lights_html+"""
      """+west_gate_lights_html+"""
      </tr>"""
if north_gate_lights == "" and south_gate_lights == "" and east_gate_lights == "" and west_gate_lights == "":
    removegatelightshtml = ""

removegateshtml = """<tr>
      <td height="22" style="text-align: center">Gate Mechanism:</td>
      """+north_gate_html+"""
      """+south_gate_html+"""
      """+east_gate_html+"""
      """+west_gate_html+"""
      </tr>"""
if north_gate == "" and south_gate == "" and east_gate == "" and west_gate == "":
    removegateshtml = ""
    
removegatestripehtml = """<tr>
      <td height="22" style="text-align: center">Gate Striping:</td>
      """+north_gate_str_html+"""
      """+south_gate_str_html+"""
      """+east_gate_str_html+"""
      """+west_gate_str_html+"""
      </tr>"""
if north_gate_str == "" and south_gate_str == "" and east_gate_str == "" and west_gate_str == "":
    removegatestripehtml = ""

#Sort The HTML Together

tablehtml = """<table align="center" border="1">
  <tbody>
    <tr>
      <td width="126" height="22" style="text-align: center">&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</td>
      """+tableheaderhtml+"""
     
    </tr>
    <tr>
      <td height="22" style="text-align: center">Bell:</td>
      """+northbellhtml+"""
      """+southbellhtml+"""
      """+eastbellhtml+"""
      """+westbellhtml+"""
      </tr>
    """+removecantileverhtml+"""<tr>
      <td height="22" style="text-align: center">Base:</td>
      """+north_base_html+"""
      """+south_base_html+"""
      """+east_base_html+"""
      """+west_base_html+"""
      </tr>
    <tr>
<td style="text-align: center;">Light Bracket:</td>
"""+north_bracket_html+"""
"""+south_bracket_html+"""
"""+east_bracket_html+"""
"""+west_bracket_html+"""
</tr>
<tr>
      <td height="22" style="text-align: center">Lights:</td>
      """+north_lights_html+"""
      """+south_lights_html+"""
      """+east_lights_html+"""
      """+west_lights_html+"""
      </tr>
    """+removegatelightshtml+"""
    """+removegateshtml+"""
    """+removegatestripehtml+"""
  </tbody>
</table>"""

#Made Crossing Table

input("Program has not crashed! :D" )

# to open/create a new html file in the write mode
f = open('Output/'+fullname+"/"+fullnamehtml+'.html', 'w')
  
#Begin HTML
html_template = """<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>""" + crossing_name + " ("+ crossing_city +")"+ """</title>
<style type="text/css">
.Crossing_In_Action {
font-family: Verdana;
font-size: 14px;
font-weight: bold;
color: white;
}
.Recorded_Date {
font-weight: bold;
font-family: Verdana;
font-size: 10px;
color: white;
}

</style>
</head>
<body style="color: white; background-color: black;" alink="#ffccff"
link="white" vlink="#ffccff">
<table
style="width: 950px; text-align: left; margin-left: auto; margin-right: auto;"
border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td style="text-align: center; height: 140px; width: 667px;"><span
style="vertical-align: middle; text-align: center;"><img
style="width: 650px; height: 140px;" src=" """+HeaderFilename+""" "
alt=""></span></td>
<td style="width: 277px; text-align: center; vertical-align: middle;">"""+rrhtml+"""<br>



      <br>



      """+mpblankhtml+""""""+mphtml+"""</span><span
style="vertical-align: middle; text-align: center;"></span><span
style="vertical-align: middle; text-align: center;"></span><span
style="vertical-align: middle; text-align: center;">"""+quietzone+"""</td>
</tr>
</tbody>
</table>
<br>
<table
style="width: 77%; text-align: left; margin-left: auto; margin-right: auto;"
border="0" cellpadding="0" cellspacing="8">
<tbody>
<tr>
<td style="text-align: center; vertical-align: middle;"><span
style="vertical-align: middle; text-align: center;">"""+defunctxing+"""<img
src="http://www.rxrsignals.com/Graphics/Dates/Created.png" alt=""
height="24" width="98"><img
src="http://www.rxrsignals.com/Graphics/Dates/Blank.png" alt=""
height="24" width="9"></span><span
style="vertical-align: middle; text-align: center;"><img
style="width: """+str(width)+"""px; height: 24px;"
src="http://www.rxrsignals.com/Graphics/Dates/Month/"""+str(month)+""".png" alt=""></span><span
style="vertical-align: middle; text-align: center;"><img
src="http://www.rxrsignals.com/Graphics/Dates/Blank.png" alt=""
height="24" width="9"></span><span
style="vertical-align: middle; text-align: center;"><img
src="http://www.rxrsignals.com/Graphics/Dates/Year/"""+str(year)+""".png" alt=""</span></td>
</tr>
</tbody>
</table>
<br>
<table
style="width: 77%; height: 1%; text-align: left; margin-left: auto; margin-right: auto;"
border="0" cellpadding="0" cellspacing="0">
<tbody>
"""+crossingaccidentshtml+"""
"""+dothtmlblank+"""
<tr>
<td align="center" valign="middle"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
src="http://www.rxrsignals.com/Graphics/Daily_Trains/Daily/"""+crossing_daily+""".png" 
alt=""></font></font></strong><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
src="http://www.rxrsignals.com/Graphics/Daily_Trains/Blank.png" alt=""
height="12" width="7"><img src="http://www.rxrsignals.com/Graphics/Daily_Trains/Since/"""+crossing_asof+""".png" 
alt=""></font></font></strong></td>
</tr>
</tbody>
</table>
<br>
<div style="text-align: center;">
"""+tablehtml+"""
<br>
Pictures 1-"""+str(name)+""" were taken on """+PhotoDates+""", by """+Username+""".<br>
This crossing is located on the """+Subdivision+""".<br>
"""+pagecreatedhtml+"""<br>
</div>
<br>
"""+facingimagehtml+"""
"""+northernsignalhtml+"""
"""+southernsignalhtml+"""
"""+easternsignalhtml+"""
"""+westernsignalhtml+"""
"""+relayandgradehtml+"""
"""+trackfacinghtml+"""
<br>
"""+VideoHTML+"""
</body>
</html>
"""

#End HTML
  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()