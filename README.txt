So in the file we may use three python files -> to_json_2022.py / html_parser.py / major_scrap.py
1: <html_parser.py>
The html_parser.py is used for read the "URL2022FallRaw.txt", which combined all the websites we need.
And then we use the html_parser.py to get the links for each of the websites. and store it in "majorURLlist2022FA.txt"
Also you can change the readfile name, in this way you can generate another txt file with all the valid links.

html_parser.py -> read -> "URL2022FallRaw.txt" -> write -> "majorURLlist2022FA.txt"

2: <major_scrap.py>
The major_scrap.py is used for read the "majorURLlist2022FA.txt" and then turn this file to a txt file that include all the 
info on the websites of every links. And the files that be generated are "majorData2022.txt" and "Database.txt".
outfile = "majorData2022.txt"
outfile2 = "DBCCommandsN.txt"

major_scrap.py -> read -> "majorURLlist2022FA.txt" -> write -> "majorData2022.txt" and "Database.txt"

3: <to_json_2022.py>
After we get the "majorData2022.txt", so we can just put the file in the to_json_2022.py and then we may get a json file that include all the 
data in the "majorData2022.txt".

to_json_2022.py -> read -> "majorData2022.txt" -> write -> majorData2022test.json

The work i did for our group this semester is that we update a README.txt about all the files that using in the -> rpi_data/Degree_Templates. We update a clear README.txt for our program about what python files can generate what type of text or JSON file. And the whole process of these codes in the file. Also, I and my teammate wrote a to_json.py to generate a JSON file about all the major information. (FILE: finalJson -> majorData2022.json) Also, I debugged one of the python files also gives each file commands. And finally, we found the problem is the major environmental science, so I put the link of environmental science into txt file called enviornmental_Science.txt. Then the major_scrap.py get the Database.txt successfully.
Lastly, we handle the final database, for combine the 2021-spring.csv and 2022-spring.csv to the 2023-spring.csv by learning pandas and writing in python code.
Most of the files we did for the semester:
Database.txt
README.txt
majorData2022.json
environmental_Science.txt
folder(no_use)
folder(new)
folder(finaljson)
to_json_2022.py
csvTOtxt.py
get2023S.py
spring-2023_Spring.txt
final(folder)
ccode.py
spring-2023.csv
