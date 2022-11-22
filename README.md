# Tracking report

This program generates a report on views and visitors 
for given URLs.

## Prerequisites
Python version ^3.10.2.

Trackingreport project folder distributed via mail is downloaded locally. 

### Running the program
To run the program, three arguments are needed in formats:
<start> "YYYY-MM-DD HH:MM:SSUTC"
<end> "YYYY-MM-DD HH:MM:SSUTC"
<path> "./log.txt"

Navigate to root folder: 
run ./script.py "2019-03-01 09:00:00UTC" "2019-03-02 11:59:59UTC" "./log.txt"

## Running the tests

Tests are performed in SBE manner, visualizing exact input as well as search parameters needed to get expected output. 

### Given this input as .txt file: 

    |timestamp              |url           |userid|
    |2019-03-01 09:00:00UTC |/contact.html |12345 |
    |2019-03-01 09:00:00UTC |/contact.html |12346 |
    |2019-03-01 10:00:00UTC |/contact.html |12345 |
    |2019-03-01 10:30:00UTC |/home.html    |12347 |
    |2019-03-01 11:00:00UTC |/contact.html |12347 |
    |2019-03-02 11:00:00UTC |/contact.html |12348 |
    |2019-03-02 12:00:00UTC |/home.html    |12348 |
    |2019-03-03 13:00:00UTC |/home.html    |12349 |

### When searching the time range:
2019-03-01 09:00:00 - 2019-03-02 11:59:59

### Then you can expect: 

    URL           VIEWS  VISITORS
    /contact.html 5          4       
    /home.html    1          1       
