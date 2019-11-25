const Routes = require('../routes');
const assert = require('chai').assert;


var Request = {};
var Response =  {
    viewName: ""
    ,data : {}
    ,render: function(view, viewData){
        this.viewName = view;
        this.data = viewData;
    }
};
describe('Routing', function(){
    it("should provide the title and the home view name", function(){
        var obj = Routes.home(Request, Response);
        assert.equal(Response.viewName, "home");
    });
});

describe('Routing', function(){
    it("should provide the title and the notFound view name", function(){
        var obj = Routes.notFound(Request, Response);
        assert.equal(Response.viewName, "notFound");
    });
});

describe('Routing', function(){
    it("should provide the title and the stats view name", function(){
        var obj = Routes.stats(Request, Response);
        assert.equal(Response.viewName, "stats");
    });
});


