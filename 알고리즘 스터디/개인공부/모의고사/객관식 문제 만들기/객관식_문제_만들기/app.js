const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();
const port = 3000;
const ANSWER = '안창호';
const COOKIE = {
	KEY: 'DoSK28wwVK',
	VALUE: '3Hn6cufr10',
};

app.use(cookieParser());
app.use(bodyParser.json());

app.get('/', (req,res) => {
  res.sendFile(path.join(__dirname, './index.html'));
});

app.post('/submit', (req, res) => {
	var answers = req.body && req.body.answers;
	res.cookie(COOKIE.KEY, COOKIE.VALUE).send(answers.length === 1 && answers[0] === ANSWER);
});

app.use(express.static(__dirname));

app.listen(port, () => console.log('Start Server'));
