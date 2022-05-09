var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.post("/result", (req, res) => {

	// Retrieve array form post body
	var array = req.body.result;
	var cls = req.body.class;
	console.log(array, cls);

	// Return json response
	res.json({ result: 'pass'});
});

app.post("/fps", (req,res) =>{
	var fps = req.body.fps;
	console.log(fps);
	// Return json response
	res.json({ result: 'pass'});
});

// Server listening to PORT 3000
app.listen(3000);

