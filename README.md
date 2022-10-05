# General-Elections

Welcome to my General Election project!!! 
<br>

Let's talk a little about the origin of this project... I was talking to a colleague of mine where we discussed on alternative approaches to commute anywhere. We both came with the conclusion that improving Public Transportation is the answer. That's when the idea hit me. With the General Elections just around the corner I wanted to gather all the data from the House of Representatives and what they believe on Public Transportation. 


## View Live Demo
[https://general-election.herokuapp.com/](https://general-election.herokuapp.com/)


## The Algorithm to Gather Data from the Politician's Website 
<br>

- I first gathered all the available URL's in the politicians webpage using Python Beautiful Soup HTML parser. 
   - I did this because we want to loop through each of their webpages to see if there is key words
   - While we are looping we are able to find the key words through Python Regex expressions. 
   - You can check out snippet of code underneath.
```{r test-python, engine='python'}
x = 'hello, python world!'
print(x)
print(x.split(' '))
```



## React Frontend 
You can check out the code here: [github.com/alexcodes11/WeatherApp](https://github.com/alexcodes11/WeatherApp). Now. let's discuss the frontend a little more...
<br>
* Now, that I have implemented the REST API. I am now able to request for the API data using React. 
* It is much more simple now. Because instead of calling an API like this in the front end: 

  * ``` fetch('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}') ```

* I am able to call this using React:

  * ``` fetch('weather/?q={city}') ```

* The reason I am able to do this is because I already made my REST API through Nodejs. It makes it much simpler to call it in REACT.

