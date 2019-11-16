import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Home from './Components/Home';
import SecondPage from './Components/SecondPage';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.render(<Home />, div);
  ReactDOM.render(<SecondPage />, div);
  ReactDOM.unmountComponentAtNode(div);
});
