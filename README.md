 # Using MikeRXRTools

 ## Chapters

 - [Setup](#setup)
 - [Making Crossing Pages](#making-crossing-pages)
 - [Making Crossing Headers](#making-crossing-headers)
 - [Finding Crossing Street Name and City](#finding-crossing-street-name-and-city)
 - [Getting DOT Number, Milepost, Railroads, Accident Count, and Daily Trains](#getting-dot-number-milepost-railroads-accident-count-and-daily-trains)
   - [FRA Website](#fra-website)
   - [FRA Map](#fra-map)
   - [Crossing Information](#crossing-information)

 ## Setup

 In order for MikeRXRTools to run, it requires the Python Engine and the Pillow Module for photo editing.

 MikeRXRTools will run on Windows 10 and 11 computers.

1. First, download Python 3.0 from the offical python website: https://www.python.org/downloads/windows/

 MAKE SURE TO SPECIFICALLY DOWNLOAD "Windows installer (64-bit)" FOR VERSIONS 3.12.0 OR ABOVE OR PILLOW WILL NOT INSTALL!

![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/53b5b10a-e91b-42a1-8acd-6f31522cd2ed)


2. Next, download the MikeRXRTools "Source code (Zip)" from the releases tab on the right. 

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/70a08f8d-6861-49cb-ba3c-faa9c9155dcc)
 
 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/b1dc1762-7ff8-4db7-81a2-13e77eaf78a9)



3. Once downloaded, extract the folder.

    
 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/8e1888be-b843-4cc6-ba87-2120efad02a6)

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/8a8aca43-f2e7-4849-a21d-b7ea0757337a)

4. Check if Python installed correctly by running a script in the MikeRXRTools folder called "Empty Temporary Folder Junk"

![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/7f6c6363-7ec3-475e-b6ca-cc0b51ed5b0c)


 You should be able to easily run Python scripts by double left clicking. 

 This will remove some temporary "junk" .txt files from all folders (This exists so GitHub will allow me to upload empty folders)

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

 Make sure to crop the header size to fit the text.

 Then make the header and export as PNG!

 For more info on making headers, visit this: https://docs.google.com/document/d/1squEBHujx-LUVL1bXV-agknS0YGdyvKR/edit

 ## Finding Crossing Street Name and City

 You can use Google Maps or any accurate mapping service to find the street and city name. 

 We will be using J St SW in Cedar Rapids IA as an example.

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/ab80d7ec-23eb-46c5-b178-89bad70e8cfa)

 # Getting DOT Number, Milepost, Railroads, Accident Count, and Daily Trains

 Getting the DOT number and the Milepost number is straightfoward with the correct instructions. There are two methods you can use.

 ## FRA Website

 If you have a photo of the DOT number tag at the crossing (Like This).

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/5150402d-be04-48d6-bb65-3bc847c11b71)

 You can go to this website to get the milepost, railroad, and accident count with this website: https://safetydata.fra.dot.gov/OfficeofSafety/PublicSite/Crossing/Crossing.aspx

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/055b303c-8796-48d5-a840-d07febe6173d)

 Once you have typed the DOT number in, you can then download a PDF of both accidents and all crossing info that you need located in "inventory" and "accident".

 ## FRA Map

 If you don't have your crossing DOT number, you can still get the same results by using an interactive map from the FRA: https://fragis.fra.dot.gov/gisfrasafety/

 You should get a map that looks like this:

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/4b053096-0c3d-47a1-8795-0bb7c159be84)

 You can find your crossing by typing in its coardinates in the search bar with the help of Google Maps or by zooming in and finding your crossing on the map.

 Here is J St SW on the FRA map:

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/6018a5d0-893e-4c87-9557-491d5e816cd0)

 You can find the DOT number and milepost when you left click the orange dot.

 To expand the info menu, click this button here:

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/5cdfac01-62fe-468a-8731-ed2295625ffc)

 You can find some of the info you need such as the DOT number, milepost, railroad owner, and the railroad subdivision on the info menu:

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/74dd5686-60d6-4357-8822-d2700eca6f4b)

 However it does not show the amount of accidents or trains per day. 
 
 At the bottom of the info menu, you can download both the accident count PDF and crossing inventory PDF here:

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/874c31b5-370f-4d2f-9cef-8214c778681f)

 ## Crossing Information

 Its very easy to get the info from both PDF files. 

 The accident PDF file has one page per accident, this means that since this crossing has 6 pages, there have been 6 accidents at this crossing (Yikes!)

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/1437f4c2-533f-4767-8627-3459c1de0b56)

 The crossing inventory PDF is a little more complicated but still easy to find what you need with CTRL+F.

 Under "Part II: Railroad Information" or with CTRL+F "Daily", is the location of the daily train count:

 ![image](https://github.com/Hopen111/MikeRXRTools/assets/147209436/9575671c-afa5-4057-9196-6b2a00200635)

 Combining all numbers together, this crossing has 35 trains per day as of 2019.

 You can find all other info like the subdivision and associated railroads in the PDF file as well.


