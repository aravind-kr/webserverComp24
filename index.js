const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const data = require('./result.json')

const app = express();
const port = 3000;

app.use(cors());

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/data', (req, res) => {
	res.json(data);
});

app.listen(port, () => console.log(`Server listening on port ${port}!`));
