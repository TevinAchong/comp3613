const {exec} = require('child_process'); 

var company_name = 'apple'; 
var search_date_since = '01-02-2019'; 

if (process.platform === 'win32' || process.platform === 'win64') {
    exec(`python ..\bin\main.py`, (err, stdout, stderr) => {
        if (err) {
            console.error(err)
        }
        else {
            console.log(`stdout: ${stdout}`); 
            console.log(`stderr: ${stderr}`); 
        }
    }); 
}
else {
    exec(
        `python3 ../bin/main.py --company-name ${company_name} --search-date-since ${search_date_since}`,
        (err, stdout, stderr) => {
        if (err) {
            console.error(err)
        }
        else {
            console.log(`stdout: ${stdout}`); 
            console.log(`stderr: ${stderr}`); 
        }
    });  
}