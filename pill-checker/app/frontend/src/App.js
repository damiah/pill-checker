import React from 'react';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
        test: "sdfsd"
    };
  }

  componentDidMount() {
      fetch('api/')
          .then(response => response.json())
          // .then(response => this.setState({'test': response.test}))
  }

  render() {
    // return <h1>Hey!  It's {this.state}</h1>;
    return <h1>Hey!  It's </h1>;
  }

}

export default App;