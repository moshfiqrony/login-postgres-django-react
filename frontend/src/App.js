import React, { Component } from 'react';
import Form from './component/Form'
import Users from './component/Users'

class App extends Component {
  render() {
    return (
      <div>
        <Form/>
        <Users />
      </div>
    );
  }
}

export default App;
