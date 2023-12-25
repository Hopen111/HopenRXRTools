#This Script Will Delete Temporary Files In Folders So GitHub Idiot Will Work.

input("""This Script Will Delete Any Unecessary Temporary Files When Starting Up The Program 
This Will Also Delete Any Photos You Have Already Put In. Proceed? (Press ENTER)""")

import os

if os.path.exists("Header/Delete This Please.txt"):
  os.remove("Header/Delete This Please.txt")

if os.path.exists("Output/Delete This Please.txt"):
  os.remove("Output/Delete This Please.txt")

if os.path.exists("Grade/Delete This Please.txt"):
  os.remove("Grade/Delete This Please.txt")

if os.path.exists("Relay_Case/Delete This Please.txt"):
  os.remove("Relay_Case/Delete This Please.txt")

if os.path.exists("Northern_Signal/Delete This Please.txt"):
  os.remove("Northern_Signal/Delete This Please.txt")

if os.path.exists("Southern_Signal/Delete This Please.txt"):
  os.remove("Southern_Signal/Delete This Please.txt")

if os.path.exists("Eastern_Signal/Delete This Please.txt"):
  os.remove("Eastern_Signal/Delete This Please.txt")

if os.path.exists("Western_Signal/Delete This Please.txt"):
  os.remove("Western_Signal/Delete This Please.txt")

if os.path.exists("Overviews/Overview_Facing_North/Delete This Please.txt"):
  os.remove("Overviews/Overview_Facing_North/Delete This Please.txt")

if os.path.exists("Overviews/Overview_Facing_South/Delete This Please.txt"):
  os.remove("Overviews/Overview_Facing_South/Delete This Please.txt")

if os.path.exists("Overviews/Overview_Facing_East/Delete This Please.txt"):
  os.remove("Overviews/Overview_Facing_East/Delete This Please.txt")

if os.path.exists("Overviews/Overview_Facing_West/Delete This Please.txt"):
  os.remove("Overviews/Overview_Facing_West/Delete This Please.txt")

if os.path.exists("Track_Views/Track_View_North/Delete This Please.txt"):
  os.remove("Track_Views/Track_View_North/Delete This Please.txt")

if os.path.exists("Track_Views/Track_View_South/Delete This Please.txt"):
  os.remove("Track_Views/Track_View_South/Delete This Please.txt")

if os.path.exists("Track_Views/Track_View_East/Delete This Please.txt"):
  os.remove("Track_Views/Track_View_East/Delete This Please.txt")

if os.path.exists("Track_Views/Track_View_West/Delete This Please.txt"):
  os.remove("Track_Views/Track_View_West/Delete This Please.txt")

if os.path.exists("Street_View/Delete This Please.txt"):
  os.remove("Street_View/Delete This Please.txt")

input("All Temporary Files Removed!")