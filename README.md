This project shows 3 different visualizations of the US population from 1900 to 2014.
Along with the national debt and the debt per individual. 
Rather than just using D3 directly with JS inside HTML, I wanted to see if there was a
more effective and therby effiecient way to deal with data processing. Python was a very
familar language to me and libraries like numpy make math and data manipulation quite 
easy and efficeint (perhapes more personal preference in the end, but I found it so).

Flask and jinja2 make routing pages super easy and that isnt the only advantage. 
Flask allows python code to be used directly in the HTML itself. Meaning the variables on the
back end are easily avaliable on the front end. 

You can also easily make JSON objects and pass them to JS to be easily loaded into the page
and there by do whatever you wish with them. 

This code is adapted from the NVD3 example library. 

## Supported Browsers
NVD3 runs best on WebKit based browsers. 

* **Google Chrome: latest version (preferred)**
* **Opera 15+ (preferred)**
* Safari: latest version
* Firefox: latest version
* Internet Explorer: 9 and 10
