 # Using HopenRXRTools

 ## Chapters

 - [Setup](#setup)
 - [Making Crossing Pages](#making-crossing-pages)
 - [Making Crossing Headers](#making-crossing-headers)
 - [Finding Crossing Street Name and City](#finding-crossing-street-name-and-city)
 - [Getting DOT Number, Milepost, Railroads, Accident Count, and Daily Trains](#getting-dot-number-milepost-railroads-accident-count-and-daily-trains)
   - [FRA Website](#fra-website)
   - [FRA Map](#fra-map)
   - [Crossing Information](#crossing-information)
 - [Inserting Photos Into HopenRXRTools](#inserting-photos-into-HopenRXRTools)
 - [Running HopenRXRTools](#running-HopenRXRTools)
   - [Railroad Logos](#railroad-logos)
   - [Proccessing Photos Warning](#proccessing-photos-warning)
   - [Track Views](#track-views)
   - [Track View Link](#track-view-link)
   - [Photo Information](#photo-information)
   - [Subdivision](#subdivision)
   - [Videos](#videos)
   - [Crossing Info Table](#crossing-info-table)
 - [KompoZer](#kompozer)
   - [Fixing Typos and Other Small Edits](#fixing-typos-and-other-small-edits)
   - [Rearranging and Moving Photos](#rearranging-and-moving-photos)

 ## Setup

 In order for HopenRXRTools to run, it requires the Python Engine and the Pillow Module for photo editing.

 HopenRXRTools will run on Windows 10 and 11 computers.

1. First, download Python 3.0 from the offical python website: https://www.python.org/downloads/windows/

 MAKE SURE TO SPECIFICALLY DOWNLOAD "Windows installer (64-bit)" FOR VERSIONS 3.12.0 OR ABOVE OR PILLOW WILL NOT INSTALL!

![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/53b5b10a-e91b-42a1-8acd-6f31522cd2ed)


2. Next, download the HopenRXRTools "Source code (Zip)" from the [releases](https://github.com/Hopen111/HopenRXRTools/releases) tab on the right.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/03560851-1f5b-4466-9222-c2324a35d72a)
 
 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/de6e29b0-ac63-41f6-a1de-1f377f1e803e)



3. Once downloaded, extract the folder.

    
 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/0451deec-00de-428d-8643-c885ff32bd9f)

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/b6b54ee2-d3b6-49be-95cb-7ab97945dfc4)

4. Check if Python installed correctly by running a script in the HopenRXRTools folder called "Empty Temporary Folder Junk"

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/0eb533ba-e98c-4926-8803-d2087a4e0785)


 You should be able to easily run Python scripts by double left clicking. 

 This will remove some temporary "junk" .txt files from all folders (They exist so GitHub will allow me to upload empty folders)

 If you open the folders and the junk .txt files are removed, this means Python has installed correctly!

 If there was an error, reinstall Python. If that doesn't work, try contacting me on Discord (Username: "Hopen111").

 Once Python works correctly, run the "INSTALLPILLOW" script. There is an "UNINSTALLPILLOW" script if needed.

 If all goes well, it should download Pillow without any errors.

 Now, you are done!

 ## Making Crossing Pages

 Since we have already set up the program (Hopefully), now we can begin making crossing pages!

 First, you will need to get some crossing photos, supported file types are: PNG, JPG, JEPG, and possibly a few more (HEIC WILL NOT WORK).

 Next, you have to get the basic crossing info such as street and city name, DOT, milepost, accidents, associated railroads, daily trains, and the date the photos were taken, which will all be explained below!

 ## Making Crossing Headers

 You will need to make a header since the program cannot make one at the current moment.

 For making headers, you need to download a Header.PSD file template from here: https://drive.google.com/drive/folders/1URC-K7prmxNuoZrVuk6MTQeQu3_K3gDW

 Next, go to photopea.com: https://www.photopea.com

 Open the PSD file by clicking file, and then "Open" on the top left:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/6a76b788-f8f9-4fd3-be5b-0e11aeb823ee)
 
 You should see something like this.

 Next, edit the text to fit the street name (Don't worry about the text changing size when it is edited).
 
 Make sure to crop the header size to fit the text with the crop tool on the left side of the screen.
 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/e2114bc5-839f-479c-b1ce-5bf1fdd160ba)

 Then export as PNG with "File" and then "Export As"

 Drag the header from downloads to the "Header" folder.

 And you have made the header!

 For more info on making headers, visit this: https://docs.google.com/document/d/1squEBHujx-LUVL1bXV-agknS0YGdyvKR/edit

 ## Finding Crossing Street Name and City

 You can use Google Maps or any accurate mapping service to find the street and city name. 

 We will be using J St SW in Cedar Rapids IA as an example.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/ab80d7ec-23eb-46c5-b178-89bad70e8cfa)

 # Getting DOT Number, Milepost, Railroads, Accident Count, and Daily Trains

 Getting the DOT number and the Milepost number is straightfoward with the correct instructions. There are two methods you can use.

 ## FRA Website

 If you have a photo of the DOT number tag at the crossing (Like This).

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/5150402d-be04-48d6-bb65-3bc847c11b71)

 You can go to this website to get the milepost, railroad, and accident count with this website: https://safetydata.fra.dot.gov/OfficeofSafety/PublicSite/Crossing/Crossing.aspx

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/055b303c-8796-48d5-a840-d07febe6173d)

 Once you have typed the DOT number in, you can then download a PDF of both accidents and all crossing info that you need located in "inventory" and "accident".

 ## FRA Map

 If you don't have your crossing DOT number, you can still get the same results by using an interactive map from the FRA: https://fragis.fra.dot.gov/gisfrasafety/

 You should get a map that looks like this:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/4b053096-0c3d-47a1-8795-0bb7c159be84)

 You can find your crossing by typing in its coardinates in the search bar with the help of Google Maps or by zooming in and finding your crossing on the map.

 Here is J St SW on the FRA map:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/6018a5d0-893e-4c87-9557-491d5e816cd0)

 You can find the DOT number and milepost when you left click the orange dot.

 To expand the info menu, click this button here:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/5cdfac01-62fe-468a-8731-ed2295625ffc)

 You can find some of the info you need such as the DOT number, milepost, railroad owner, and the railroad subdivision on the info menu:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/74dd5686-60d6-4357-8822-d2700eca6f4b)

 However it does not show the amount of accidents or trains per day. 
 
 At the bottom of the info menu, you can download both the accident count PDF and crossing inventory PDF here:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/874c31b5-370f-4d2f-9cef-8214c778681f)

 ## Crossing Information

 Its very easy to get the info from both PDF files. 

 The accident PDF file has one page per accident, this means that since this crossing has 6 pages, there have been 6 accidents at this crossing (Yikes!)

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/1437f4c2-533f-4767-8627-3459c1de0b56)

 The crossing inventory PDF is a little more complicated but still easy to find what you need with CTRL+F.

 Under "Part II: Railroad Information" or with CTRL+F "Daily", is the location of the daily train count:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/9575671c-afa5-4057-9196-6b2a00200635)

 Combining all numbers together, this crossing has 35 trains per day as of 2019.

 You can find all other info like the subdivision and associated railroads in the PDF file as well.

 ## Inserting Photos Into HopenRXRTools

 Also very straightfoward. Copy and paste your photos and [`header`](#making-crossing-headers) into each folder that it belongs in.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/a5f7f541-c0ca-4bba-a61d-5b9a970827da)
 
 For example, the header goes into the "Header" folder.

 And for the grade, it will go in the "Grade" folder.

 For all the northern signal photos, put them all into the "northern_signal" folder.

 Once you have put all the photos in, it's time to run the program!

 (Please do not rename or move any folders or scripts because this WILL break HopenRXRTools)

 # Running HopenRXRTools

 Double left click the "HopenRXRTools" Python script to run the program.

 You will be asked questions that the program cannot find on its own at the current moment. Such as DOT number, street name, etc.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/21e6bcd4-ab23-4d53-8949-e157a1172d1c)

 There are a few tips and tutorials when the program is running which should help you when you get stuck.

 ## Railroad Logos

 You will eventually reach this prompt:
 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/39f776b3-68e9-4cef-9d47-f72f3fd3e01f)

 You will need to get the rail logos from the site, which can be found here: http://www.rxrsignals.com/Graphics/Rail_Logos/

 Use CTRL+F to find the railroads you need, then paste the full file name into the answer input.

 Example:
 
 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/6c0b2a7e-b701-4277-a43a-5fd448ec2eec)

 HopenRXRTools allows for multiple railroads as well.

 If the rail_logos page cannot be accessed, you can get the url for a railroad from an existing site page by right clicking the logo and selecting "Copy Image Address".

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/96770af9-c006-4ab6-9a08-add99aaac2c3)

 Then take out the rest of the URL from "http://www.rxrsignals.com/Graphics/Rail_Logos/SQSC.png" to just the logo name "SQSC.png".

 Input the final result.

 ## Processing Photos Warning

 Do not worry if you see a yellow warning.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/d0df7b17-767b-41ff-96ab-93fdbe376da4)

 Make sure to worry when you see a red warning.

 If there is a red warning, then you should investigate it and fix the issue. 
 
 The possible errors include:

 --Missing header.
 --Duplicate output file name.
 --Photos outside of track view and overview folders.

 This is basically the final test for the program. 
 
 I recommend having your photos in a backup folder in case if something crashes the program or if there is a bug that also crashes the program.

 If you are ready and have rectified any issues, press ENTER twice to proceed.

 Proccessing should take less than 15 seconds, but it can be longer depending on how many photos are being processed. (duh)

 ## Track Views

 You should see something like this if everything went well:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/c38f1086-160a-4ed1-9876-c989bd65e5bc)

 Next you can use Google Maps or another accurate mapping software to find the next crossing down the track. 

 To the west of J St SW is SW 26th St. 

 As an example I will leave the facing east blank and then press ENTER to show the result for if you want to skip this part.

 To the left is the track view with both street name and link, and to the right is without both.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/e5528e53-8a38-46e3-936f-2d7fc301d37c)

 ## Track View Link

 Here is the 1st hard part. Making a link for the next crossing over. 

 If the crossing to the west or east already exists, then you can use that!

 However it most likely won't.

 Thankfully link rules are simple:

 https://www.rxrsignals.com/STATE/A-F/CITY/STREET/

 Captiallized words are words that are inputs that change.

 For example, normally 26th St SW would be:

 https://www.rxrsignals.com/Iowa/A-F/Cedar_Rapids/26(1)/

 If there are multiple crossings, "26" must be followed by "(1)".

 Luckily for me, this crossing has a link to it to the west: http://www.rxrsignals.com/Iowa/A-K/Cedar_Rapids/0/26(3)/

 We can easily paste it in.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/6eab67da-f789-43aa-999b-54dce8be682f)

 Repeat for the other side.

 If this is too complicated, then you can try using ../ to move to another directory layer above.

 We can use this to make a link. For example:

 ../26(1)

 Here are the rules for ../ link form:

 If It (Next crossing) Is Just To Another Crossing In The Same City/Town, Just Add One: ../Road_Name
 If It Leads To Another City, Add Two: ../../City_Name/Road_Name
 If It Leads To Another City, And Is In Another Alphabetical Group, Such As A-F Or G-Q, 
 Add Three: ../../../A-K/City_Name/Road_Name
 If It Leads To Another State And It Isn't Different Letter Group, Add Three: ../../../State_Name/City_Name/Road_Name
 If It Leads To Another State And Different Letter Group, Add Four: ../../../../State_Name/A-K/City_Name/Road_Name

 Crossing Link Examples:

 Cherry Grove Rd.
 ../Cherry

 80th Ave
 ../80

 Barron St. (Different Town)
 ../../Different_Town/Barron

 Sohl Ave. #2
 ../Sohl2

 Waldron St. (Different Town And Different Alphabet Catagory)
 ../../../A-K/Different_Town/Waldron

 Now the link should be done!

 ## Photo Information

 You will be asked for when the photos were taken. There are no abbreviations available on this question unlike the page creation date a few questions above near the beginning.

 You must type in something like these examples:

 March 29, 2023
 October 30, 2023
 January 5, 2024

 On the next question, just input your username.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/f9e55a05-ef3c-430f-80d7-9d2f3e9cbbc2)

 Do the same thing for the creator name, since you created the page.

 ## Subdivision

 Pretty simple. Answer with the full subdivision name like this:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/6bdd2390-03f7-4a68-a6e5-319a98592ee2)

 You can find the subdivision name in the [`crossing inventory PDF file`](#getting-dot-number-milepost-railroads-accident-count-and-daily-trains).

 ## Videos

 If there is a Youtube video you have recorded, paste the link in and then press ENTER.

 It will ask for a 2nd video, keep inputing as many videos as needed until you are finished, then press ENTER leaving it blank.

 ## Crossing Info Table

 This is the hardest part. You must use your photos or Google Street View to find the crossing parts that make up this crossing. 

 You may use the /102/ page on the site to guide you: http://www.rxrsignals.com/102/

 Some examples are listed when the program is running.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/9f44160b-b1f2-4cee-82ec-e8d5031b12fe)

 If there is no cantilever, gate, or base on all the signals, leave the answer input empty and press ENTER instead of typing "None" and the table will not include the cantilever, gate, or base.

 if you want to type: 

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/c7929f37-298c-4809-b562-e38e00c35ad0)

 Then instead of pressing SHIFT+ENTER (Which just brings you to the next question),

 Type ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/1a0e5a31-68f9-4e5a-807a-a7a82d808f37) which seperates the line!

 Once the program tells you that it has not crashed, you are done!

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/4b4ccd03-1a87-4abf-8aba-9bd9933bcaaa)

 Your finished page will appear in the "Output" folder.

 The workflow should get faster as you get the hang of it. I was able to make one page with HopenRXRTools every 10 minutes, much better than the 2 hours I was able to do before!

 # KompoZer

 If you want to fix any typos or remove the crossing table, you can download KompoZer: https://kompozer-web-authoring.en.lo4d.com/windows

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/34a67444-437b-481f-b671-c514b0ccc4e1)

 KompoZer is an HTML editor that can be used even without knowledge of HTML.

 It hasn't been updated in many years and will only download in a 32 bit executable. So this method might become obsolete in the future.

 ## Fixing Typos and Other Small Edits

 First, open the HTMl file from the page you made in the "Output" folder with "FILE, OPEN FILE".

 You should get some warnings or something. Hold ESC and they will go away quickly.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/b1151e76-75fa-4266-a3fe-4c92cd2b420c)

 It should look something like this when opened.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/f36c40d9-47d2-4d56-8a84-d89d988f909e)

 Now we can begin fixing some typos and adding some extra info.

 You can edit text by left clicking. 

 Now we can fix any typos that were created an add extra info.

 In this case, we can fix the typo under "Northern Signal Lights".

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/ad5861c3-c72d-4ba7-acde-2804d6bf369d)

 ## Rearranging and Moving Photos

 This is a little complicated but very possible.

 We are going to swap photo 18 with photo 19:

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/5de3e579-baf7-410d-9e2d-d42a5530d9fe)

 First, we will rename each photo. Photo 18 will be renamed to 19, and vice versa.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/3a89b2fd-0fe1-4a36-ba48-9ec658504968)

 After the images are renamed, you can reload the images by going to "FILE", then "RELOAD IMAGES"

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/efdbfadc-bd4e-4d54-8128-be13966c5bc0)

 Let's change track view facing south to track view facing east and track view facing east to track view facing west.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/5990a10c-2f6d-4659-bedf-916985dffb08)

 Now let's merge both text headers on the right (Because both are track views facing west).

 Right click the text box on the left. Then click "Join With Cell To The Right"

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/cd3cd1f1-351e-4550-95c3-819fe793301b)

 Then delete the extra text from the right cell.

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/a1db2245-8dbb-45fe-b4be-e48537bcae2c)

 ![image](https://github.com/Hopen111/HopenRXRTools/assets/147209436/46d884db-bd37-40f9-a0e6-f3a7df002bef)

 And now, we have moved the images!




 

