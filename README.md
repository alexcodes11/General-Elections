# General-Elections
Let's talk a little about the origin of this project... I was talking to a colleague of mine where we discussed on alternative approaches to commute anywhere. We both came with the conclusion that improving Public Transportation is the answer. That's when the idea hit me. With the General Elections just around the corner I wanted to gather all the data from the House of Representatives and what they believe on Public Transportation. I accomplished this by using Python's Beautiful Soup HTML parser which essentially gather's data from the politician's website. I used Python's Regex expression which looks for specific key words for example "Biking" would most likely be related to public transit.

To see the algrothim


Once I finished my algorithm for this project I had to learn how to set up PostgreSQL Server to collect the data from my Python Algorithm. This was truly a challenging part because it forced me to learn new concepts I already did not know. I have created a Django Application in the past which uses SQLite this helps make relational database a little bit easier. This is because Django Models takes care of all database management underneath the hood. In this project I was not able to do this because I was going to use an existing database.  So I had to learn how to hook the Heroku PostgreSQL server into my Django application while keeping it secured through process.env variables. Now, after that was done I was able to use the relational tables I have created to display the data on a Django web application. I displayed the data by using Django SQL queries. I did this all with the most challenging part of the project the time constraints. I noticed that Microsoft Leap had only a couple days left to apply. So I quickly got started on this project because I wanted to at least finish the first prototype for this project. Which I did accomplish. Right now I only have the data for the State of Washington House of Representatives. Slowly I will keep adding to this project to eventually get all 50 states of America. You can check out what I have so far on LinkedIn as well as my portfolio site which are both on my resume.