# Javascript web scraping

## Reading from a file
```
const fs = require('fs'):

fs.readFile('file', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
})
```

## Writing to a file
```
const fs = require('fs'):
const content = 'content';

fs.writeFile('file', content, err => {
    if (err) {
        console.error(err);
    }
})
```

## Parsing json from request
```
const request = require('request');

let url = 'https://api.com/id';

let options = {json: true};

request(url, options, (error, res, body) => {
    if (error) {
        return console.log(error);
    };

    if (res.statusCode == 200) {
        console.log(body);
    }
})
```
