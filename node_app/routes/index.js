exports.home = (req, res) => {
   res.render('home', {
      title: 'Home Page', 
   }); 
};

exports.stats = (req, res) => {
    res.render('stats', {
        title: 'Statistics'
    })
}; 

exports.notFound = (req, res) => {
    res.render('notFound', {
        title: 'Page Not Found'
    }); 
}; 