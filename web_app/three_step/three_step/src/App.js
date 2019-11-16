import React, {Component} from 'react';
import Navbar from './Components/Navbar'
import { BrowserRouter, Route, Switch} from 'react-router-dom'
import Home from './Components/Home'
import Second from './Components/SecondPage'

class App extends Component {
  render(){
    return (
      <BrowserRouter>
        <div className="App">
        <Navbar />
        <Switch>
        <Route exact path='/' component={Home}/>
        <Route path='/second' component={Second}/>
        </Switch>
        </div>
      </BrowserRouter>
    );
  }

}

export default App;
