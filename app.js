let fs = require('fs');

let express = require('express');
let app = express();
const port = 3000;

let returnImage = function(req, res) {
    let latestImage = getLatestImage();
    res.sendFile(__dirname + '/' + latestImage);
};

let getLatestImage = function() {
    var statsFile = fs.readFileSync("./stats.json");
    return JSON.parse(statsFile).latestImage;
}

app.listen(port, function(){
    console.log("app listening on ", port);
});

app.get('/picture', returnImage);

app.get('/captures', function(req, res){
    res.send('Access Denied');
});