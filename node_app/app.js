const express = require('express'); 

const app = express(); 

app.set('view engine', 'ejs'); 

const path = require('path'); 
app.use(express.static(path.join(__dirname, 'public'))); 

const routes = require('./routes');

app.get('/', routes.home); 
app.get('/stats', routes.stats);
app.get('*', routes.notFound); 

app.use(express.urlencoded({extended: false})); 

// Function takes user input and renders the statistics for entered company
app.post('/stat', (req, res) => {
    const {exec} = require('child_process');
    const Highcharts = require('highcharts');

    var company_name = req.body.company_name;
    var search_date_since = req.body.search_date_since; 
    
    var python, slash;
    if (process.platform === 'win32' || process.platform === 'win64') {
        command = `python ..\\bin\main.py --company-name "${company_name}" --search-date-since "${search_date_since}"`;
    }
    else {
        command = `python3 ../bin/main.py --company-name "${company_name}" --search-date-since "${search_date_since}"`;   
    }
    exec(
        // Running the python script via a shell/terminal command to pull the tweets
        command, 
        (err, stdout, stderr) => {
        if (err) {
            console.error(err)
            res.send(err); 
        }
        else {
            stdout = stdout.replace("\n", "");
            res.render("stats" ,{
                'tweets': stdout,
                'title' : "stats",
                "date": search_date_since,
                "company_name" : company_name
            });
        }
    });
}); 

var port = 3000; 
app.listen(port, () => {
    console.log(`Listening on port ${port}`); 
}); 