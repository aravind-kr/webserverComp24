const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

let books = [
	{
		isbn: '9781593275846',
		title: 'Eloquent JavaScript, Second Edition',
		author: 'Marijn Haverbeke',
		publish_date: '2014-12-14',
		publisher: 'No Starch Press',
		numOfPages: 472,
	},
];

app.use(cors());

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/book', (req, res) => {
	res.json(books);
});

app.listen(port, () => console.log(`Server listening on port ${port}!`));
