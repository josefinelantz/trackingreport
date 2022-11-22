# Tracking report


## Background


A tracking pixel is commonly used to capture visitor activity on web sites, in order to later
display statistics on page views, visits and advertising. An example of a tracking pixel is Google Analytics.


## Task description


The task is to implement a simple report for a tracking pixel solution.


Please focus on clear, readable code and a well packaged delivery. If it seems like several days of work it is possible that you have misinterpreted something. Please email us if that is the case or if you have any questions. 


Create a program that can be run as a command-line tool, that accepts a
date-range and the path to a log file as parameters, and generates a report.


Expected output: a simple report that for each page displays the number of page views
and unique visitors for a given time range.


Given a log of visits that contains:


    |timestamp              |url           |userid|
    |2019-03-01 09:00:00UTC |/contact.html |12345 |
    |2019-03-01 09:00:00UTC |/contact.html |12346 |
    |2019-03-01 10:00:00UTC |/contact.html |12345 |
    |2019-03-01 10:30:00UTC |/home.html    |12347 |
    |2019-03-01 11:00:00UTC |/contact.html |12347 |
    |2019-03-02 11:00:00UTC |/contact.html |12348 |
    |2019-03-02 12:00:00UTC |/home.html    |12348 |
    |2019-03-03 13:00:00UTC |/home.html    |12349 |


For the time range 2019-03-01 09:00:00 - 2019-03-02 11:59:59
the report should contain the data:


    |url           |page views |visitors|
    |/contact.html |5          |4       |
    |/home.html    |1          |1       |


### Additional requirements
* You are free to choose the language to write the assignment in, and to use reasonable third
party libraries (open source or libraries bundled with the relevant run-time).
* Use appropriate and commonly known build tools for your chosen language (no dependencies on a specific IDE).
* Suitable unit tests
* The delivery should contain a Readme file with information on how to build, test, and run your
program.
* The build and instructions should be suitable for Ubuntu or OSX.
* The program should be able to handle the format in the attached [logfile](log.txt)
* Please submit your solution by email as a single .zip, .tar.gz or as a link to some cloud storage to kodprov@funnel.io. Do not use .rar or other proprietary formats.


## FAQ


Q: Is the format of timestamp and url important?
A: Yes, assume the timestamp and url will follow the format above.


Q: Are userids supposed to be numeric and/or sequential?
A: No, they should be treated as a unique sequence of characters, but may not be numeric


Q: Should the command line tool be interactive?
A: No, just simple command line arguments for the date-range and file path are fine
