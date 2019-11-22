const Routes = require('../routes');
const assert = require('chai').assert;
//const should = require("should");

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
    it("should provide the title and the index view name", function(){
        var obj = Routes.home(Request, Response);
        assert.equal(Response.viewName, "home");
    });
});

describe('Routing', function(){
    it("should provide the title and the index view name", function(){
        var obj = Routes.notFound(Request, Response);
        assert.equal(Response.viewName, "notFound");
    });
});

describe('Routing', function(){
    it("should provide the title and the index view name", function(){
        var obj = Routes.stats(Request, Response);
        assert.equal(Response.viewName, "stats");
    });
});
// describe("Routing", function(){
//     describe("Default Route", function(){
//         it("should provide the title and the index view name", function(){
//             Routes.home(Request, Response);
//             Response.viewName.should.equal("home"); 
//         });
//     });
// });


