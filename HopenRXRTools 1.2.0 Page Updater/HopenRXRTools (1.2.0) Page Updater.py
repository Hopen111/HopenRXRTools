VERSION = "1.2.0 Page Updater"
DISPLAYVERSION = "1.2.0 Page Updater"

import os

Filenamefix = """ " """
Filenamefix2 = Filenamefix[1:2]

def prRed(skk):print("\033[31m {}\033[00m".format(skk))
def inRed(skk):input("\033[31m {}\033[00m".format(skk))

def prYellow(skk): print("\033[33m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

print("""--HopenRXRTools """+VERSION+"""--""")
print("--Created by Hopen111--")

#Where To Begin Photo Count

print("")

try:
    HTMLFile = open("Input/index.html", 'r') 
    index = HTMLFile.read() 
except:
    inRed("""
No HTML File Found!
""")

sub_string = "</body>"
count_er=0
start_index=0

body_list = []

for i in range(len(index)):
    j = index.find(sub_string,start_index)
    if(j!=-1):
        start_index = j+1
        count_er+=1
        body_list.append(start_index-2)

indexbegin = index[0:body_list[len(body_list)-1]]
indexend = index[body_list[len(body_list)-1]:len(index)]

namecountfrom = input("Existing Photo Count? ")
if namecountfrom == "":
    namecountfrom = 0

UpdateText = input("Return Visit Notes? ")
if UpdateText == "":
    UpdateText = "Return visit text goes here."

namecountfrom = int(namecountfrom)

#What is done

#Street View Text
#Check For Header

StreetViewCheck = False

CheckForStreetView = os.listdir('Street_View')
for f in CheckForStreetView:
    StreetViewCheck = True

if StreetViewCheck == True:
    print("""
--Type Out The Text That Will Appear Below Your Street View Photos.
""")
    StreetViewText = input("Street View Photo Comments: ")
    if StreetViewText == "":
        StreetViewText = "Street view text goes here."


#Check If User Is Ready

prYellow("""
!WARNING! 
Any Photos Proccessed By HopenRXRTools Cannot Be Undone! 
Make Sure To Have A Backup Folder With All The Photos In The Event You Make A Typo Or Want 
To Make The Page Again (Or If The Program Straight Up Crashes).

Also, If The Program Detects A Crossing/Folder With The Same Street Name Already 
In The Output Folder, HopenRXRTools WILL Crash.

Any Issues Found Will Be Listed Below.""")

HeaderWorks = False
CheckForSameName = False
OverviewCheckNumber = 0
TrackCheckNumber = 0


#Check For Overview Photos

CheckForOverview = os.listdir('Overviews')
for f in CheckForOverview:
    OverviewCheckNumber = OverviewCheckNumber + 1

if OverviewCheckNumber >= 5:
    prRed("""
Overview Photos Found Outside Subfolders In The Overviews Folder!""")

#Overview Checked


#Check For Track View Photos

CheckForTracks = os.listdir('Track_Views')
for f in CheckForTracks:
    TrackCheckNumber = TrackCheckNumber + 1

if TrackCheckNumber >= 5:
    prRed("""
Track View Photos Found Outside Subfolders In The Track_Views Folder!""")

#Track View Checked

#Check For Same Folder Name

try:
    TestPath = "Output\index.html"
    TestPath2 = os.listdir(TestPath)
    prRed("""
Same Folder Name Found In Output Folder! Program Will Crash If The Folder With The Same Name Is Not Moved!""")
except:
    CheckForSameName = True


#Folder Name Checked


#If There Are No Issues

if HeaderWorks == True and CheckForSameName == True and TrackCheckNumber <= 5 and OverviewCheckNumber <= 5:
    prGreen("""
No Issues Found!""")

print("")
input("Press ENTER Twice To Begin Processing Photos")
input("Press ENTER Twice To Begin Processing Photos")

print("""
Processing Photos...""")

fullnamehtml = "index"



"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

import shutil
import PIL
import glob

from PIL import Image

name = namecountfrom
Sname = 0
Filenamelist = []
Filenamelist2= []
FacingWest = False
FacingEast = False
FacingNorth = False
FacingSouth = False
StreetView = False
North = False
South = False
East = False
West = False
FacingImageCount = 0
StreetViewhtml = ""
NorthImagehtml = ""
SouthImagehtml = ""
EastImagehtml = ""
WestImagehtml = ""

#Sort Street View Photos

source = 'Street_View/'
destination = 'Output/'
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
streetviewcount = 0
for f in allfiles:
    Sname = Sname + 1
    streetviewcount = streetviewcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist2.append(str(Sname)+filenameext)
    StreetView = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, "SV"+str(Sname)+filenameext)
    dst_pathT = os.path.join(destination, "TSV"+str(Sname)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

allTfiles = os.listdir(destination)

for f in allTfiles:
    filename = f
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

theinput = streetviewcount #Number of photos
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

streetviewhtml = ""
streetviewbegincount = Sname-streetviewcount
streetviewcounter = 0

for i in range(make1column):
    streetviewcounter = streetviewcounter + 1
    streetviewhtml = streetviewhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        streetviewhtml = streetviewhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">"""+StreetViewText+"""</td>
</tr>
</tbody>
</table>
"""
    else:
        streetviewhtml = streetviewhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    streetviewcounter = streetviewcounter + 1
    streetviewhtml = streetviewhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+1)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        streetviewhtml = streetviewhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">"""+StreetViewText+"""</td>
</tr>
</tbody>
</table>
"""
    else:
        streetviewhtml = streetviewhtml+ """
</tr>
</tbody>
</table>
"""
    streetviewcounter = streetviewcounter + 1

for i in range(make3columns):
    streetviewcounter = streetviewcounter + 1
    streetviewhtml = streetviewhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+1)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+2)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        streetviewhtml = streetviewhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">"""+StreetViewText+"""</td>
</tr>
</tbody>
</table>
"""
    else:
        streetviewhtml = streetviewhtml+ """
</tr>
</tbody>
</table>
"""
    streetviewcounter = streetviewcounter + 2

for i in range(make4columns):
    streetviewcounter = streetviewcounter + 1
    streetviewhtml = streetviewhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+1)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+2)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+3)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        streetviewhtml = streetviewhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">"""+StreetViewText+"""</td>
</tr>
</tbody>
</table>
"""
    else:
        streetviewhtml = streetviewhtml+ """
</tr>
</tbody>
</table>
"""
    streetviewcounter = streetviewcounter + 3

#Street View Sorted

#Sort Facing North Photo

source = 'Overviews/Overview_Facing_North/'
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)


#Sorted Facing North Photo

#Sort Facing South Photo

source = 'Overviews/Overview_Facing_South/'
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

#Sorted Facing South Photo

#Sort Facing East Photo

source = 'Overviews/Overview_Facing_East/'
destination = 'Output/'

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

#Sorted Facing East Photo

#Sort Facing West Photo

source = 'Overviews/Overview_Facing_West/'
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

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
destination = 'Output/'
 
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

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
northernsignalbegincount = name-northernsignalcount-namecountfrom
northernsignalcounter = 0

for i in range(make1column):
    northernsignalcounter = northernsignalcounter + 1
    northernsignalhtml = northernsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        northernsignalhtml = northernsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The northern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernsignalhtml = northernsignalhtml+ """
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        northernsignalhtml = northernsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The northern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernsignalhtml = northernsignalhtml+ """
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        northernsignalhtml = northernsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The northern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernsignalhtml = northernsignalhtml+ """
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
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+namecountfrom+3)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        northernsignalhtml = northernsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The northern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernsignalhtml = northernsignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernsignalcounter = northernsignalcounter + 3

#Northern Signal Sorted

#Sort Southern Signal Photos

source = 'Southern_Signal/'
destination = 'Output/'
 
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

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
southernsignalbegincount = name-southernsignalcount-namecountfrom
southernsignalcounter = 0

for i in range(make1column):
    southernsignalcounter = southernsignalcounter + 1
    southernsignalhtml = southernsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        southernsignalhtml = southernsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The southern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernsignalhtml = southernsignalhtml+ """
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        southernsignalhtml = southernsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The southern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernsignalhtml = southernsignalhtml+ """
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        southernsignalhtml = southernsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The southern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernsignalhtml = southernsignalhtml+ """
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
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+namecountfrom+3)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        southernsignalhtml = southernsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The southern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernsignalhtml = southernsignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernsignalcounter = southernsignalcounter + 3

#Southern Signal Sorted

#Sort Eastern Signal Photos

source = 'Eastern_Signal/'
destination = 'Output/'
 
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

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
easternsignalbegincount = name-easternsignalcount-namecountfrom
easternsignalcounter = 0

for i in range(make1column):
    easternsignalcounter = easternsignalcounter + 1
    easternsignalhtml = easternsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        easternsignalhtml = easternsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The eastern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternsignalhtml = easternsignalhtml+ """
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        easternsignalhtml = easternsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The eastern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternsignalhtml = easternsignalhtml+ """
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        easternsignalhtml = easternsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The eastern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternsignalhtml = easternsignalhtml+ """
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
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+namecountfrom+3)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        easternsignalhtml = easternsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The eastern signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternsignalhtml = easternsignalhtml+ """
</tr>
</tbody>
</table>
"""

    easternsignalcounter = easternsignalcounter + 3

#Sorted Eastern Signal

#Sort Western Signal Photos

source = 'Western_Signal/'
destination = 'Output/'
 
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

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
westernsignalbegincount = name-westernsignalcount-namecountfrom
westernsignalcounter = 0

for i in range(make1column):
    westernsignalcounter = westernsignalcounter + 1
    westernsignalhtml = westernsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        westernsignalhtml = westernsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The western signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernsignalhtml = westernsignalhtml+ """
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+""" style="border: 0px solid ;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        westernsignalhtml = westernsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The western signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernsignalhtml = westernsignalhtml+ """
</tr>
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        westernsignalhtml = westernsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The western signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernsignalhtml = westernsignalhtml+ """
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
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom+2)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+namecountfrom+3)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid ;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        westernsignalhtml = westernsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The western signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernsignalhtml = westernsignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernsignalcounter = westernsignalcounter + 3

#Sorted Western Signal

"""Sort Relay Bungalow And Grade Photo ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

TrackRelayNumber = 0
RelayBungalow = False
Grade = False
RelayBungalowimagecount = 0
RelayBungalowhtml = ""
Gradehtml = ""

source = 'Relay_Bungalow/'
destination = 'Output/'
 
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
    RelayBungalow = True
    RelayBungalowimagecount = RelayBungalowimagecount + 1
    RelayBungalowhtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)


#Sorted Relay Bungalow Photo

#Sort Grade Photo

source = 'Grade/'
destination = 'Output/'
 
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
    RelayBungalowimagecount = RelayBungalowimagecount + 1
    Gradehtml = """
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

#Sorted Facing South Track Photo

#Sort Relay Bungalow and Grade Photos

relayandgradehtml = ""
relayheaderhtml = ""
gradeheaderhtml = ""
FacingWidth = "100"

if RelayBungalowimagecount == 4:
    FacingWidth = "25"
if RelayBungalowimagecount == 3:
    FacingWidth = "33"
if RelayBungalowimagecount == 2:
    FacingWidth = "50"
if RelayBungalowimagecount == 1:
    FacingWidth = "100"

if RelayBungalow == True:
    TrackRelayNumber = TrackRelayNumber + 1
    relayheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>"""
if Grade == True:
    TrackRelayNumber = TrackRelayNumber + 1
    gradeheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""

relayandgradehtml = relayandgradehtml+"""
"""+RelayBungalowhtml+"""
"""+Gradehtml+"""
</tr>
<tr>
"""+relayheaderhtml+"""
"""+gradeheaderhtml+"""
</tr>
"""

if RelayBungalow == True or Grade == True:
    relayandgradehtml = """<table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
<tbody>"""+relayandgradehtml+"""</tbody>
</table>"""

#Sorted Relay Bungalow And Grade Photos

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
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)


#Sorted Facing North Track Photo

#Sort Facing South Track Photo

source = 'Track_Views/Track_View_South/'
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

#Sorted Facing South Track Photo

#Sort Facing East Track Photo

source = 'Track_Views/Track_View_East/'
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

#Sorted Facing East Track Photo

#Sort Facing West Track Photo

source = 'Track_Views/Track_View_West/'
destination = 'Output/'
 
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-namecountfrom-1])+Filenamefix2+"""><img style="border: 0px solid ;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-namecountfrom-1]+Filenamefix2+"""></a><br>
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
    image = Image.open('Output/'+filename)
    image.thumbnail((1600, 1600))
    image.save('Output/'+filename)
    if f[0] == "T": 
      image = Image.open('Output/'+filename)
      image.thumbnail((214, 214))
      if image.size[1] != 120 and image.size[0] != 120:
          image.thumbnail((160, 160))
      image.save('Output/'+filename)

#Sorted Facing West Track Photo

if name+Sname-namecountfrom != 1:
    prGreen("""
Processed """+str(name+Sname-namecountfrom)+""" Photos!""")
if name+Sname-namecountfrom == 0:
    prRed("""
0 Photos Were Detected, Make Sure You Put Your Photos In The Correct Folders!""")
if name+Sname-namecountfrom == 1:
    prGreen("""
Processed 1 Photo!""")
print("")

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
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TNorthStreet = input("Track view facing north towards: ")
    if TNorthStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Rules Are Listed Below!

--We Will Be Using ../ To Direct The Link To The Crossing Next To This One.

--If It Is Just To Another Crossing In The Same City/Town, Just Add One: ../Road_Name
--If It Leads To Another City, Add Two: ../../City_Name/Road_Name
--If It Leads To Another City, And Is In Another Alphabetical Group, Such As A-F Or G-Q, 
Add Three: ../../../A-K/City_Name/Road_Name
--If It Leads To Another State And It Isn't Different Letter Group, Add Three: ../../../State_Name/City_Name/Road_Name
--If It Leads To Another State And Different Letter Group, Add Four: ../../../../State_Name/A-K/City_Name/Road_Name

Crossing Link Examples:

--Cherry Grove Rd.--
--../Cherry--

--80th Ave--
--../80--

--Barron St. (Different Town)--
--../../Different_Town/Barron--

--Sohl Ave. #2--
--../Sohl2--

--Waldron St. (Different Town And Different Alphabet Catagory--
--../../../A-K/Different_Town/Waldron--
""")
        TNorthStreetLink = input("Crossing Link? ")
        TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north towards <a href="""+Filenamefix2+TNorthStreetLink+Filenamefix2+""">"""+TNorthStreet+"""</a></td>"""

    elif TNorthStreet == "":
        TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north.</td>"""

if TFacingSouth == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name South Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TSouthStreet = input("Track view facing south towards: ")
    if TSouthStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Rules Are Listed Below!

--We Will Be Using ../ To Direct The Link To The Crossing Next To This One.

--If It Is Just To Another Crossing In The Same City/Town, Just Add One: ../Road_Name
--If It Leads To Another City, Add Two: ../../City_Name/Road_Name
--If It Leads To Another City, And Is In Another Alphabetical Group, Such As A-F Or G-Q, 
Add Three: ../../../A-K/City_Name/Road_Name
--If It Leads To Another State And It Isn't Different Letter Group, Add Three: ../../../State_Name/City_Name/Road_Name
--If It Leads To Another State And Different Letter Group, Add Four: ../../../../State_Name/A-K/City_Name/Road_Name

Crossing Link Examples:

--Cherry Grove Rd.--
--../Cherry--

--80th Ave--
--../80--

--Barron St. (Different Town)--
--../../Different_Town/Barron--

--Sohl Ave. #2--
--../Sohl2--

--Waldron St. (Different Town And Different Alphabet Catagory--
--../../../A-K/Different_Town/Waldron--
""")
        TSouthStreetLink = input("Crossing Link? ")
        TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south towards <a href="""+Filenamefix2+TSouthStreetLink+Filenamefix2+""">"""+TSouthStreet+"""</a></td>"""

    elif TSouthStreet == "":
        TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south.</td>"""

if TFacingEast == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name East Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TEastStreet = input("Track view facing east towards: ")
    if TEastStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Rules Are Listed Below!

--We Will Be Using ../ To Direct The Link To The Crossing Next To This One.

--If It Is Just To Another Crossing In The Same City/Town, Just Add One: ../Road_Name
--If It Leads To Another City, Add Two: ../../City_Name/Road_Name
--If It Leads To Another City, And Is In Another Alphabetical Group, Such As A-F Or G-Q, 
Add Three: ../../../A-K/City_Name/Road_Name
--If It Leads To Another State And It Isn't Different Letter Group, Add Three: ../../../State_Name/City_Name/Road_Name
--If It Leads To Another State And Different Letter Group, Add Four: ../../../../State_Name/A-K/City_Name/Road_Name

Crossing Link Examples:

--Cherry Grove Rd.--
--../Cherry--

--80th Ave--
--../80--

--Barron St. (Different Town)--
--../../Different_Town/Barron--

--Sohl Ave. #2--
--../Sohl2--

--Waldron St. (Different Town And Different Alphabet Catagory--
--../../../A-K/Different_Town/Waldron--
""")
        TEastStreetLink = input("Crossing Link? ")
        TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east towards <a href="""+Filenamefix2+TEastStreetLink+Filenamefix2+""">"""+TEastStreet+"""</a></td>"""

    elif TEastStreet == "":
        TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east.</td>"""

if TFacingWest == True:
    print("""--Next, You Will Have To Find The Next Crossing And It's Street Name West Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TWestStreet = input("Track view facing west towards: ")
    if TWestStreet != "":
        print("""
--This Next Part Might Be A Little Hard, You Will Have To Make A Link. Some Rules Are Listed Below!

--We Will Be Using ../ To Direct The Link To The Crossing Next To This One.

--If It Is Just To Another Crossing In The Same City/Town, Just Add One: ../Road_Name
--If It Leads To Another City, Add Two: ../../City_Name/Road_Name
--If It Leads To Another City, And Is In Another Alphabetical Group, Such As A-F Or G-Q, 
Add Three: ../../../A-K/City_Name/Road_Name
--If It Leads To Another State And It Isn't Different Letter Group, Add Three: ../../../State_Name/City_Name/Road_Name
--If It Leads To Another State And Different Letter Group, Add Four: ../../../../State_Name/A-K/City_Name/Road_Name

Crossing Link Examples:

--Cherry Grove Rd.--
--../Cherry--

--80th Ave--
--../80--

--Barron St. (Different Town)--
--../../Different_Town/Barron--

--Sohl Ave. #2--
--../Sohl2--

--Waldron St. (Different Town And Different Alphabet Catagory--
--../../../A-K/Different_Town/Waldron--
""")
        TWestStreetLink = input("Crossing Link? ")
        TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west towards <a href="""+Filenamefix2+TWestStreetLink+Filenamefix2+""">"""+TWestStreet+"""</a></td>"""

    elif TWestStreet == "":
        TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west.</td>"""

#Can Relay And Track View Be Merged?
TrackRelayNumber = TrackRelayNumber + TFacingImageCount
if TrackRelayNumber <= 4 and (TNorthImageHeaderhtml != "" or TSouthImageHeaderhtml != "" or TEastImageHeaderhtml != "" or TWestImageHeaderhtml != "") and (RelayBungalow == True or Grade == True): 
    if TrackRelayNumber == 4:
        TFacingWidth = "25"
        FacingWidth = "25"
    if TrackRelayNumber == 3:
        TFacingWidth = "33"
        FacingWidth = "33"
    if TrackRelayNumber == 2:
        TFacingWidth = "50"
        FacingWidth = "50"
    if TrackRelayNumber == 1:
        TFacingWidth = "100"
        FacingWidth = "100"

    if RelayBungalow == True:
        relayheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>"""
    if Grade == True:
        gradeheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""

    if TNorthImageHeaderhtml != "":
        if TNorthStreet != "":
            TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north towards <a href="""+Filenamefix2+TNorthStreetLink+Filenamefix2+""">"""+TNorthStreet+"""</a></td>"""
    
        elif TNorthStreet == "":
            TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north.</td>"""
    if TSouthImageHeaderhtml != "":
        if TSouthStreet != "":
            TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south towards <a href="""+Filenamefix2+TSouthStreetLink+Filenamefix2+""">"""+TSouthStreet+"""</a></td>"""
    
        elif TSouthStreet == "":
            TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south.</td>"""
    if TEastImageHeaderhtml != "":    
        if TEastStreet != "":
            TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east towards <a href="""+Filenamefix2+TEastStreetLink+Filenamefix2+""">"""+TEastStreet+"""</a></td>"""
    
        elif TEastStreet == "":
            TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east.</td>"""
    if TWestImageHeaderhtml != "":
        if TWestStreet != "":
            TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west towards <a href="""+Filenamefix2+TWestStreetLink+Filenamefix2+""">"""+TWestStreet+"""</a></td>"""
    
        elif TWestStreet == "":
            TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west.</td>"""

    trackfacinghtml = trackfacinghtml+"""
"""+RelayBungalowhtml+"""
"""+Gradehtml+"""
"""+TFacingNorthhtml+"""
"""+TFacingSouthhtml+"""
"""+TFacingEasthtml+"""
"""+TFacingWesthtml+"""
</tr>
<tr>
"""+relayheaderhtml+"""
"""+gradeheaderhtml+"""
"""+TNorthImageHeaderhtml+"""
"""+TSouthImageHeaderhtml+"""
"""+TEastImageHeaderhtml+"""
"""+TWestImageHeaderhtml+"""
</tr>
"""
    Gradehtml = ""
    RelayBungalowhtml = ""
    relayandgradehtml = ""

else:
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
        VideoHTML = VideoHTML+"""</div><div style="text-align: center;"><iframe src="https://www.youtube.com/embed/"""+VideoHTMLInput+Filenamefix2+""" allowfullscreen="" frameborder="0" height="540" width="960">&amp;lt;br&amp;gt;
</iframe>
</div>
<br>"""
#Made Video Embeded

input("Program has not crashed! :D" )

# to open/create a new html file in the write mode
f = open('Output/index.html', 'w')
  
#Begin HTML
html_template = indexbegin+"""
<br>
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="middle">"""+UpdateText+"""<br>
</td>
</tr>
</tbody>
</table>
<br>
"""+streetviewhtml+"""
"""+facingimagehtml+"""
"""+northernsignalhtml+"""
"""+southernsignalhtml+"""
"""+easternsignalhtml+"""
"""+westernsignalhtml+"""
"""+relayandgradehtml+"""
"""+trackfacinghtml+"""
<br>
"""+VideoHTML+"""
"""+indexend

#End HTML
  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()