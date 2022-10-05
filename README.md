# General-Elections

Welcome to my General Election project!!! 

Let's talk a little about the origin of this project... I was talking to a colleague of mine where we discussed on alternative approaches to commute anywhere. We both came with the conclusion that improving Public Transportation is the answer. That's when the idea hit me. With the General Elections just around the corner I wanted to gather all the data from the House of Representatives and what they believe on Public Transportation. 


## View Live Demo
[https://general-election.herokuapp.com/](https://general-election.herokuapp.com/)
Disclaimer !!! This project is very new and is a work in progress I still have a lot to work on.


## The Algorithm to Gather Data from the Politician's Website 
<br>

- I first gathered all the available URL's in the politicians webpage using Python Beautiful Soup HTML parser. 
   - I did this because we want to loop through each of their webpages to see if there is key words
   - While we are looping we are able to find the key words through Python Regex expressions. 
   - You can check out snippet of code:
 ```
webpages = BeautifulSoup(thelink, "html.parser")
for webpage in webpages.find_all('a'):
    try:
        if theirwebsite in webpage['href']:
```
   - The code below basically returns a list in Python with all the texts that contains the key words. This is a Python Regex Expression:
 ```
transit = thelink.find_all(text=re.compile(r'\bBIKES\b | \bBIKE\b |\bSUBWAYS\b | \bMETRO\b | \bRAIL\b | \bTRANSIT\b | \bBIKING\b  | \bBUSES\b '))

```

## The PostgreSQL Database 
* This was very much a big learning experience because as soon I recieve the data I have to store it somehow. 
* Well, It wasn't long until I realized that this whole time PostgreSQL is a ***SERVER***. Now, hear me out as someone who is just getting started with the industry of 

  * ``` fetch('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}') ```

* I am able to call this using React:

  * ``` fetch('weather/?q={city}') ```

* The reason I am able to do this is because I already made my REST API through Nodejs. It makes it much simpler to call it in REACT.

## Displaying the Data through Django Backend FrameWork 

