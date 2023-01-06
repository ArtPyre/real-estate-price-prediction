# real-estate-price-prediction
 A dataset gathering information about properties all around Belgium
## Description

### Links acquisition
main.py in list_acquisition folder.

Using Selenium to open the welkom page and manage the cookie.
Fill in the form with the name of all Belgium provinces and scrap the results of sales, for a detemined amount of pages.
store the results in the list_of_results.txt file.
Tested with 90 pages of results per query and collected 26k links in about 12 min.![Alt text](links_acquisition/results_80pages_10regions%202023-01-06.png)
The list_of_results.txt file is used by scrapping.py in data_acquisition folder, to gather all the data from indivual properties.
### Data acquisition

### Conversion to csv file

### Dependencies

* Using selenium library to scrap data 
* ex. Windows 10

### Installing

* Virtual environment, running python 3.10.9
* ...

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Marlies
Arthur
Meulemans Philippe

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments


