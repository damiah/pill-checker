import React from 'react';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      records: []
    };
  }

  componentDidMount() {
      fetch('api/')
          .then(response => response.json())
          .then(records => this.setState({records: records}))
          .catch(error => console.log(error))
  }

  render() {
    return <h1>Hey!  It's {this.state}</h1>;
    // return <h1>Hey!  It's mess </h1>;
  }

}

export default App;