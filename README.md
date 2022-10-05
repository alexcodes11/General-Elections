# General-Elections

Welcome to my General Election project!!! 

Let's talk a little about the origin of this project... I was talking to a colleague of mine where we discussed on alternative approaches to commute anywhere. We both came with the conclusion that improving Public Transportation is the answer. That's when the idea hit me. With the General Elections just around the corner I wanted to gather all the data from the House of Representatives and what they believe on Public Transportation. 


## View Live Demo
[https://general-election.herokuapp.com/](https://general-election.herokuapp.com/)
<br>
Disclaimer !!! This project is very new and is a work in progress I still have a lot to work on. 


## The Algorithm to Gather Data from the Politician's Website 
<br>

- I first gathered all the available URL's in the politician's webpage using Python Beautiful Soup HTML parser. 
   - I did this because we want to loop through each of their webpages to see if there is key words
   - While we are looping we are able to find the key words through Python Regex expressions. 
   - You can check out snippet of code:
 ```
webpages = BeautifulSoup(thelink, "html.parser")
for webpage in webpages.find_all('a'):
    try:
        if theirwebsite in webpage['href']:
```
   - The code below returns a Python List with all the texts that contains a key words. 
   - For example "BIKE" is a key word. My code would return ["Building pedestrian friendly infastructure so people can walk, **"BIKE"**, and run without any fear"].  
   - This is a Python Regex Expression:
 ```
transit = thelink.find_all(text=re.compile(r'\bBIKES\b | \bBIKE\b |\bSUBWAYS\b | \bMETRO\b | \bRAIL\b | \bTRANSIT\b | \bBIKING\b  | \bBUSES\b '))

```

## The PostgreSQL Database 
* This was very much a big learning experience because as soon I recieve the data I have to store it somehow. 
* Well, It wasn't long until I realized that this whole time PostgreSQL is a ***SERVER***. Now, hear me out as someone who is just getting started with the industry of software engineering I was used to Django. Django brings a lot ease when it comes to Databases. This is because Django Models takes care of a lot for you. 
* I had to learn how to truly create PostgreSQL databases on the terminal and make SELECT queries to practice with relational databases. 
* Below will be my two relational databases I created to store my data that I recieved through Python. 
* This table was created to store politician data:
~~~~sql
CREATE TABLE politician(
    politician_id INT GENERATED ALWAYS AS IDENTITY,
    full_name TEXT NOT NULL,
	house_or_senate VARCHAR(10) NOT NULL,
	state VARCHAR ( 100 ) NOT NULL,
	district VARCHAR(50) NOT NULL,
	party VARCHAR(255),
	website TEXT,
    PRIMARY KEY(politician_id)
);

~~~~

 

## Displaying the Data through Django Full Stack Application 

