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
* As we can see we have the politician name, whether they are in the House or Senate (I added this because I always think about scalabilty!!! Maybe in the future I will Decide to add more data), their state, district, etc.

<br>

* But what about the Public Transportation where is that Data stored? Well that is our next table!!
	* Let's explain why we need two tables. Again think about scalability!
	* If in the future I need to add more issues like HealthCare, Education, and Military.
	* I will be able to do that because I seperated my tables into a relational type of table.
	* I added a ForeignKey to this table that makes it connect with the Politician Table

~~~~sql
CREATE TABLE transportation(
   transportation_id INT GENERATED ALWAYS AS IDENTITY,
   politician_id INT,
   info_or_not VARCHAR(50) NOT NULL, 
   quotes TEXT,
   website_found TEXT,
   PRIMARY KEY(transportation_id),
   CONSTRAINT fk_politician
      FOREIGN KEY(politician_id) 
	  REFERENCES politician(politician_id)
	  ON DELETE CASCADE
);

~~~~

## Other Skills I learned before getting to the grand finale...
* I now know why Docker Containers can be so important on bigger projects.
	* I had to set up my own Local PostgreSQL server which was already a hasle now imagine setting up so many things at once?
	* Docker Container is suppose to simplify this process by instead of downloading things to your own machine. You can just do it on a Container. 
	

## Displaying the Data through Django 

* In the picture below you will be able to pick between two states. Washington or Hawaii. 
	* Based on which ever button you click it will make a SQL QUERY to display you the data.
<img width="1146" alt="Screen Shot 2022-10-05 at 6 47 32 AM" src="https://user-images.githubusercontent.com/79346881/194076440-19e0906d-3db9-474c-8a8f-d9e341a2e1b1.png">

* Oh look at you, you ended up picking Washington !! Well This is what happens when you pick it: 


* As I stated before we are at the infant stages of this project but now you know how difficult it was to get this whole mini project to work. 
