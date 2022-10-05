# General-Elections

Welcome to my General Election project!!! 
<br>

Let's talk a little about the origin of this project... I was talking to a colleague of mine where we discussed on alternative approaches to commute anywhere. We both came with the conclusion that improving Public Transportation is the answer. That's when the idea hit me. With the General Elections just around the corner I wanted to gather all the data from the House of Representatives and what they believe on Public Transportation. 
To see the algrothim

## View Live Demo
[https://general-election.herokuapp.com/](https://general-election.herokuapp.com/)


## The Algorithm to look through the politician's website 
You can check out the code here: [github.com/alexcodes11/Weather](https://github.com/alexcodes11/Weather). Now, let's talk a little about what I did in the backend... 
<br>
* First, I fetched the both the Google Places API and the Weather API into my proxy server.
* Next, I made a REST API for both API's so I can call data from the NODE.js server.
* I then added caching through a middleware for both APIs. This allows for future requests becoming faster than usual. 
* I added rate limiting to my APIs which prevents spammers from making to many requests to my API server.
* I secured the API key by hiding it with an env variable in the nodejs. 


## React Frontend 
You can check out the code here: [github.com/alexcodes11/WeatherApp](https://github.com/alexcodes11/WeatherApp). Now. let's discuss the frontend a little more...
<br>
* Now, that I have implemented the REST API. I am now able to request for the API data using React. 
* It is much more simple now. Because instead of calling an API like this in the front end: 

  * ``` fetch('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}') ```

* I am able to call this using React:

  * ``` fetch('weather/?q={city}') ```

* The reason I am able to do this is because I already made my REST API through Nodejs. It makes it much simpler to call it in REACT.

