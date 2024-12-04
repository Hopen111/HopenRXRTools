VERSION = "1.3.0"

idiit = """\\"""
thing = """ ' """

import os
os.system('color') #For colors to work on Windows 10

Filenamefix = """ " """
Filenamefix2 = Filenamefix[1:2]

def prRed(skk):print("\033[31m {}\033[00m".format(skk))
def inRed(skk):input("\033[31m {}\033[00m".format(skk))

def prYellow(skk): print("\033[33m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

print("""--HopenRXRTools """+VERSION+"""--""")
print("--Created by Hopen111--")

try:
    import PIL
except:
    inRed("""
PILLOW Library Not Found! Press ENTER To Begin Installation.""")
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])

def Typo_Fix(Text_Input, Type):
    try:
        if Type == 2 and Text_Input[len(Text_Input)-1] == ".":
            Text_Input = Text_Input[0:len(Text_Input)-1]
            prGreen("""
Typo Has Been Removed!""")
            return Text_Input
        elif Text_Input[len(Text_Input)-1] == " " or Text_Input[len(Text_Input)-1] == thing[1] or Text_Input[len(Text_Input)-1] == "/"  or Text_Input[len(Text_Input)-1] == "]" or Text_Input[len(Text_Input)-1] == idiit[0]:
            Text_Input = Text_Input[0:len(Text_Input)-1]
            if Type == 1:
                prGreen("""
Typo Has Been Removed!
""")
            else:
                prGreen("""
Typo Has Been Removed!""")
        return Text_Input
    except:
        return Text_Input
    return Text_Input

def Sort_Number(theinput):
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
    return [make4columns, make3columns, make2columns, make1column]

print("""
Please Fill Out The Info Below.""")

print("""
Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--US 64--
--Depot St. #2--

--Don't Forget To Add A "." When Needed!
""")
crossing_name = input("Crossing Street Name? ") #Crossing Street
crossing_name = Typo_Fix(crossing_name, 0)

print("""
Crossing City Examples: 
--Dedham, IA--
--Nickerson, NE--
--Chicago, IL--

--Don't Add A "."!
""")

crossing_city = input("Crossing City? ") #Crossing City
crossing_city = Typo_Fix(crossing_city, 0)

print("""
Creation Date Examples:
--January 2023--
--May 2024--
--April 2022--

You Can Also Type In The Date As MM/DD/YYYY.
""")

crossingdate = input("Page Creation Date? ") #Month & Year
crossingdate = Typo_Fix(crossingdate, 0)

digits = len(crossingdate)

datecheck = crossingdate.find("/")

day = 0

if crossingdate != "" and datecheck == -1:
    if crossingdate[digits-1] == " " and crossingdate != "":
        crossingdate = crossingdate[0:digits-1]
        digits = len(crossingdate)
if datecheck == -1:
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
   
    year = crossingdate[digits-4:digits]
else:
    if datecheck == 1:
        month = crossingdate[0]
    else:
        month = crossingdate[0]+crossingdate[1]
    #Month Sorted
   
    day = crossingdate[datecheck+1:digits-5]
   
    year = crossingdate[digits-4:digits]

day_html = ""
if day != 0:
    day_html = """<img src="http://www.rxrsignals.com/Graphics/Dates/Day/"""+str(day)+""".png" alt=""><img src="http://www.rxrsignals.com/Graphics/Dates/Blank.png" alt="" height="24" width="9">"""

# Sort DOT

print("""
DOT Number Examples: 
--377886R--
--190742P--
--385269T, 743706A--

--If You Don't Know How To Get Your Crossing DOT, First Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/ 
--Next, Find Your Crossing, Click On It, And Then Under "CROSSING", It Will Show The DOT Number
--You Can Also Use Your Photos Of The DOT Number And Just Copy It Here
--If You Still Cannot Find The DOT Number, You Can Type "UNKNOWN" In Full Caps Or "idk"
--If The Crossing Has No DOT Number Assigned, Type "N/A", "n/a", Or "Not Assigned"
--If This Crossing Is In A Country Without DOT Numbers, Type "ID" (Or "TC" If You Are In Canada)
--If The Crossing Is In A Country Without DOT Or ID Numbers, Press ENTER And The Number Will Not Appear
""")

dot = input("DOT Number(s)? ")
dot = Typo_Fix(dot, 0)

dotlist = []
dotcommacheck = "DOT"

if dot == "ID" or dot == "Id" or dot == "id":
    dot = input("ID Number(s)? ")
    dotcommacheck = "ID"
elif dot == "TC" or dot == "Tc" or dot == "tc":
    dot = input("TC Number(s)? ")
    dotcommacheck = "TC"

Dotdigits = len(dot)

for i in range(Dotdigits):
    DotDigitSorted = dot[0+i:1+i]
    if DotDigitSorted == " ": #Adds Space? It also replaces letters with blank
        DotDigitSorted ="Blank"
        dotlist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/DOT/"+DotDigitSorted+".png"+Filenamefix2+" alt="">")
    elif DotDigitSorted == ",": #Adds Comma
        DotDigitSorted ="Comma"
        if dotcommacheck == "DOT":
            dotcommacheck = "DOTS"
        elif dotcommacheck == "ID":
            dotcommacheck = "IDS"
        elif dotcommacheck == "TC":
            dotcommacheck = "TCS"
        dotlist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/DOT/"+DotDigitSorted+".png"+Filenamefix2+" alt="+Filenamefix2+","+Filenamefix2+">")
    else:
        dotlist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/DOT/"+DotDigitSorted+".png"+Filenamefix2+" alt="+Filenamefix2+DotDigitSorted+Filenamefix2+">")

dotlistlength = len(dotlist)

dothtml = ""
dotcommasizefix = "13"

for i in range(dotlistlength): #Should Create HTML
    dotsort = str(dotlist[0+i]) #Begin making HTML line 57
    dotcommasizefix = "13"
    if dotsort == """"http://www.rxrsignals.com/Graphics/DOT/Comma.png" alt=",">""":
    	dotcommasizefix = "5"
    dothtml = dothtml+"""<img style="width: """+dotcommasizefix+"""px; height: 20px;" src="""+dotsort+""""""

dothtmlblank = """<tr>
<td style="vertical-align: middle; text-align: center;"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="http://www.rxrsignals.com/Graphics/DOT/"""+dotcommacheck+""".png"><img style="width: 10px; height: 20px;" alt="" src="http://www.rxrsignals.com/Graphics/DOT/Blank.png">"""+dothtml+"""</font></font></strong></td>
</tr>"""
if dot == "":
    dothtmlblank = ""
if dot == "UNKNOWN" or dot == "Unknown" or dot == "unknown" or dot == "idk":
    dothtmlblank = """<tr>
<td style="vertical-align: middle; text-align: center;"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt=""
src="http://www.rxrsignals.com/Graphics/DOT/"""+dotcommacheck+""".png"><img
style="width: 10px; height: 20px;" alt=""
src="http://www.rxrsignals.com/Graphics/DOT/Blank.png"><img
style="width: 93px; height: 20px;" alt=""
src="http://www.rxrsignals.com/Graphics/DOT/Unknown.png"></font></font></strong></td>
</tr>"""
if dot == "N/A" or dot == "n/a" or dot == "Not Assigned" or dot == "not assigned" or dot == "Not assigned" or dot == "notassigned" or dot == "NotAssigned" or dot == "Notassigned":
    dothtmlblank = """<tr>
<td style="vertical-align: middle; text-align: center;"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt=""
src="http://www.rxrsignals.com/Graphics/DOT/"""+dotcommacheck+""".png"><img
style="width: 10px; height: 20px;" alt=""
src="http://www.rxrsignals.com/Graphics/DOT/Blank.png"><img
style="width: 141px; height: 20px;" alt=""
src="http://www.rxrsignals.com/Graphics/DOT/NOT_ASSIGNED.png"></font></font></strong></td>
</tr>"""

#DOT Sorted

#Sort Milepost

print("""
Milepost Examples: 
--20.25--
--289.77--
--255.78, 26.77--

--If You Don't Know How To Get Your Crossing Milepost, First Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/ 
--Next, Find Your Crossing, Click On It, And Then Scroll Down
--And Then Under "MILEPOST", It Will Show The Milepost Number
--If The Crossing Uses Metric Units, You Can Type "KMP"
--If You Still Cannot Find The MP Number, You Can Type "UNKNOWN" In Full Caps
""")

mp = input("Milepost? ")
mp = Typo_Fix(mp, 0)

KmpFix = "MP"
kmpsizefix = "46px; height: 20"

if mp == "KMP" or mp == "Kmp" or mp == "kmp" or mp == "KMp":
    mp = input("Kilometerpost? ")
    KmpFix = "KMP"
    kmpsizefix = "60px; height: 20"

mpdigits = len(mp)
mplist = []

for i in range(mpdigits):
    mpdigitsorted = mp[0+i:1+i]
    if mpdigitsorted == " ": #Adds Space? It also replaces letters with blank
        mpdigitsorted ="Blank"
        mplist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/Milepost_Numbers/"+mpdigitsorted+".PNG"+Filenamefix2+" alt="">")
    elif mpdigitsorted == ".": #Adds Comma
        mpdigitsorted ="Decimal"
        mplist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/Milepost_Numbers/"+mpdigitsorted+".PNG"+Filenamefix2+" alt="+Filenamefix2+"."+Filenamefix2+">")
    elif mpdigitsorted == ",": #Adds Comma
        mpdigitsorted ="Comma"
        mplist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/Milepost_Numbers/"+mpdigitsorted+".PNG"+Filenamefix2+" alt="+Filenamefix2+","+Filenamefix2+">")
    else:
        mplist.append(Filenamefix2+"http://www.rxrsignals.com/Graphics/Milepost_Numbers/"+mpdigitsorted+".PNG"+Filenamefix2+" alt="+Filenamefix2+mpdigitsorted+Filenamefix2+">")

mplistlength = len(mplist)

mphtml = ""
mpdecimalsizefix = "16"

for i in range(mplistlength): #Should Create HTML
    mpsort = str(mplist[0+i]) #Begin making HTML line 57
    mpdecimalsizefix = "16"
    if mpsort == """"http://www.rxrsignals.com/Graphics/Milepost_Numbers/Decimal.PNG" alt=".">""":
    	mpdecimalsizefix = "8"
    if mpsort == """"http://www.rxrsignals.com/Graphics/Milepost_Numbers/Comma.PNG" alt=",">""":
    	mpdecimalsizefix = "7"
    mphtml = mphtml+"""<img style="width: """+mpdecimalsizefix+"""px; height: 20px;" src="""+mpsort+""""""

mpblankhtml = """<img style="width: """+kmpsizefix+"""px;" alt="" src="http://www.rxrsignals.com/Graphics/Milepost_Numbers/"""+KmpFix+""".PNG"><img style="width: 16px; height: 20px;" alt="" src="http://www.rxrsignals.com/Graphics/Milepost_Numbers/Blank.PNG">"""
if mp == "":
    mpblankhtml = ""
if mp == "UNKNOWN" or mp == "Unknown" or mp == "unknown" or mp == "idk":
    mphtml = """<img src="http://www.rxrsignals.com/Graphics/Milepost_Numbers/Unknown.PNG" alt="" style="width: 134px; height: 20px;">"""
if mp == "N/A" or mp == "n/a":
    mphtml = """<img src="http://www.rxrsignals.com/Graphics/Milepost_Numbers/N_A.PNG" alt="" style="width: 48px; height: 20px;">"""

#Milepost Sorted

#Sort Accidents

print("""
--If You Don't Know How To Get Your Crossing Accidents, First, Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/
--Next, Find Your Crossing, Click On It, And Then Scroll Down To "ACC_LINK" And Click "View" 
--This Will Download A PDF With The Amount Of Accidents Included
--If You Still Cannot Find The Number Of Accidents Or You Live In Canada, You Can Type "Unknown", "idk", Or "N/A"
""")

crossing_acc = input("Total Accidents? ") #Accidents
crossing_acc = Typo_Fix(crossing_acc, 0)

if crossing_acc == "N/A" or crossing_acc == "n/a" or crossing_acc == "Unknown" or crossing_acc == "UNKNOWN" or crossing_acc == "unknown" or crossing_acc == "idk":
    crossing_acc = "Unknown"

crossingaccidentshtml = """<tr>
<td
style="vertical-align: middle; text-align: center; height: 40px;"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
alt="" src="http://www.rxrsignals.com/Graphics/Accidents/"""+crossing_acc+""".png"></font></font></strong></td>
</tr>"""

if crossing_acc =="":
    crossingaccidentshtml = ""

#Accidents Sorted

#Sort Railroads

print("""
Railroad Logo Examples: 
--BNSF.png--
--UP.png--
--CPKC.png--
--CN.png--
--CSX.png--
--NS.png--
--Amtrak.png--

--To Get More Railroad Logos, First Visit This Site:
http://www.rxrsignals.com/Graphics/Rail_Logos/ 
--Next, Use CTRL+F And Search For The Railroad Logo You Need (Use Reporting Markers Such As UP, or BNSF)
--And Then Copy And Paste Your Railroad Logo With The File Name Extension Too (Such As CN.png or Metra.png)
--For Multiple Railroads, You Can Type "BNSF.png CN.png CSX.png"
--Add A Space When Differentiating Between Different Railroads, No Comma Needed! 
""")

rr = input("Railroad(s)? ")
rr = Typo_Fix(rr, 1)

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
QZ = Typo_Fix(QZ, 1)

quietzone = ""
if QZ == "Yes" or QZ == "Y" or QZ == "yes" or QZ == "y":
    quietzone = """<img src="http://www.rxrsignals.com/Graphics/QuietZone.png" width="151" height="32" alt="">"""
if QZ == "No" or QZ == "N" or QZ == "no" or QZ == "n" or QZ == "":
    quietzone = ""

#Quiet Zone Sorted

#Defunct Xing

DF = input("Defunct X-ing? (Y/N) ")
DF = Typo_Fix(DF, 0)

defunctxing = ""
if DF == "Yes" or DF == "Y" or DF == "yes" or DF == "y":
    defunctxing = """<div style="text-align: center;"><img style="width: 450px; height: 60px;" alt="" src="http://www.rxrsignals.com/Graphics/Defunct.gif"></div><br>"""
if DF == "No" or DF == "N" or DF == "no" or DF == "n" or DF == "":
    defunctxing = ""

#Defunct Xing Sorted

print("""
--If You Don't Know How To Get Your Crossings Daily Train Count, First Visit This Site:
https://fragis.fra.dot.gov/gisfrasafety/
--Next, Find Your Crossing, Click On It, And Then Scroll Down To "INV_LINK" And Click "View"
--This Will Download A PDF With The Amount Of Daily Trains Included
--If You Still Cannot Find The Number Of Daily Trains Or You Live In Canada, You Can Type "Unknown", "idk", Or "N/A"
--If You Want To Type A Month Or Year, Type "Weekly, Monthly", Or "Yearly" In "Daily Trains?"
--For Typing In Former Trains, Type "Former" In Weekly, Monthly, Yearly, Or In "Daily Trains?"
--For A Range, Simply Type "2-4" Or "0-2"
""")

crossing_daily = input("Daily Trains? ") #Daily Trains
crossing_daily = Typo_Fix(crossing_daily, 1)
crossing_daily_crash = crossing_daily

if crossing_daily == "N/A" or crossing_daily == "n/a" or crossing_daily == "Unknown" or crossing_daily == "unknown" or crossing_daily == "idk":
    crossing_daily = "Daily/Unknown"
elif crossing_daily.find("-") != -1:
    crossing_daily = "Daily/Range/"+crossing_daily
elif crossing_daily == "Former" or crossing_daily == "former":
    crossing_daily = input("Former Daily Trains? ")
    crossing_daily = Typo_Fix(crossing_daily, 0)
    if crossing_daily.find("-") != -1:
        crossing_daily = "Daily/Former/Range/"+crossing_daily
    else:
        crossing_daily = "Daily/Former/"+crossing_daily
       
elif crossing_daily == "Weekly" or crossing_daily == "weekly" or crossing_daily == "Week" or crossing_daily == "week":
    crossing_daily = input("Weekly Trains? ")
    crossing_daily = Typo_Fix(crossing_daily, 1)
    if crossing_daily.find("-") != -1:
        crossing_daily = "Weekly/Range/"+crossing_daily
    elif crossing_daily == "Former" or crossing_daily == "former":
        crossing_daily = input("Former Weekly Trains? ")
        crossing_daily = Typo_Fix(crossing_daily, 0)
        if crossing_daily.find("-") != -1:
            crossing_daily = "Weekly/Former/Range/"+crossing_daily
        else:
            crossing_daily = "Weekly/Former/"+crossing_daily
    else:
        crossing_daily = "Weekly/"+crossing_daily

elif crossing_daily == "Monthly" or crossing_daily == "monthly" or crossing_daily == "Month" or crossing_daily == "month":
    crossing_daily = input("Monthly Trains? ")
    crossing_daily = Typo_Fix(crossing_daily, 1)
    if crossing_daily.find("-") != -1:
        crossing_daily = "Monthly/Range/"+crossing_daily
    elif crossing_daily == "Former" or crossing_daily == "former":
        crossing_daily = input("Former Monthly Trains? ")
        crossing_daily = Typo_Fix(crossing_daily, 0)
        if crossing_daily.find("-") != -1:
            crossing_daily = "Monthly/Former/Range/"+crossing_daily
        else:
            crossing_daily = "Monthly/Former/"+crossing_daily
    else:
        crossing_daily = "Monthly/"+crossing_daily
       
elif crossing_daily == "Yearly" or crossing_daily == "yearly" or crossing_daily == "Year" or crossing_daily == "year":
    crossing_daily = input("Yearly Trains? ")
    crossing_daily = Typo_Fix(crossing_daily, 1)
    if crossing_daily.find("-") != -1:
        crossing_daily = "Yearly/Range/"+crossing_daily
    elif crossing_daily == "Former" or crossing_daily == "former":
        crossing_daily = input("Former Yearly Trains? ")
        crossing_daily = Typo_Fix(crossing_daily, 0)
        if crossing_daily.find("-") != -1:
            crossing_daily = "Yearly/Former/Range/"+crossing_daily
        else:
            crossing_daily = "Yearly/Former/"+crossing_daily
    else:
        crossing_daily = "Yearly/"+crossing_daily
       
else:
    crossing_daily = "Daily/"+crossing_daily

print("""
As Of Examples:
--2020--
--2019--
--2022--
--Estimated--
""")

crossing_asof = input("As Of? ") #As Of
crossing_asof = Typo_Fix(crossing_asof, 0)
crossing_asof = crossing_asof.replace("estimated", "Estimated")

fullname = crossing_name + " ("+ crossing_city +")"

fullname = fullname.replace("/", "(Slash)")

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
    StreetViewText = Typo_Fix(StreetViewText, 0)

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
MedianCheckNumber = 0
PedestrianCheckNumber = 0


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


#Check For Median Photos

CheckForMedian = os.listdir('Median_Signals')
for f in CheckForMedian:
    MedianCheckNumber = MedianCheckNumber + 1

if MedianCheckNumber >= 5:
    prRed("""
Median Signal Photos Found Outside Subfolders In The Median_Signals Folder!""")

#Median Checked


#Check For Pedestrian Photos

CheckForPedestrian = os.listdir('Pedestrian_Signals')
for f in CheckForPedestrian:
    PedestrianCheckNumber = PedestrianCheckNumber + 1

if PedestrianCheckNumber >= 5:
    prRed("""
Pedestrian Signal Photos Found Outside Subfolders In The Pedestrian_Signals Folder!""")

#Pedestrian Checked


#Check For Header

CheckForHeader = os.listdir('Header')
for f in CheckForHeader:
    HeaderWorks = True

if HeaderWorks == False:
    prRed("""
No Header Was Found In Header Folder!""")

#Header Checked


#Check For Same Folder Name

try: 
    TestPath = "Output/"+fullname[0:len(fullname)]
    TestPath2 = os.listdir(TestPath)
    prRed("""
Same Folder Name Found In Output Folder! Program Will Crash If The Folder With The Same Name Is Not Moved!""")
except:
    CheckForSameName = True


#Folder Name Checked


#If There Are No Issues

if HeaderWorks == True and CheckForSameName == True and TrackCheckNumber <= 4 and MedianCheckNumber <= 4 and PedestrianCheckNumber <=4 and OverviewCheckNumber <= 4:
    prGreen("""
No Issues Found!""")

print("")
input("Press ENTER Twice To Begin Processing Photos")
input("Press ENTER Twice To Begin Processing Photos")

print("""
Processing Photos...
""")

fullnamehtml = "index"

#Make Folder

directory = fullname 

parent_dir = "Output/"

path = os.path.join(parent_dir, directory)

os.mkdir(path)

#Made Folder

"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

import shutil
import glob

from PIL import Image

name = 0
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
NorthMed = False
SouthMed = False
EastMed = False
WestMed = False
NorthPed = False
SouthPed = False
EastPed = False
WestPed = False
FacingImageCount = 0
StreetViewhtml = ""
NorthImagehtml = ""
SouthImagehtml = ""
EastImagehtml = ""
WestImagehtml = ""
NorthMedImagehtml = ""
SouthMedImagehtml = ""
EastMedImagehtml = ""
WestMedImagehtml = ""
NorthPedImagehtml = ""
SouthPedImagehtml = ""
EastPedImagehtml = ""
WestPedImagehtml = ""

#Sort Street View Photos

source = 'Street_View/'
destination = 'Output/'+fullname
 
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

theinput = streetviewcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
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
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter)+"""px;"></font></font></strong></a></span></td>
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+1)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter+1)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter+1)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+1)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter+1)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter+1)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+2)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter+2)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter+2)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+1)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter+1)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter+1)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+2)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter+2)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter+2)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+"SV"+""""""+str(streetviewbegincount+streetviewcounter+3)+"""<a href="""+Filenamefix2+"SV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(streetviewbegincount+streetviewcounter+3)+"""px; height: """+"""TL"""+str(streetviewbegincount+streetviewcounter+3)+"""px;" src="""+Filenamefix2+"TSV"+Filenamelist2[streetviewbegincount-1+streetviewcounter+3]+Filenamefix2+"""
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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

#Sorted Facing West Photo

#Sort Overview Photos

facingimagehtml = ""
NorthImageHeaderhtml = ""
SouthImageHeaderhtml = ""
EastImageHeaderhtml = ""
WestImageHeaderhtml = ""
FacingWidth = "100"

if FacingImageCount >= 3:
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

facingimagehtml = facingimagehtml+NorthImagehtml+SouthImagehtml+EastImagehtml+WestImagehtml+"""
</tr>
<tr>
"""+NorthImageHeaderhtml+SouthImageHeaderhtml+EastImageHeaderhtml+WestImageHeaderhtml+"""
</tr>"""

if facingimagehtml == """
</tr>
<tr>

</tr>""":
    facingimagehtml = ""

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


theinput = northernsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
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
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernsignalbegincount+northernsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[northernsignalbegincount-1+northernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernsignalbegincount+northernsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(northernsignalbegincount+northernsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernsignalbegincount-1+northernsignalcounter+3]+Filenamefix2+"""
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

#Sort Northern Median Signal Photos

source = 'Median_Signals/Northern_Median_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
northernmediansignalcount = 0
for f in allfiles:
    name = name + 1
    northernmediansignalcount = northernmediansignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    NorthMed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)


theinput = northernmediansignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

northernmediansignalhtml = ""
northernmediansignalbegincount = name-northernmediansignalcount
northernmediansignalcounter = 0

for i in range(make1column):
    northernmediansignalcounter = northernmediansignalcounter + 1
    northernmediansignalhtml = northernmediansignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The northern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    northernmediansignalcounter = northernmediansignalcounter + 1
    northernmediansignalhtml = northernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The northern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernmediansignalcounter = northernmediansignalcounter + 1

for i in range(make3columns):
    northernmediansignalcounter = northernmediansignalcounter + 1
    northernmediansignalhtml = northernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The northern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernmediansignalcounter = northernmediansignalcounter + 2

for i in range(make4columns):
    northernmediansignalcounter = northernmediansignalcounter + 1
    northernmediansignalhtml = northernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernmediansignalbegincount+northernmediansignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(northernmediansignalbegincount+northernmediansignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernmediansignalbegincount-1+northernmediansignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The northern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernmediansignalhtml = northernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernmediansignalcounter = northernmediansignalcounter + 3

#Northern Median Signal Sorted

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

theinput = southernsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
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
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernsignalbegincount+southernsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[southernsignalbegincount-1+southernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernsignalbegincount+southernsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(southernsignalbegincount+southernsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernsignalbegincount-1+southernsignalcounter+3]+Filenamefix2+"""
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

#Sort Southern Median Signal Photos

source = 'Median_Signals/Southern_Median_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
southernmediansignalcount = 0
for f in allfiles:
    name = name + 1
    southernmediansignalcount = southernmediansignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    SouthMed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = southernmediansignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

southernmediansignalhtml = ""
southernmediansignalbegincount = name-southernmediansignalcount
southernmediansignalcounter = 0

for i in range(make1column):
    southernmediansignalcounter = southernmediansignalcounter + 1
    southernmediansignalhtml = southernmediansignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The southern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    southernmediansignalcounter = southernmediansignalcounter + 1
    southernmediansignalhtml = southernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The southern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernmediansignalcounter = southernmediansignalcounter + 1

for i in range(make3columns):
    southernmediansignalcounter = southernmediansignalcounter + 1
    southernmediansignalhtml = southernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The southern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernmediansignalcounter = southernmediansignalcounter + 2

for i in range(make4columns):
    southernmediansignalcounter = southernmediansignalcounter + 1
    southernmediansignalhtml = southernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernmediansignalbegincount+southernmediansignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(southernmediansignalbegincount+southernmediansignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernmediansignalbegincount-1+southernmediansignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The southern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernmediansignalhtml = southernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernmediansignalcounter = southernmediansignalcounter + 3

#Southern Median Signal Sorted

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

theinput = easternsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
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
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternsignalbegincount+easternsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[easternsignalbegincount-1+easternsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternsignalbegincount+easternsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(easternsignalbegincount+easternsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternsignalbegincount-1+easternsignalcounter+3]+Filenamefix2+"""
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

#Sort Eastern Median Signal Photos

source = 'Median_Signals/Eastern_Median_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
easternmediansignalcount = 0
for f in allfiles:
    name = name + 1
    easternmediansignalcount = easternmediansignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    EastMed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = easternmediansignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

easternmediansignalhtml = ""
easternmediansignalbegincount = name-easternmediansignalcount
easternmediansignalcounter = 0

for i in range(make1column):
    easternmediansignalcounter = easternmediansignalcounter + 1
    easternmediansignalhtml = easternmediansignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The eastern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    easternmediansignalcounter = easternmediansignalcounter + 1
    easternmediansignalhtml = easternmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The eastern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    easternmediansignalcounter = easternmediansignalcounter + 1

for i in range(make3columns):
    easternmediansignalcounter = easternmediansignalcounter + 1
    easternmediansignalhtml = easternmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The eastern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    easternmediansignalcounter = easternmediansignalcounter + 2

for i in range(make4columns):
    easternmediansignalcounter = easternmediansignalcounter + 1
    easternmediansignalhtml = easternmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternmediansignalbegincount+easternmediansignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(easternmediansignalbegincount+easternmediansignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternmediansignalbegincount-1+easternmediansignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The eastern median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternmediansignalhtml = easternmediansignalhtml+ """
</tr>
</tbody>
</table>
"""

    easternmediansignalcounter = easternmediansignalcounter + 3

#Sorted Eastern Median Signal

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

theinput = westernsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
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
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
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
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
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
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernsignalbegincount+westernsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[westernsignalbegincount-1+westernsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernsignalbegincount+westernsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(westernsignalbegincount+westernsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernsignalbegincount-1+westernsignalcounter+3]+Filenamefix2+"""
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

#Sort Western Median Signal Photos

source = 'Median_Signals/Western_Median_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
westernmediansignalcount = 0
for f in allfiles:
    name = name + 1
    westernmediansignalcount = westernmediansignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    WestMed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = westernmediansignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

westernmediansignalhtml = ""
westernmediansignalbegincount = name-westernmediansignalcount
westernmediansignalcounter = 0

for i in range(make1column):
    westernmediansignalcounter = westernmediansignalcounter + 1
    westernmediansignalhtml = westernmediansignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The western median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    westernmediansignalcounter = westernmediansignalcounter + 1
    westernmediansignalhtml = westernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The western median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernmediansignalcounter = westernmediansignalcounter + 1

for i in range(make3columns):
    westernmediansignalcounter = westernmediansignalcounter + 1
    westernmediansignalhtml = westernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The western median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernmediansignalcounter = westernmediansignalcounter + 2

for i in range(make4columns):
    westernmediansignalcounter = westernmediansignalcounter + 1
    westernmediansignalhtml = westernmediansignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernmediansignalbegincount+westernmediansignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(westernmediansignalbegincount+westernmediansignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernmediansignalbegincount-1+westernmediansignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The western median signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernmediansignalhtml = westernmediansignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernmediansignalcounter = westernmediansignalcounter + 3

#Sorted Western Median Signal

#Sort Northern Pedestrian Signal Photos

source = 'Pedestrian_Signals/Northern_Ped_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
northernpedsignalcount = 0
for f in allfiles:
    name = name + 1
    northernpedsignalcount = northernpedsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    NorthPed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)


theinput = northernpedsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

northernpedsignalhtml = ""
northernpedsignalbegincount = name-northernpedsignalcount
northernpedsignalcounter = 0

for i in range(make1column):
    northernpedsignalcounter = northernpedsignalcounter + 1
    northernpedsignalhtml = northernpedsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The northern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    northernpedsignalcounter = northernpedsignalcounter + 1
    northernpedsignalhtml = northernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The northern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernpedsignalcounter = northernpedsignalcounter + 1

for i in range(make3columns):
    northernpedsignalcounter = northernpedsignalcounter + 1
    northernpedsignalhtml = northernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The northern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernpedsignalcounter = northernpedsignalcounter + 2

for i in range(make4columns):
    northernpedsignalcounter = northernpedsignalcounter + 1
    northernpedsignalhtml = northernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(northernpedsignalbegincount+northernpedsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(northernpedsignalbegincount+northernpedsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[northernpedsignalbegincount-1+northernpedsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The northern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        northernpedsignalhtml = northernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    northernpedsignalcounter = northernpedsignalcounter + 3

#Northern Pedestrian Signal Sorted

#Sort Southern Pedestrian Signal Photos

source = 'Pedestrian_Signals/Southern_Ped_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
southernpedsignalcount = 0
for f in allfiles:
    name = name + 1
    southernpedsignalcount = southernpedsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    SouthPed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = southernpedsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

southernpedsignalhtml = ""
southernpedsignalbegincount = name-southernpedsignalcount
southernpedsignalcounter = 0

for i in range(make1column):
    southernpedsignalcounter = southernpedsignalcounter + 1
    southernpedsignalhtml = southernpedsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The southern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    southernpedsignalcounter = southernpedsignalcounter + 1
    southernpedsignalhtml = southernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The southern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernpedsignalcounter = southernpedsignalcounter + 1

for i in range(make3columns):
    southernpedsignalcounter = southernpedsignalcounter + 1
    southernpedsignalhtml = southernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The southern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernpedsignalcounter = southernpedsignalcounter + 2

for i in range(make4columns):
    southernpedsignalcounter = southernpedsignalcounter + 1
    southernpedsignalhtml = southernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(southernpedsignalbegincount+southernpedsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(southernpedsignalbegincount+southernpedsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[southernpedsignalbegincount-1+southernpedsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The southern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        southernpedsignalhtml = southernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    southernpedsignalcounter = southernpedsignalcounter + 3

#Southern Pedestrian Signal Sorted

#Sort Eastern Pedestrian Signal Photos

source = 'Pedestrian_Signals/Eastern_Ped_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
easternpedsignalcount = 0
for f in allfiles:
    name = name + 1
    easternpedsignalcount = easternpedsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    EastPed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = easternpedsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

easternpedsignalhtml = ""
easternpedsignalbegincount = name-easternpedsignalcount
easternpedsignalcounter = 0

for i in range(make1column):
    easternpedsignalcounter = easternpedsignalcounter + 1
    easternpedsignalhtml = easternpedsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The eastern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    easternpedsignalcounter = easternpedsignalcounter + 1
    easternpedsignalhtml = easternpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The eastern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    easternpedsignalcounter = easternpedsignalcounter + 1

for i in range(make3columns):
    easternpedsignalcounter = easternpedsignalcounter + 1
    easternpedsignalhtml = easternpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The eastern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    easternpedsignalcounter = easternpedsignalcounter + 2

for i in range(make4columns):
    easternpedsignalcounter = easternpedsignalcounter + 1
    easternpedsignalhtml = easternpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(easternpedsignalbegincount+easternpedsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(easternpedsignalbegincount+easternpedsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[easternpedsignalbegincount-1+easternpedsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The eastern pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        easternpedsignalhtml = easternpedsignalhtml+ """
</tr>
</tbody>
</table>
"""

    easternpedsignalcounter = easternpedsignalcounter + 3

#Sorted Eastern Pedestrian Signal

#Sort Western Pedestrian Signal Photos

source = 'Pedestrian_Signals/Western_Ped_Signal/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
westernpedsignalcount = 0
for f in allfiles:
    name = name + 1
    westernpedsignalcount = westernpedsignalcount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    WestPed = True
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = westernpedsignalcount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

westernpedsignalhtml = ""
westernpedsignalbegincount = name-westernpedsignalcount
westernpedsignalcounter = 0

for i in range(make1column):
    westernpedsignalcounter = westernpedsignalcounter + 1
    westernpedsignalhtml = westernpedsignalhtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The western pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    westernpedsignalcounter = westernpedsignalcounter + 1
    westernpedsignalhtml = westernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The western pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernpedsignalcounter = westernpedsignalcounter + 1

for i in range(make3columns):
    westernpedsignalcounter = westernpedsignalcounter + 1
    westernpedsignalhtml = westernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The western pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernpedsignalcounter = westernpedsignalcounter + 2

for i in range(make4columns):
    westernpedsignalcounter = westernpedsignalcounter + 1
    westernpedsignalhtml = westernpedsignalhtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter+1)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+1)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter+2)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+2)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(westernpedsignalbegincount+westernpedsignalcounter+3)+"""<a href="""+Filenamefix2+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+3)+"""px; height: """+"""TL"""+str(westernpedsignalbegincount+westernpedsignalcounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[westernpedsignalbegincount-1+westernpedsignalcounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The western pedestrian signal.</td>
</tr>
</tbody>
</table>
"""
    else:
        westernpedsignalhtml = westernpedsignalhtml+ """
</tr>
</tbody>
</table>
"""
    westernpedsignalcounter = westernpedsignalcounter + 3

#Sorted Western Pedestrian Signal

"""Sort Relay Bungalow And Grade Photo ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

TrackRelayNumber = 0
RelayBungalow = False
Grade = False
RelayBungalowimagecount = 0
Gradeimagecount = 0
RelayBungalowhtml = ""
Gradehtml = ""

source = 'Relay_Bungalow/'
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
    RelayBungalow = True
    RelayBungalowimagecount = RelayBungalowimagecount + 1
    RelayBungalowhtml = RelayBungalowhtml+"""
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)


#Sorted Relay Bungalow Photo

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
    Gradeimagecount = Gradeimagecount + 1
    Gradehtml = Gradehtml+"""
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

#Sorted Facing South Track Photo

#Sort Relay Bungalow and Grade Photos

relayandgradehtml = ""
relayheaderhtml = ""
gradeheaderhtml = ""
FacingWidth = "100"

if RelayBungalowimagecount+Gradeimagecount >= 3:
    FacingWidth = "25"
if RelayBungalowimagecount+Gradeimagecount == 3:
    FacingWidth = "33"
if RelayBungalowimagecount+Gradeimagecount == 2:
    FacingWidth = "50"
if RelayBungalowimagecount+Gradeimagecount == 1:
    FacingWidth = "100"

if RelayBungalow == True:
    TrackRelayNumber = TrackRelayNumber + 1
    relayheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>"""
if RelayBungalowimagecount > 1:
    relayheaderhtml = relayheaderhtml+"""
<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>"""
if RelayBungalowimagecount > 2:
    relayheaderhtml = relayheaderhtml+"""
<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>"""
if RelayBungalowimagecount > 3:
    relayheaderhtml = relayheaderhtml+"""
<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>"""
if Grade == True:
    TrackRelayNumber = TrackRelayNumber + 1
    gradeheaderhtml = """<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""
if Gradeimagecount > 1:
    gradeheaderhtml = gradeheaderhtml+"""
<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""
if Gradeimagecount > 2:
    gradeheaderhtml = gradeheaderhtml+"""
<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""
if Gradeimagecount > 3:
    gradeheaderhtml = gradeheaderhtml+"""
<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""

relayandgradehtml = relayandgradehtml+RelayBungalowhtml+Gradehtml+"""
</tr>
<tr>
"""+relayheaderhtml+gradeheaderhtml+"""
</tr>"""

if relayandgradehtml == """
</tr>
<tr>

</tr>""":
    relayandgradehtml = ""

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)


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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

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
<td style="text-align: center; width: 25%; vertical-align: bottom;"><span style="font-family: Arial; font-weight: bold;">"""+str(name)+"""</span><a href="""+Filenamefix2+str(Filenamelist[name-1])+Filenamefix2+"""><img style="border: 0px solid; width: """+"""TW"""+str(name+Sname)+"""px; height: """+"""TL"""+str(name+Sname)+"""px;" alt="" src="""+Filenamefix2+"T"+Filenamelist[name-1]+Filenamefix2+"""></a><br>
</td>
"""
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

#Sorted Facing West Track Photo

#Sort Action Shots ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

source = 'Action_Shots/'
destination = 'Output/'+fullname
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
ActionShotscount = 0
for f in allfiles:
    name = name + 1
    ActionShotscount = ActionShotscount + 1
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files
    Filenamelist.append(str(name)+filenameext)
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, str(name)+filenameext)
    dst_pathT = os.path.join(destination, "T"+str(name)+filenameext)
    shutil.copyfile(src_path, dst_pathT)
    os.rename(src_path, dst_path)

theinput = ActionShotscount #Number of photos
if theinput != "":
    theinput = int(theinput)
elif theinput =="":
    theinput = 0

Sorted_Number = Sort_Number(int(theinput))
make4columns = Sorted_Number[0]
make3columns = Sorted_Number[1]
make2columns = Sorted_Number[2]
make1column = Sorted_Number[3]
#Photos Sorted

ActionShotshtml = ""
ActionShotsbegincount = name-ActionShotscount
ActionShotscounter = 0

for i in range(make1column):
    ActionShotscounter = ActionShotscounter + 1
    ActionShotshtml = ActionShotshtml+ """
<table width="100%" border="1">
  <tbody>
    <tr>
      <td width="25%" align="center" valign="bottom"><span style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px;"></font></font></strong></a></span></td>
"""
    if i == make1column-1 and make2columns == 0 and make3columns == 0 and make4columns == 0:
        ActionShotshtml = ActionShotshtml+ """
</tr>
<tr>
<td colspan="1" align="center" valign="middle">The crossing in action!</td>
</tr>
</tbody>
</table>
"""
    else:
        ActionShotshtml = ActionShotshtml+ """
</tr>
</tbody>
</table>
"""

for i in range(make2columns):
    ActionShotscounter = ActionShotscounter + 1
    ActionShotshtml = ActionShotshtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img alt="" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+""" style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px;"></font></font></strong></a></span></td>
<td style="text-align: center;" align="center" valign="bottom" width="50%"><span style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter+1)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname+1)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make2columns-1 and make3columns == 0 and make4columns == 0:
        ActionShotshtml = ActionShotshtml+ """
</tr>
<tr>
<td colspan="2" align="center" valign="middle">The crossing in action!</td>
</tr>
</tbody>
</table>
"""
    else:
        ActionShotshtml = ActionShotshtml+ """
</tr>
</tbody>
</table>
"""
    ActionShotscounter = ActionShotscounter + 1

for i in range(make3columns):
    ActionShotscounter = ActionShotscounter + 1
    ActionShotshtml = ActionShotshtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter+1)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+1]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname+1)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+1]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
<td align="center" valign="bottom" width="33%"><span style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter+2)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+2]+Filenamefix2+"""><strong><font face="Arial,Helvetica,Monaco"><font color="WHITE"><img style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname+2)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+2]+Filenamefix2+""" alt=""></font></font></strong></a></span></td>
"""
    if i == make3columns-1 and make4columns == 0:
        ActionShotshtml = ActionShotshtml+ """
</tr>
<tr>
<td colspan="3" align="center" valign="middle">The crossing in action!</td>
</tr>
</tbody>
</table>
"""
    else:
        ActionShotshtml = ActionShotshtml+ """
</tr>
</tbody>
</table>
"""
    ActionShotscounter = ActionShotscounter + 2

for i in range(make4columns):
    ActionShotscounter = ActionShotscounter + 1
    ActionShotshtml = ActionShotshtml+ """
<table border="1" width="100%">
<tbody>
<tr>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter+1)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+1]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname+1)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname+1)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+1]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter+2)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+2]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname+2)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname+2)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+2]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
<td width="25%" align="center" valign="bottom" style="text-align: center"><span
style="font-family: Arial; font-weight: bold;">"""+str(ActionShotsbegincount+ActionShotscounter+3)+"""<a href="""+Filenamefix2+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+3]+Filenamefix2+"""><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
style="border: 0px solid; width: """+"""TW"""+str(ActionShotsbegincount+ActionShotscounter+Sname+3)+"""px; height: """+"""TL"""+str(ActionShotsbegincount+ActionShotscounter+Sname+3)+"""px;" src="""+Filenamefix2+"T"+Filenamelist[ActionShotsbegincount-1+ActionShotscounter+3]+Filenamefix2+"""
alt=""></font></font></strong></a></span></td>
"""
    if i == make4columns-1:
        ActionShotshtml = ActionShotshtml+ """
</tr>
<tr>
<td colspan="4" align="center" valign="middle">The crossing in action!</td>
</tr>
</tbody>
</table>
"""
    else:
        ActionShotshtml = ActionShotshtml+ """
</tr>
</tbody>
</table>
"""
    ActionShotscounter = ActionShotscounter + 3

#Sorted Action Shots ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sort Header Photo

source = 'Header'
destination = 'Output/'+fullname

allfiles = os.listdir(source)

HeaderFilename = ""
 
# iterate on all files to move them to destination folder
for f in allfiles:
    filename = f
    filenamelength = len(filename)#Get Length
    filenameext = str(filename[filenamelength-4:filenamelength])#Get Extension
    if filenameext[0:1] != ".": #Fixes for JEPG
        filenameext = "."+filenameext #Fixed JEPG files

    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, "Header"+filenameext)
    os.rename(src_path, dst_path)
    HeaderFilename = "Header"+filenameext
if HeaderFilename == "":
    HeaderFilename = "Header.png"

#Sorted Header Photo

allTfiles = os.listdir(destination)

size_list = []

ImageProcessCounter = 0
ImageProcessLimit = 0

#For keeping exif data:
from PIL.ExifTags import TAGS, Base

PILLOW_TAGS = [
    306,
    272,
]
from types import NoneType
try:
    for f in allTfiles:
        ImageProcessLimit = ImageProcessLimit+1
    for f in allTfiles:
        filename = f
        ImageProcessCounter = ImageProcessCounter+1
        print("("+str(ImageProcessCounter)+"/"+str(ImageProcessLimit)+") "+filename)
        image = Image.open('Output/'+fullname+"/"+filename)
        imagetest = image
        
        info = image.getexif()
        VALUES = [
            info.get(306),
            info.get(272),
        ]
        img_exif = image.getexif()
        for tag, value in zip(PILLOW_TAGS, VALUES):
            img_exif[tag] = value

        image.thumbnail((1600, 1600))
        
        if info.get(306) == None and info.get(272) == None:
            image.save('Output/'+fullname+"/"+filename)
        else:
            try:
                image.save('Output/'+fullname+"/"+filename, exif=img_exif)
            except:
                print('\033[31mUnable To Save Exif Data To Image!\033[0m')
                image.save('Output/'+fullname+"/"+filename)

        if f[0] == "T": 
          image = Image.open('Output/'+fullname+"/"+filename)
          if image.size[0] > image.size[1]:
              imagetest.thumbnail((image.size[0], 121))
              if ((imagetest.size[0])) == 215:
                  image.thumbnail([214, 214])
              else:
                  image.thumbnail((image.size[0], 120))
          else:
              imagetest.thumbnail((121, image.size[1]))
              if ((imagetest.size[1])) == 215:
                  image.thumbnail([214, 214])
              else:
                  image.thumbnail((120, image.size[1]))

          image.save('Output/'+fullname+"/"+filename)
          size_list.append([filename,image.size[0],image.size[1]])
except Exception as error:
    print('\033[31m\nProgram Crashed! Photo Processing Didn\'t Work Due To:\n\033[0m')
    print(error)
    input("\nRuh Roh! Press ENTER To View Previous Input Info")
    print("\nCrossing Street Name: "+str(crossing_name))
    print("\nCrossing City: "+str(crossing_city))
    print("\nPage Creation Date: "+str(crossingdate))
    print("\nDOT Number(s): "+str(dot))
    print("\nMilepost: "+str(mp))
    print("\nTotal Accidents: "+str(crossing_acc))
    print("\nRailroad(s): "+str(rr))
    print("\nQuiet Zone: "+str(QZ))
    print("\nDefunct X-ing: "+str(DF))
    print("\nDaily Trains: "+str(crossing_daily_crash))
    print("\nAs Of: "+str(crossing_asof))
    if StreetViewCheck == True: 
        print("\nStreet View Photo Comments: : "+str(StreetViewText))
    input("\nPress ENTER Twice To Close The Program D:")
    input("Press ENTER Twice To Close The Program D:")
    quit()

add=0
for i in range(len(size_list)):
    if size_list[i][0][0:2] == "TS":
       size_list[i][0] = size_list[i][0][3:]
       add = add+1
for i in range(len(size_list)):
    try:
        if size_list[i][0][2] == ".":
            size_list[i][0] = int(size_list[i][0][1:2])+add
        elif size_list[i][0][4] == ".":
            size_list[i][0] = int(size_list[i][0][1:4])+add
        else:
            size_list[i][0] = int(size_list[i][0][1:3])+add
    except:
        size_list[i][0] = int(size_list[i][0][0:1])

size_list = sorted(size_list, key=lambda x: x[0])

if name+Sname != 1:
    prGreen("""
Processed """+str(name+Sname)+""" Photos!""")
if name+Sname == 0:
    prRed("""
0 Photos Were Detected, Make Sure You Put Your Photos In The Correct Folders!""")
if name+Sname == 1:
    prGreen("""
Processed 1 Photo!""")

#Sort Track Overview Photos

trackfacinghtml = ""
TNorthImageHeaderhtml = ""
TSouthImageHeaderhtml = ""
TEastImageHeaderhtml = ""
TWestImageHeaderhtml = ""
FacingWidth = "100"

if TFacingImageCount >= 3:
    TFacingWidth = "25"
if TFacingImageCount == 3:
    TFacingWidth = "33"
if TFacingImageCount == 2:
    TFacingWidth = "50"
if TFacingImageCount == 1:
    TFacingWidth = "100"

if TFacingNorth == True:
    print("""
--Next, You Will Have To Find The Next Crossing And It's Street Name North Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--16th St. in Another Town.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TNorthStreet = input("Track view facing north towards: ")
    TNorthStreet = TNorthStreet.replace(" in ", "</a> in ", 1)
    if TNorthStreet != "":
        if TNorthStreet.find(" in ") == -1:
            TNorthStreet = TNorthStreet+"</a>"
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

--Waldron St. (Different Town And Different Alphabet Category)--
--../../../A-K/Different_Town/Waldron--
""")
        TNorthStreetLink = input("Crossing Link? ")
        TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north towards <a href="""+Filenamefix2+TNorthStreetLink+Filenamefix2+""">"""+TNorthStreet+"""</td>"""

    elif TNorthStreet == "":
        TNorthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing north.</td>"""

if TFacingSouth == True:
    print("""
--Next, You Will Have To Find The Next Crossing And It's Street Name South Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--16th St. in Another Town.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TSouthStreet = input("Track view facing south towards: ")
    TSouthStreet = TSouthStreet.replace(" in ", "</a> in ", 1)
    if TSouthStreet != "":
        if TSouthStreet.find(" in ") == -1:
            TSouthStreet = TSouthStreet+"</a>"
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

--Waldron St. (Different Town And Different Alphabet Category)--
--../../../A-K/Different_Town/Waldron--
""")
        TSouthStreetLink = input("Crossing Link? ")
        TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south towards <a href="""+Filenamefix2+TSouthStreetLink+Filenamefix2+""">"""+TSouthStreet+"""</td>"""

    elif TSouthStreet == "":
        TSouthImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing south.</td>"""

if TFacingEast == True:
    print("""
--Next, You Will Have To Find The Next Crossing And It's Street Name East Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--16th St. in Another Town.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TEastStreet = input("Track view facing east towards: ")
    TEastStreet = TEastStreet.replace(" in ", "</a> in ", 1)
    if TEastStreet != "":
        if TEastStreet.find(" in ") == -1:
            TEastStreet = TEastStreet+"</a>"
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

--Waldron St. (Different Town And Different Alphabet Category)--
--../../../A-K/Different_Town/Waldron--
""")
        TEastStreetLink = input("Crossing Link? ")
        TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east towards <a href="""+Filenamefix2+TEastStreetLink+Filenamefix2+""">"""+TEastStreet+"""</td>"""

    elif TEastStreet == "":
        TEastImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing east.</td>"""

if TFacingWest == True:
    print("""
--Next, You Will Have To Find The Next Crossing And It's Street Name West Of This Crossing
--You Can Use Google Maps Or Any Accurate Mapping Software To Do This

Street Name Examples: 
--W 2nd St.--
--5th Ave.--
--16th St. in Another Town.--
--US 64.--
--Depot St. #2.--

--Don't Forget To Add A "." At The End!

--If You Cannot Find The Crossing Street Name Or Make The Crossing Link, Skip This By Pressing ENTER
""")
    TWestStreet = input("Track view facing west towards: ")
    TWestStreet = TWestStreet.replace(" in ", "</a> in ", 1)
    if TWestStreet != "":
        if TWestStreet.find(" in ") == -1:
            TWestStreet = TWestStreet+"</a>"
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

--Waldron St. (Different Town And Different Alphabet Category)--
--../../../A-K/Different_Town/Waldron--
""")
        TWestStreetLink = input("Crossing Link? ")
        TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west towards <a href="""+Filenamefix2+TWestStreetLink+Filenamefix2+""">"""+TWestStreet+"""</td>"""

    elif TWestStreet == "":
        TWestImageHeaderhtml = """<td style="text-align: center; width: """+TFacingWidth+"""%;">Track view facing west.</td>"""

#Can Relay And Track View Be Merged?
TrackRelayNumber = TrackRelayNumber + TFacingImageCount
if TrackRelayNumber <= 4 and (TNorthImageHeaderhtml != "" or TSouthImageHeaderhtml != "" or TEastImageHeaderhtml != "" or TWestImageHeaderhtml != "") and RelayBungalowimagecount+Gradeimagecount+TFacingImageCount <= 4 and (RelayBungalow == True or Grade == True):
    if RelayBungalowimagecount+Gradeimagecount+TFacingImageCount >= 4:
        TFacingWidth = "25"
        FacingWidth = "25"
    if RelayBungalowimagecount+Gradeimagecount+TFacingImageCount <= 3:
        TFacingWidth = "33"
        FacingWidth = "33"
    if RelayBungalowimagecount+Gradeimagecount+TFacingImageCount <= 2:
        TFacingWidth = "50"
        FacingWidth = "50"
    if RelayBungalowimagecount+Gradeimagecount+TFacingImageCount <= 1:
        TFacingWidth = "100"
        FacingWidth = "100"

    relayheaderhtml = ""
    for i in range(RelayBungalowimagecount):
        relayheaderhtml = relayheaderhtml+"""<td style="text-align: center; width: """+FacingWidth+"""%;">The relay bungalow.</td>""" 
    gradeheaderhtml = ""
    for i in range(Gradeimagecount):
        gradeheaderhtml = gradeheaderhtml+"""<td style="text-align: center; width: """+FacingWidth+"""%;">The grade.</td>"""

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

    trackfacinghtml = trackfacinghtml+RelayBungalowhtml+Gradehtml+TFacingNorthhtml+TFacingSouthhtml+TFacingEasthtml+TFacingWesthtml+"""
</tr>
<tr>
"""+relayheaderhtml+gradeheaderhtml+TNorthImageHeaderhtml+TSouthImageHeaderhtml+TEastImageHeaderhtml+TWestImageHeaderhtml+"""
</tr>"""
    Gradehtml = ""
    RelayBungalowhtml = ""
    relayandgradehtml = ""

else:
    trackfacinghtml = trackfacinghtml+TFacingNorthhtml+TFacingSouthhtml+TFacingEasthtml+TFacingWesthtml+"""
</tr>
<tr>
"""+TNorthImageHeaderhtml+TSouthImageHeaderhtml+TEastImageHeaderhtml+TWestImageHeaderhtml+"""
</tr>"""

if trackfacinghtml == """
</tr>
<tr>

</tr>""":
    trackfacinghtml = ""

if TFacingSouth == True or TFacingNorth == True or TFacingEast == True or TFacingWest == True:
    trackfacinghtml = """<table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
<tbody>"""+trackfacinghtml+"""</tbody>
</table>"""

"""Sorted Track Overview Photos ---------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

#Photo Dates And Credit

print("""
--When Were These Photos Taken?

Date Examples: 
--Feburary 20, 2023--
--April 19, 2025--
--October 3, 2021--

--Don't Forget To NOT (I REPEAT DO NOT) Add A "." or "," At The End!""")
PhotoDates = input("""
Pictures 1-"""+str(name)+""" were taken on """)
PhotoDates = Typo_Fix(PhotoDates, 2)

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
--No "." or "," Needed.
""")
Username = input("""Pictures 1-"""+str(name)+""" were taken on """+PhotoDates+""", by """)
Username = Typo_Fix(Username, 2)

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
--No "." or "," Needed Still.
""")
Creator = input("Page Created By? ")
Creator = Typo_Fix(Creator, 2)

pagecreatedhtml = """Page created by """+Creator+""" (using HopenRXRTools """+VERSION+""")."""
if Creator == "":
    pagecreatedhtml ="""Page created using HopenRXRTools """+VERSION+"""."""

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
Subdivision = Typo_Fix(Subdivision, 2)

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
        if VideoInput.find("//youtu.be/") != -1:
            VideoHTMLInput = VideoInput[VideoInput.find("/youtu.be/")+10:VideoInput.find("/youtu.be/")+21]
        elif VideoInput.find("youtube.com/watch?v=") != -1:
            VideoHTMLInput = VideoInput[VideoInput.find("youtube.com/watch?v=")+20:VideoInput.find("youtube.com/watch?v=")+31]
        else:
            Videoi = Videoi - 1
            print('\033[31mInvalid Link! Try Again!\033[0m')
            VideoHTMLInput = "Invalid"
        if VideoHTMLInput != "Invalid":
            VideoHTML = VideoHTML+"""</div><div style="text-align: center;"><iframe src="https://www.youtube.com/embed/"""+VideoHTMLInput+Filenamefix2+""" allowfullscreen="" frameborder="0" height="540" width="960">&amp;lt;br&amp;gt;
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
   Base:       | MI 4" Single Sided
Light Brackets:| Safetran
  Lights:      | 4 - 8"x20" Safetran incandescents
Gate Lights:   | 3 - RECO 4" LEDs
Gate Mechanism:| Safetran Late 1970s
Gate Striping: | Vertical Striping
-----------------------------------------

-----------------------------------------
   Bell:       | GS Type 2 E-Bell
   Base:       | Safetran 5" Single Sided
Light Brackets:| Safetran
  Lights:      | 4 - 12"x20" Safetran w/ Dialight Ball LEDs
 Gate Lights:  | 3 - RECO 4" LEDs
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

north_bell_html = ""
north_cant_html = ""
north_base_html = ""
north_bracket_html = ""
north_lights_html = ""
north_gate_lights_html = ""
north_gate_html = ""
north_gate_str_html = ""

north_med_bell_html = ""
north_med_cant_html = ""
north_med_base_html = ""
north_med_bracket_html = ""
north_med_lights_html = ""
north_med_gate_lights_html = ""
north_med_gate_html = ""
north_med_gate_str_html = ""

north_bell = ""
north_base = ""
north_cant = ""
north_bracket = ""
north_lights = ""
north_gate_lights = ""
north_gate = ""
north_gate_str = ""

north_med_bell = ""
north_med_base = ""
north_med_cant = ""
north_med_bracket = ""
north_med_lights = ""
north_med_gate_lights = ""
north_med_gate = ""
north_med_gate_str = ""

south_bell_html = ""
south_cant_html = ""
south_base_html = ""
south_bracket_html = ""
south_lights_html = ""
south_gate_lights_html = ""
south_gate_html = ""
south_gate_str_html = ""

south_med_bell_html = ""
south_med_cant_html = ""
south_med_base_html = ""
south_med_bracket_html = ""
south_med_lights_html = ""
south_med_gate_lights_html = ""
south_med_gate_html = ""
south_med_gate_str_html = ""

south_bell = ""
south_base = ""
south_cant = ""
south_bracket = ""
south_lights = ""
south_gate_lights = ""
south_gate = ""
south_gate_str = ""

south_med_bell = ""
south_med_base = ""
south_med_cant = ""
south_med_bracket = ""
south_med_lights = ""
south_med_gate_lights = ""
south_med_gate = ""
south_med_gate_str = ""

east_bell_html = ""
east_cant_html = ""
east_base_html = ""
east_bracket_html = ""
east_lights_html = ""
east_gate_lights_html = ""
east_gate_html = ""
east_gate_str_html = ""

east_med_bell_html = ""
east_med_cant_html = ""
east_med_base_html = ""
east_med_bracket_html = ""
east_med_lights_html = ""
east_med_gate_lights_html = ""
east_med_gate_html = ""
east_med_gate_str_html = ""

east_bell = ""
east_base = ""
east_cant = ""
east_bracket = ""
east_lights = ""
east_gate_lights = ""
east_gate = ""
east_gate_str = ""

east_med_bell = ""
east_med_base = ""
east_med_cant = ""
east_med_bracket = ""
east_med_lights = ""
east_med_gate_lights = ""
east_med_gate = ""
east_med_gate_str = ""

west_bell_html = ""
west_cant_html = ""
west_base_html = ""
west_bracket_html = ""
west_lights_html = ""
west_gate_lights_html = ""
west_gate_html = ""
west_gate_str_html = ""

west_med_bell_html = ""
west_med_cant_html = ""
west_med_base_html = ""
west_med_bracket_html = ""
west_med_lights_html = ""
west_med_gate_lights_html = ""
west_med_gate_html = ""
west_med_gate_str_html = ""

west_bell = ""
west_base = ""
west_cant = ""
west_bracket = ""
west_lights = ""
west_gate_lights = ""
west_gate = ""
west_gate_str = ""

west_med_bell = ""
west_med_base = ""
west_med_cant = ""
west_med_bracket = ""
west_med_lights = ""
west_med_gate_lights = ""
west_med_gate = ""
west_med_gate_str = ""

NorthTableCheck = False
NorthMedTableCheck = False
SouthTableCheck = False
SouthMedTableCheck = False
EastTableCheck = False
EastMedTableCheck = False
WestTableCheck = False
WestMedTableCheck = False

if North == True:
    NorthTableCheck = True
    print("--Northern Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Northern Signal</em></strong></td>"""
    north_bell = input("Northern Bell? ")
    north_bell = Typo_Fix(north_bell, 1)
    north_bell_html = """<td style="text-align: center">"""+north_bell+"""</td>"""
    north_cant = input("Northern Cantilever? ")
    north_cant = Typo_Fix(north_cant, 1)
    north_cant_html = """<td style="text-align: center">"""+north_cant+"""</td>"""
    north_base = input("Northern Base? ")
    north_base = Typo_Fix(north_base, 1)
    north_base_html = """<td style="text-align: center">"""+north_base+"""</td>"""
    north_bracket = input("Northern Light Brackets? ")
    north_bracket = Typo_Fix(north_bracket, 1)
    north_bracket_html = """<td style="text-align: center">"""+north_bracket+"""</td>"""
    north_lights = input("Northern Lights? ")
    north_lights = Typo_Fix(north_lights, 1)
    north_lights_html = """<td style="text-align: center">"""+north_lights+"""</td>"""
    north_gate_lights = input("Northern Gate Lights? ")
    north_gate_lights = Typo_Fix(north_gate_lights, 1)
    north_gate_lights_html = """<td style="text-align: center">"""+north_gate_lights+"""</td>"""
    north_gate = input("Northern Gate Mechanism? ")
    north_gate = Typo_Fix(north_gate, 1)
    north_gate_html = """<td style="text-align: center">"""+north_gate+"""</td>"""
    north_gate_str = input("Northern Gate Striping? ")
    north_gate_str = Typo_Fix(north_gate_str, 1)
    north_gate_str_html = """<td style="text-align: center">"""+north_gate_str+"""</td>"""
    if north_bell == "" and north_cant == "" and north_base == "" and north_bracket == "" and north_lights == "" and north_gate_lights == "" and north_gate == "" and north_gate_str == "":
        NorthTableCheck = False
if NorthMed == True:
    NorthMedTableCheck = True
    print("--Northern Median Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Northern Median Signal</em></strong></td>"""
    north_med_bell = input("Northern Median Bell? ")
    north_med_bell = Typo_Fix(north_med_bell, 1)
    north_med_bell_html = """<td style="text-align: center">"""+north_med_bell+"""</td>"""
    north_med_cant = input("Northern Median Cantilever? ")
    north_med_cant = Typo_Fix(north_med_cant, 1)
    north_med_cant_html = """<td style="text-align: center">"""+north_med_cant+"""</td>"""
    north_med_base = input("Northern Median Base? ")
    north_med_base = Typo_Fix(north_med_base, 1)
    north_med_base_html = """<td style="text-align: center">"""+north_med_base+"""</td>"""
    north_med_bracket = input("Northern Median Light Brackets? ")
    north_med_bracket = Typo_Fix(north_med_bracket, 1)
    north_med_bracket_html = """<td style="text-align: center">"""+north_med_bracket+"""</td>"""
    north_med_lights = input("Northern Median Lights? ")
    north_med_lights = Typo_Fix(north_med_lights, 1)
    north_med_lights_html = """<td style="text-align: center">"""+north_med_lights+"""</td>"""
    north_med_gate_lights = input("Northern Median Gate Lights? ")
    north_med_gate_lights = Typo_Fix(north_med_gate_lights, 1)
    north_med_gate_lights_html = """<td style="text-align: center">"""+north_med_gate_lights+"""</td>"""
    north_med_gate = input("Northern Median Gate Mechanism? ")
    north_med_gate = Typo_Fix(north_med_gate, 1)
    north_med_gate_html = """<td style="text-align: center">"""+north_med_gate+"""</td>"""
    north_med_gate_str = input("Northern Median Gate Striping? ")
    north_med_gate_str = Typo_Fix(north_med_gate_str, 1)
    north_med_gate_str_html = """<td style="text-align: center">"""+north_med_gate_str+"""</td>"""
    if north_med_bell == "" and north_med_cant == "" and north_med_base == "" and north_med_bracket == "" and north_med_lights == "" and north_med_gate_lights == "" and north_med_gate == "" and north_med_gate_str == "":
        NorthMedTableCheck = False
if South == True:
    SouthTableCheck = True
    print("--Southern Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Southern Signal</em></strong></td>"""
    south_bell = input("Southern Bell? ")
    south_bell = Typo_Fix(south_bell, 1)
    south_bell_html = """<td style="text-align: center">"""+south_bell+"""</td>"""
    south_cant = input("Southern Cantilever? ")
    south_cant = Typo_Fix(south_cant, 1)
    south_cant_html = """<td style="text-align: center">"""+south_cant+"""</td>"""
    south_base = input("Southern Base? ")
    south_base = Typo_Fix(south_base, 1)
    south_base_html = """<td style="text-align: center">"""+south_base+"""</td>"""
    south_bracket = input("Southern Light Brackets? ")
    south_bracket = Typo_Fix(south_bracket, 1)
    south_bracket_html = """<td style="text-align: center">"""+south_bracket+"""</td>"""
    south_lights = input("Southern Lights? ")
    south_lights = Typo_Fix(south_lights, 1)
    south_lights_html = """<td style="text-align: center">"""+south_lights+"""</td>"""
    south_gate_lights = input("Southern Gate Lights? ")
    south_gate_lights = Typo_Fix(south_gate_lights, 1)
    south_gate_lights_html = """<td style="text-align: center">"""+south_gate_lights+"""</td>"""
    south_gate = input("Southern Gate Mechanism? ")
    south_gate = Typo_Fix(south_gate, 1)
    south_gate_html = """<td style="text-align: center">"""+south_gate+"""</td>"""
    south_gate_str = input("Southern Gate Striping? ")
    south_gate_str = Typo_Fix(south_gate_str, 1)
    south_gate_str_html = """<td style="text-align: center">"""+south_gate_str+"""</td>"""
    if south_bell == "" and south_cant == "" and south_base == "" and south_bracket == "" and south_lights == "" and south_gate_lights == "" and south_gate == "" and south_gate_str == "":
        SouthTableCheck = False
if SouthMed == True:
    SouthMedTableCheck = True
    print("--Southern Median Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Southern Median Signal</em></strong></td>"""
    south_med_bell = input("Southern Median Bell? ")
    south_med_bell = Typo_Fix(south_med_bell, 1)
    south_med_bell_html = """<td style="text-align: center">"""+south_med_bell+"""</td>"""
    south_med_cant = input("Southern Median Cantilever? ")
    south_med_cant = Typo_Fix(south_med_cant, 1)
    south_med_cant_html = """<td style="text-align: center">"""+south_med_cant+"""</td>"""
    south_med_base = input("Southern Median Base? ")
    south_med_base = Typo_Fix(south_med_base, 1)
    south_med_base_html = """<td style="text-align: center">"""+south_med_base+"""</td>"""
    south_med_bracket = input("Southern Median Light Brackets? ")
    south_med_bracket = Typo_Fix(south_med_bracket, 1)
    south_med_bracket_html = """<td style="text-align: center">"""+south_med_bracket+"""</td>"""
    south_med_lights = input("Southern Median Lights? ")
    south_med_lights = Typo_Fix(south_med_lights, 1)
    south_med_lights_html = """<td style="text-align: center">"""+south_med_lights+"""</td>"""
    south_med_gate_lights = input("Southern Median Gate Lights? ")
    south_med_gate_lights = Typo_Fix(south_med_gate_lights, 1)
    south_med_gate_lights_html = """<td style="text-align: center">"""+south_med_gate_lights+"""</td>"""
    south_med_gate = input("Southern Median Gate Mechanism? ")
    south_med_gate = Typo_Fix(south_med_gate, 1)
    south_med_gate_html = """<td style="text-align: center">"""+south_med_gate+"""</td>"""
    south_med_gate_str = input("Southern Median Gate Striping? ")
    south_med_gate_str = Typo_Fix(south_med_gate_str, 1)
    south_med_gate_str_html = """<td style="text-align: center">"""+south_med_gate_str+"""</td>"""
    if south_med_bell == "" and south_med_cant == "" and south_med_base == "" and south_med_bracket == "" and south_med_lights == "" and south_med_gate_lights == "" and south_med_gate == "" and south_med_gate_str == "":
        SouthMedTableCheck = False
if East == True:
    EastTableCheck = True
    print("--Eastern Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Eastern Signal</em></strong></td>"""
    east_bell = input("Eastern Bell? ")
    east_bell = Typo_Fix(east_bell, 1)
    east_bell_html = """<td style="text-align: center">"""+east_bell+"""</td>"""
    east_cant = input("Eastern Cantilever? ")
    east_cant = Typo_Fix(east_cant, 1)
    east_cant_html = """<td style="text-align: center">"""+east_cant+"""</td>"""
    east_base = input("Eastern Base? ")
    east_base = Typo_Fix(east_base, 1)
    east_base_html = """<td style="text-align: center">"""+east_base+"""</td>"""
    east_bracket = input("Eastern Light Brackets? ")
    east_bracket = Typo_Fix(east_bracket, 1)
    east_bracket_html = """<td style="text-align: center">"""+east_bracket+"""</td>"""
    east_lights = input("Eastern Lights? ")
    east_lights = Typo_Fix(east_lights, 1)
    east_lights_html = """<td style="text-align: center">"""+east_lights+"""</td>"""
    east_gate_lights = input("Eastern Gate Lights? ")
    east_gate_lights = Typo_Fix(east_gate_lights, 1)
    east_gate_lights_html = """<td style="text-align: center">"""+east_gate_lights+"""</td>"""
    east_gate = input("Eastern Gate Mechanism? ")
    east_gate = Typo_Fix(east_gate, 1)
    east_gate_html = """<td style="text-align: center">"""+east_gate+"""</td>"""
    east_gate_str = input("Eastern Gate Striping? ")
    east_gate_str = Typo_Fix(east_gate_str, 1)
    east_gate_str_html = """<td style="text-align: center">"""+east_gate_str+"""</td>"""
    if east_bell == "" and east_cant == "" and east_base == "" and east_bracket == "" and east_lights == "" and east_gate_lights == "" and east_gate == "" and east_gate_str == "":
        EastTableCheck = False
if EastMed == True:
    EastMedTableCheck = True
    print("--Eastern Median Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Eastern Median Signal</em></strong></td>"""
    east_med_bell = input("Eastern Median Bell? ")
    east_med_bell = Typo_Fix(east_med_bell, 1)
    east_med_bell_html = """<td style="text-align: center">"""+east_med_bell+"""</td>"""
    east_med_cant = input("Eastern Median Cantilever? ")
    east_med_cant = Typo_Fix(east_med_cant, 1)
    east_med_cant_html = """<td style="text-align: center">"""+east_med_cant+"""</td>"""
    east_med_base = input("Eastern Median Base? ")
    east_med_base = Typo_Fix(east_med_base, 1)
    east_med_base_html = """<td style="text-align: center">"""+east_med_base+"""</td>"""
    east_med_bracket = input("Eastern Median Light Brackets? ")
    east_med_bracket = Typo_Fix(east_med_bracket, 1)
    east_med_bracket_html = """<td style="text-align: center">"""+east_med_bracket+"""</td>"""
    east_med_lights = input("Eastern Median Lights? ")
    east_med_lights = Typo_Fix(east_med_lights, 1)
    east_med_lights_html = """<td style="text-align: center">"""+east_med_lights+"""</td>"""
    east_med_gate_lights = input("Eastern Median Gate Lights? ")
    east_med_gate_lights = Typo_Fix(east_med_gate_lights, 1)
    east_med_gate_lights_html = """<td style="text-align: center">"""+east_med_gate_lights+"""</td>"""
    east_med_gate = input("Eastern Median Gate Mechanism? ")
    east_med_gate = Typo_Fix(east_med_gate, 1)
    east_med_gate_html = """<td style="text-align: center">"""+east_med_gate+"""</td>"""
    east_med_gate_str = input("Eastern Median Gate Striping? ")
    east_med_gate_str = Typo_Fix(east_med_gate_str, 1)
    east_med_gate_str_html = """<td style="text-align: center">"""+east_med_gate_str+"""</td>"""
    if east_med_bell == "" and east_med_cant == "" and east_med_base == "" and east_med_bracket == "" and east_med_lights == "" and east_med_gate_lights == "" and east_med_gate == "" and east_med_gate_str == "":
        EastMedTableCheck = False
if West == True:
    WestTableCheck = True
    print("--Western Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Western Signal</em></strong></td>"""
    west_bell = input("Western Bell? ")
    west_bell = Typo_Fix(west_bell, 1)
    west_bell_html = """<td style="text-align: center">"""+west_bell+"""</td>"""
    west_cant = input("Western Cantilever? ")
    west_cant = Typo_Fix(west_cant, 1)
    west_cant_html = """<td style="text-align: center">"""+west_cant+"""</td>"""
    west_base = input("Western Base? ")
    west_base = Typo_Fix(west_base, 1)
    west_base_html = """<td style="text-align: center">"""+west_base+"""</td>"""
    west_bracket = input("Western Light Brackets? ")
    west_bracket = Typo_Fix(west_bracket, 1)
    west_bracket_html = """<td style="text-align: center">"""+west_bracket+"""</td>"""
    west_lights = input("Western Lights? ")
    west_lights = Typo_Fix(west_lights, 1)
    west_lights_html = """<td style="text-align: center">"""+west_lights+"""</td>"""
    west_gate_lights = input("Western Gate Lights? ")
    west_gate_lights = Typo_Fix(west_gate_lights, 1)
    west_gate_lights_html = """<td style="text-align: center">"""+west_gate_lights+"""</td>"""
    west_gate = input("Western Gate Mechanism? ")
    west_gate = Typo_Fix(west_gate, 1)
    west_gate_html = """<td style="text-align: center">"""+west_gate+"""</td>"""
    west_gate_str = input("Western Gate Striping? ")
    west_gate_str = Typo_Fix(west_gate_str, 1)
    west_gate_str_html = """<td style="text-align: center">"""+west_gate_str+"""</td>"""
    if west_bell == "" and west_cant == "" and west_base == "" and west_bracket == "" and west_lights == "" and west_gate_lights == "" and west_gate == "" and west_gate_str == "":
        WestTableCheck = False
if WestMed == True:
    WestMedTableCheck = True
    print("--Western Median Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="350" style="text-align: center"><strong><em>Western Median Signal</em></strong></td>"""
    west_med_bell = input("Western Median Bell? ")
    west_med_bell = Typo_Fix(west_med_bell, 1)
    west_med_bell_html = """<td style="text-align: center">"""+west_med_bell+"""</td>"""
    west_med_cant = input("Western Median Cantilever? ")
    west_med_cant = Typo_Fix(west_med_cant, 1)
    west_med_cant_html = """<td style="text-align: center">"""+west_med_cant+"""</td>"""
    west_med_base = input("Western Median Base? ")
    west_med_base = Typo_Fix(west_med_base, 1)
    west_med_base_html = """<td style="text-align: center">"""+west_med_base+"""</td>"""
    west_med_bracket = input("Western Median Light Brackets? ")
    west_med_bracket = Typo_Fix(west_med_bracket, 1)
    west_med_bracket_html = """<td style="text-align: center">"""+west_med_bracket+"""</td>"""
    west_med_lights = input("Western Median Lights? ")
    west_med_lights = Typo_Fix(west_med_lights, 1)
    west_med_lights_html = """<td style="text-align: center">"""+west_med_lights+"""</td>"""
    west_med_gate_lights = input("Western Median Gate Lights? ")
    west_med_gate_lights = Typo_Fix(west_med_gate_lights, 1)
    west_med_gate_lights_html = """<td style="text-align: center">"""+west_med_gate_lights+"""</td>"""
    west_med_gate = input("Western Median Gate Mechanism? ")
    west_med_gate = Typo_Fix(west_med_gate, 1)
    west_med_gate_html = """<td style="text-align: center">"""+west_med_gate+"""</td>"""
    west_med_gate_str = input("Western Median Gate Striping? ")
    west_med_gate_str = Typo_Fix(west_med_gate_str, 1)
    west_med_gate_str_html = """<td style="text-align: center">"""+west_med_gate_str+"""</td>"""
    if west_med_bell == "" and west_med_cant == "" and west_med_base == "" and west_med_bracket == "" and west_med_lights == "" and west_med_gate_lights == "" and west_med_gate == "" and west_med_gate_str == "":
        WestMedTableCheck = False

removebellhtml = """<tr>
      <td height="22" style="text-align: center">Bell:</td>
       """+north_bell_html+"""
       """+north_med_bell_html+"""
       """+south_bell_html+"""
       """+south_med_bell_html+"""
       """+east_bell_html+"""
       """+east_med_bell_html+"""
       """+west_bell_html+"""
       """+west_med_bell_html+"""
      </tr>"""
if north_bell == "" and north_med_bell == "" and south_bell == "" and south_med_bell == "" and east_bell == ""and east_med_bell == "" and west_bell == "" and west_med_bell == "":
    removebellhtml = ""

removecantileverhtml = """<tr>
      <td height="22" style="text-align: center">Cantilever:</td>
       """+north_cant_html+"""
       """+north_med_cant_html+"""
       """+south_cant_html+"""
       """+south_med_cant_html+"""
       """+east_cant_html+"""
       """+east_med_cant_html+"""
       """+west_cant_html+"""
       """+west_med_cant_html+"""
      </tr>"""
if north_cant == "" and north_med_cant == "" and south_cant == "" and south_med_cant == "" and east_cant == "" and east_med_cant == "" and west_cant == "" and west_med_cant == "":
    removecantileverhtml = ""

removebasehtml = """<tr>
      <td height="22" style="text-align: center">Base:</td>
       """+north_base_html+"""
       """+north_med_base_html+"""
       """+south_base_html+"""
       """+south_med_base_html+"""
       """+east_base_html+"""
       """+east_med_base_html+"""
       """+west_base_html+"""
       """+west_med_base_html+"""
      </tr>"""
if north_base == "" and north_med_base == "" and south_base == "" and south_med_base == "" and east_base == "" and east_med_base == "" and west_base == "" and west_med_base == "":
    removebasehtml = ""

removebrackethtml = """<tr>
      <td height="22" style="text-align: center">Light Brackets:</td>
       """+north_bracket_html+"""
       """+north_med_bracket_html+"""
       """+south_bracket_html+"""
       """+south_med_bracket_html+"""
       """+east_bracket_html+"""
       """+east_med_bracket_html+"""
       """+west_bracket_html+"""
       """+west_med_bracket_html+"""
      </tr>"""
if north_bracket == "" and north_med_bracket == "" and south_bracket == "" and south_med_bracket == "" and east_bracket == "" and east_med_bracket == "" and west_bracket == "" and west_med_bracket == "":
    removebrackethtml = ""

removelightshtml = """<tr>
      <td height="22" style="text-align: center">Lights:</td>
       """+north_lights_html+"""
       """+north_med_lights_html+"""
       """+south_lights_html+"""
       """+south_med_lights_html+"""
       """+east_lights_html+"""
       """+east_med_lights_html+"""
       """+west_lights_html+"""
       """+west_med_lights_html+"""
      </tr>"""
if north_lights == "" and north_med_lights == "" and south_lights == "" and south_med_lights == "" and east_lights == "" and east_med_lights == "" and west_lights == "" and west_med_lights == "":
    removelightshtml = ""
    
removegatelightshtml = """<tr>
      <td height="22" style="text-align: center">Gate Lights:</td>
      """+north_gate_lights_html+"""
      """+north_med_gate_lights_html+"""
      """+south_gate_lights_html+"""
      """+south_med_gate_lights_html+"""
      """+east_gate_lights_html+"""
      """+east_med_gate_lights_html+"""
      """+west_gate_lights_html+"""
      """+west_med_gate_lights_html+"""
      </tr>"""
if north_gate_lights == "" and north_med_gate_lights == "" and south_gate_lights == "" and south_med_gate_lights == "" and east_gate_lights == "" and east_med_gate_lights == "" and west_gate_lights == "" and west_med_gate_lights == "":
    removegatelightshtml = ""

removegateshtml = """<tr>
      <td height="22" style="text-align: center">Gate Mechanism:</td>
      """+north_gate_html+"""
      """+north_med_gate_html+"""
      """+south_gate_html+"""
      """+south_med_gate_html+"""
      """+east_gate_html+"""
      """+east_med_gate_html+"""
      """+west_gate_html+"""
      """+west_med_gate_html+"""
      </tr>"""
if north_gate == "" and north_med_gate == "" and south_gate == "" and south_med_gate == "" and east_gate == "" and east_med_gate == "" and west_gate == "" and west_med_gate == "":
    removegateshtml = ""
    
removegatestripehtml = """<tr>
      <td height="22" style="text-align: center">Gate Striping:</td>
      """+north_gate_str_html+"""
      """+north_med_gate_str_html+"""
      """+south_gate_str_html+"""
      """+south_med_gate_str_html+"""
      """+east_gate_str_html+"""
      """+east_med_gate_str_html+"""
      """+west_gate_str_html+"""
      """+west_med_gate_str_html+"""
      </tr>"""
if north_gate_str == "" and north_med_gate_str == "" and south_gate_str == "" and south_med_gate_str == "" and east_gate_str == "" and east_med_gate_str == "" and west_gate_str == "" and west_med_gate_str == "":
    removegatestripehtml = ""

#Sort The HTML Together

tablehtml = """<br><table align="center" border="1">
  <tbody>
    <tr>
      <td width="126" height="22" style="text-align: center">&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</td>
      """+tableheaderhtml+"""
    </tr>
    """+removebellhtml+"""
    """+removecantileverhtml+"""
    """+removebasehtml+"""
    """+removebrackethtml+"""
    """+removelightshtml+"""
    """+removegatelightshtml+"""
    """+removegateshtml+"""
    """+removegatestripehtml+"""
  </tbody>
</table>"""

if NorthTableCheck == False and NorthMedTableCheck == False and SouthTableCheck == False and SouthMedTableCheck == False and EastTableCheck == False and EastMedTableCheck == False and WestTableCheck == False and WestMedTableCheck == False:
    tablehtml = ""

#Made Main Signal And Median Signal Crossing Table

#Make Pedestrian Signal Crossing Table

tableheaderhtml = ""

north_bell_html = ""
north_cant_html = ""
north_base_html = ""
north_bracket_html = ""
north_lights_html = ""
north_gate_lights_html = ""
north_gate_html = ""
north_gate_str_html = ""

north_bell = ""
north_base = ""
north_cant = ""
north_bracket = ""
north_lights = ""
north_gate_lights = ""
north_gate = ""
north_gate_str = ""

south_bell_html = ""
south_cant_html = ""
south_base_html = ""
south_bracket_html = ""
south_lights_html = ""
south_gate_lights_html = ""
south_gate_html = ""
south_gate_str_html = ""

south_bell = ""
south_base = ""
south_cant = ""
south_bracket = ""
south_lights = ""
south_gate_lights = ""
south_gate = ""
south_gate_str = ""

east_bell_html = ""
east_cant_html = ""
east_base_html = ""
east_bracket_html = ""
east_lights_html = ""
east_gate_lights_html = ""
east_gate_html = ""
east_gate_str_html = ""

east_bell = ""
east_base = ""
east_cant = ""
east_bracket = ""
east_lights = ""
east_gate_lights = ""
east_gate = ""
east_gate_str = ""

west_bell_html = ""
west_cant_html = ""
west_base_html = ""
west_bracket_html = ""
west_lights_html = ""
west_gate_lights_html = ""
west_gate_html = ""
west_gate_str_html = ""

west_bell = ""
west_base = ""
west_cant = ""
west_bracket = ""
west_lights = ""
west_gate_lights = ""
west_gate = ""
west_gate_str = ""

NorthTableCheck = False
SouthTableCheck = False
EastTableCheck = False
WestTableCheck = False

if NorthPed == True:
    NorthTableCheck = True
    print("--Northern Pedestrian Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="225" style="text-align: center"><strong><em>Northern Pedestrian Signal</em></strong></td>"""
    north_bell = input("Northern Pedestrian Bell? ")
    north_bell = Typo_Fix(north_bell, 1)
    north_bell_html = """<td style="text-align: center">"""+north_bell+"""</td>"""
    north_cant = input("Northern Pedestrian Cantilever? ")
    north_cant = Typo_Fix(north_cant, 1)
    north_cant_html = """<td style="text-align: center">"""+north_cant+"""</td>"""
    north_base = input("Northern Pedestrian Base? ")
    north_base = Typo_Fix(north_base, 1)
    north_base_html = """<td style="text-align: center">"""+north_base+"""</td>"""
    north_bracket = input("Northern Pedestrian Light Brackets? ")
    north_bracket = Typo_Fix(north_bracket, 1)
    north_bracket_html = """<td style="text-align: center">"""+north_bracket+"""</td>"""
    north_lights = input("Northern Pedestrian Lights? ")
    north_lights = Typo_Fix(north_lights, 1)
    north_lights_html = """<td style="text-align: center">"""+north_lights+"""</td>"""
    north_gate_lights = input("Northern Pedestrian Gate Lights? ")
    north_gate_lights = Typo_Fix(north_gate_lights, 1)
    north_gate_lights_html = """<td style="text-align: center">"""+north_gate_lights+"""</td>"""
    north_gate = input("Northern Pedestrian Gate Mechanism? ")
    north_gate = Typo_Fix(north_gate, 1)
    north_gate_html = """<td style="text-align: center">"""+north_gate+"""</td>"""
    north_gate_str = input("Northern Pedestrian Gate Striping? ")
    north_gate_str = Typo_Fix(north_gate_str, 1)
    north_gate_str_html = """<td style="text-align: center">"""+north_gate_str+"""</td>"""
    if north_bell == "" and north_cant == "" and north_base == "" and north_bracket == "" and north_lights == "" and north_gate_lights == "" and north_gate == "" and north_gate_str == "":
        NorthTableCheck = False
if SouthPed == True:
    SouthTableCheck = True
    print("--Southern Pedestrian Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="225" style="text-align: center"><strong><em>Southern Pedestrian Signal</em></strong></td>"""
    south_bell = input("Southern Pedestrian Bell? ")
    south_bell = Typo_Fix(south_bell, 1)
    south_bell_html = """<td style="text-align: center">"""+south_bell+"""</td>"""
    south_cant = input("Southern Pedestrian Cantilever? ")
    south_cant = Typo_Fix(south_cant, 1)
    south_cant_html = """<td style="text-align: center">"""+south_cant+"""</td>"""
    south_base = input("Southern Pedestrian Base? ")
    south_base = Typo_Fix(south_base, 1)
    south_base_html = """<td style="text-align: center">"""+south_base+"""</td>"""
    south_bracket = input("Southern Pedestrian Light Brackets? ")
    south_bracket = Typo_Fix(south_bracket, 1)
    south_bracket_html = """<td style="text-align: center">"""+south_bracket+"""</td>"""
    south_lights = input("Southern Pedestrian Lights? ")
    south_lights = Typo_Fix(south_lights, 1)
    south_lights_html = """<td style="text-align: center">"""+south_lights+"""</td>"""
    south_gate_lights = input("Southern Pedestrian Gate Lights? ")
    south_gate_lights = Typo_Fix(south_gate_lights, 1)
    south_gate_lights_html = """<td style="text-align: center">"""+south_gate_lights+"""</td>"""
    south_gate = input("Southern Pedestrian Gate Mechanism? ")
    south_gate = Typo_Fix(south_gate, 1)
    south_gate_html = """<td style="text-align: center">"""+south_gate+"""</td>"""
    south_gate_str = input("Southern Pedestrian Gate Striping? ")
    south_gate_str = Typo_Fix(south_gate_str, 1)
    south_gate_str_html = """<td style="text-align: center">"""+south_gate_str+"""</td>"""
    if south_bell == "" and south_cant == "" and south_base == "" and south_bracket == "" and south_lights == "" and south_gate_lights == "" and south_gate == "" and south_gate_str == "":
        SouthTableCheck = False
if EastPed == True:
    EastTableCheck = True
    print("--Eastern Pedestrian Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="225" style="text-align: center"><strong><em>Eastern Pedestrian Signal</em></strong></td>"""
    east_bell = input("Eastern Pedestrian Bell? ")
    east_bell = Typo_Fix(east_bell, 1)
    east_bell_html = """<td style="text-align: center">"""+east_bell+"""</td>"""
    east_cant = input("Eastern Pedestrian Cantilever? ")
    east_cant = Typo_Fix(east_cant, 1)
    east_cant_html = """<td style="text-align: center">"""+east_cant+"""</td>"""
    east_base = input("Eastern Pedestrian Base? ")
    east_base = Typo_Fix(east_base, 1)
    east_base_html = """<td style="text-align: center">"""+east_base+"""</td>"""
    east_bracket = input("Eastern Pedestrian Light Brackets? ")
    east_bracket = Typo_Fix(east_bracket, 1)
    east_bracket_html = """<td style="text-align: center">"""+east_bracket+"""</td>"""
    east_lights = input("Eastern Pedestrian Lights? ")
    east_lights = Typo_Fix(east_lights, 1)
    east_lights_html = """<td style="text-align: center">"""+east_lights+"""</td>"""
    east_gate_lights = input("Eastern Pedestrian Gate Lights? ")
    east_gate_lights = Typo_Fix(east_gate_lights, 1)
    east_gate_lights_html = """<td style="text-align: center">"""+east_gate_lights+"""</td>"""
    east_gate = input("Eastern Pedestrian Gate Mechanism? ")
    east_gate = Typo_Fix(east_gate, 1)
    east_gate_html = """<td style="text-align: center">"""+east_gate+"""</td>"""
    east_gate_str = input("Eastern Pedestrian Gate Striping? ")
    east_gate_str = Typo_Fix(east_gate_str, 1)
    east_gate_str_html = """<td style="text-align: center">"""+east_gate_str+"""</td>"""
    if east_bell == "" and east_cant == "" and east_base == "" and east_bracket == "" and east_lights == "" and east_gate_lights == "" and east_gate == "" and east_gate_str == "":
        EastTableCheck = False
if WestPed == True:
    WestTableCheck = True
    print("--Western Signal--")
    tableheaderhtml = tableheaderhtml + """
    <td width="225" style="text-align: center"><strong><em>Western Pedestrian Signal</em></strong></td>"""
    west_bell = input("Western Pedestrian Bell? ")
    west_bell = Typo_Fix(west_bell, 1)
    west_bell_html = """<td style="text-align: center">"""+west_bell+"""</td>"""
    west_cant = input("Western Pedestrian Cantilever? ")
    west_cant = Typo_Fix(west_cant, 1)
    west_cant_html = """<td style="text-align: center">"""+west_cant+"""</td>"""
    west_base = input("Western Pedestrian Base? ")
    west_base = Typo_Fix(west_base, 1)
    west_base_html = """<td style="text-align: center">"""+west_base+"""</td>"""
    west_bracket = input("Western Pedestrian Light Brackets? ")
    west_bracket = Typo_Fix(west_bracket, 1)
    west_bracket_html = """<td style="text-align: center">"""+west_bracket+"""</td>"""
    west_lights = input("Western Pedestrian Lights? ")
    west_lights = Typo_Fix(west_lights, 1)
    west_lights_html = """<td style="text-align: center">"""+west_lights+"""</td>"""
    west_gate_lights = input("Western Pedestrian Gate Lights? ")
    west_gate_lights = Typo_Fix(west_gate_lights, 1)
    west_gate_lights_html = """<td style="text-align: center">"""+west_gate_lights+"""</td>"""
    west_gate = input("Western Pedestrian Gate Mechanism? ")
    west_gate = Typo_Fix(west_gate, 1)
    west_gate_html = """<td style="text-align: center">"""+west_gate+"""</td>"""
    west_gate_str = input("Western Pedestrian Gate Striping? ")
    west_gate_str = Typo_Fix(west_gate_str, 1)
    west_gate_str_html = """<td style="text-align: center">"""+west_gate_str+"""</td>"""
    if west_bell == "" and west_cant == "" and west_base == "" and west_bracket == "" and west_lights == "" and west_gate_lights == "" and west_gate == "" and west_gate_str == "":
        WestTableCheck = False

removebellhtml = """<tr>
      <td height="22" style="text-align: center">Bell:</td>
       """+north_bell_html+"""
       """+south_bell_html+"""
       """+east_bell_html+"""
       """+west_bell_html+"""
      </tr>"""
if north_bell == "" and south_bell == "" and east_bell == "" and west_bell == "":
    removebellhtml = ""

removecantileverhtml = """<tr>
      <td height="22" style="text-align: center">Cantilever:</td>
       """+north_cant_html+"""
       """+south_cant_html+"""
       """+east_cant_html+"""
       """+west_cant_html+"""
      </tr>"""
if north_cant == "" and south_cant == "" and east_cant == "" and west_cant == "":
    removecantileverhtml = ""

removebasehtml = """<tr>
      <td height="22" style="text-align: center">Base:</td>
       """+north_base_html+"""
       """+south_base_html+"""
       """+east_base_html+"""
       """+west_base_html+"""
      </tr>"""
if north_base == "" and south_base == "" and east_base == "" and west_base == "":
    removebasehtml = ""

removebrackethtml = """<tr>
      <td height="22" style="text-align: center">Light Brackets:</td>
       """+north_bracket_html+"""
       """+south_bracket_html+"""
       """+east_bracket_html+"""
       """+west_bracket_html+"""
      </tr>"""
if north_bracket == "" and south_bracket == "" and east_bracket == "" and west_bracket == "":
    removebrackethtml = ""

removelightshtml = """<tr>
      <td height="22" style="text-align: center">Lights:</td>
       """+north_lights_html+"""
       """+south_lights_html+"""
       """+east_lights_html+"""
       """+west_lights_html+"""
      </tr>"""
if north_lights == "" and south_lights == "" and east_lights == "" and west_lights == "":
    removelightshtml = ""
    
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

if NorthTableCheck != False or SouthTableCheck != False or EastTableCheck != False or WestTableCheck != False:
    if tablehtml != "":
        tablehtml = tablehtml+"""<br><br><table align="center" border="1">
  <tbody>
    <tr>
      <td width="126" height="22" style="text-align: center">&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</td>
      """+tableheaderhtml+"""
    </tr>
    """+removebellhtml+"""
    """+removecantileverhtml+"""
    """+removebasehtml+"""
    """+removebrackethtml+"""
    """+removelightshtml+"""
    """+removegatelightshtml+"""
    """+removegateshtml+"""
    """+removegatestripehtml+"""
  </tbody>
</table>"""
    else:
        tablehtml = """<br><table align="center" border="1">
  <tbody>
    <tr>
      <td width="126" height="22" style="text-align: center">&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</td>
      """+tableheaderhtml+"""
    </tr>
    """+removebellhtml+"""
    """+removecantileverhtml+"""
    """+removebasehtml+"""
    """+removebrackethtml+"""
    """+removelightshtml+"""
    """+removegatelightshtml+"""
    """+removegateshtml+"""
    """+removegatestripehtml+"""
  </tbody>
</table>"""

#Finished Making Crossing Table

input("Program has not crashed! :D" )

# to open/create a new html file in the write mode
f = open('Output/'+fullname+"/"+fullnamehtml+'.html', 'w')
  
#Begin HTML

html_template = """<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<!-- Page originally created on """+crossingdate+""" by """+Creator+""" using HopenRXRTools """+VERSION+""" --><title>""" + crossing_name + " ("+ crossing_city +")"+ """</title>
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
border="0" cellpadding="0" cellspacing="0" align="center">
<tbody>
<tr>
<td style="text-align: center; height: 140px; width: 667px;"><span
style="vertical-align: middle; text-align: center;"><img src="""+Filenamefix2+HeaderFilename+Filenamefix2+"""
alt=""></span></td>
<td style="width: 277px; text-align: center; vertical-align: middle;">"""+rrhtml+"""<br>
      <br>
"""+mpblankhtml+""""""+mphtml+""""""+quietzone+"""</td>
</tr>
</tbody>
</table>
<br>
"""+defunctxing+"""
<table style="width: 77%; text-align: left; margin-left: auto; margin-right: auto;" border="0" cellpadding="0" cellspacing="8">
<tbody>
<tr>
<td style="text-align: center; vertical-align: middle;"><img src="http://www.rxrsignals.com/Graphics/Dates/Created.png" alt="" height="24" width="98"><img src="http://www.rxrsignals.com/Graphics/Dates/Blank.png" alt="" height="24" width="9"><img src="http://www.rxrsignals.com/Graphics/Dates/Month/"""+str(month)+""".png" alt=""><img src="http://www.rxrsignals.com/Graphics/Dates/Blank.png" alt="" height="24" width="9">"""+day_html+"""<img src="http://www.rxrsignals.com/Graphics/Dates/Year/"""+str(year)+""".png" alt=""></td>
</tr>
</tbody>
</table>
<br>
<table
style="width: 77%; height: 1%; text-align: left; margin-left: auto; margin-right: auto;"
border="0" cellpadding="0" cellspacing="0" align="center">
<tbody>
"""+crossingaccidentshtml+"""
"""+dothtmlblank+"""
<tr>
<td align="center" valign="middle"><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
src="http://www.rxrsignals.com/Graphics/Daily_Trains/"""+crossing_daily+""".png" 
alt=""></font></font></strong><strong><font
face="Arial,Helvetica,Monaco"><font color="WHITE"><img
src="http://www.rxrsignals.com/Graphics/Daily_Trains/Blank.png" alt=""
height="12" width="7"><img src="http://www.rxrsignals.com/Graphics/Daily_Trains/Since/"""+crossing_asof+""".png" 
alt=""></font></font></strong></td>
</tr>
</tbody>
</table>
"""+tablehtml+"""
<br>
<div style="text-align: center;">
Pictures 1-"""+str(name)+""" were taken on """+PhotoDates+""", by """+Username+""".<br>
This crossing is located on the """+Subdivision+""".<br>
"""+pagecreatedhtml+"""<br>
</div>
<br>
"""+streetviewhtml+facingimagehtml+northernsignalhtml+northernmediansignalhtml+southernsignalhtml+southernmediansignalhtml+easternsignalhtml+easternmediansignalhtml+westernsignalhtml+westernmediansignalhtml+northernpedsignalhtml+southernpedsignalhtml+easternpedsignalhtml+westernpedsignalhtml+relayandgradehtml+trackfacinghtml+ActionShotshtml+"""
<br>"""+VideoHTML+"""
</body>
</html>
"""

#End HTML

#Add Width and Height

for i in range(name+Sname):
    try:
        html_template = html_template.replace("TW"+str(i+1)+"px", str(size_list[i][1])+"px")
        html_template = html_template.replace("TL"+str(i+1)+"px", str(size_list[i][2])+"px")
    except:
        0

# writing the code into the file
f.write(html_template)
  
# close the file
f.close()