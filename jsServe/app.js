var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
console.log('hi')

var array;
var spf;
app.post("/result", (req, res) => {

	// Retrieve array form post body
	array = req.body.result;
	spf = req.body.spf;
	// console.log(array, spf);
	console.log("> track.py Post data");

	// Return json response
	res.json({ result: 'pass'});
});

app.post("/serve", (req, res) => {

	// Retrieve array form post body
	// console.log(array, spf);
	console.log("> monitor.py Get data");

	// Return json response
	res.json({ result: array, spf: spf});
});
// Server listening to PORT 3000
app.listen(3000);

