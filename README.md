# real-estate-price-prediction

A dataset gathering information about properties all around Belgium

## Description

First several links of url page that contains all informations of a properties in sale/in rent are collected
Second all these pages are scrapped then all the datas are ordered, cleaned and saved to a scv file
Third these datas are use to diplay graphs that shows different informations

### Links acquisition
main.py in list_acquisition folder.

Using Selenium to open the welkom page and manage the cookie.  
Fill in the form with the name of all Belgium provinces and scrap the results of sales, for a detemined amount of pages.  
store the results in the list_of_results.txt file.  
Tested with 90 pages of results per query and collected 26k links in about 12 min.  
![Alt text](links_acquisition/results_80pages_10regions%202023-01-06.png)  
The list_of_results.txt file is used by scrapping.py in data_acquisition folder, to gather all the data from indivual properties.

### Data acquisition
main.py in data_aquisition folder.

Scrap a url page from the immoweb site with selenium 
Choose only the useful datas and cleaned the useless ones
Return a dictionnary of the property's data and save it to a scv file.

### Data analysis
main.py in data_analysis.

Use pandas to get all the datas from a scv file.
Create multiple graphs to answer some questions about the dataframe.
Save those graphs in the "graphs" folder.

[Alt text](data_analysis/graphs/Kitchen_graph.png)  
[Alt text](data_analysis/graphs/Terrace_graph.png)  

## Dependencies

* Using selenium library to scrap data 
* Using pandas library to register datas in a dataframe
* Using matplotlib and seaborn libraries to create graphs  

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

* Marlies
* Pyre Arthur
* Meulemans Philippe

## Timeline

* links_acquisition / data_acquistion => 2 january 2023 to 6 january 2023
* data_analysis => 9 january 2023 to 17 january 2023



