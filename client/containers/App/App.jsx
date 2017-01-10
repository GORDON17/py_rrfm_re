import React, { Component } from 'react';
// import Kittens from '../components/Kittens';   //?????????
import { connect } from 'react-redux';

class App extends Component {
  componentDidMount() {
    /* init data here */
  }

  render() {
    return (
      <div className="index">
        <h1>Hello world!</h1>
      </div>
    );
  }
}

/* Pass state to its component here */
function mapStateToProps(state) {
  return {
    
  };
}

/* Map actions here */
// canvasActions: bindActionCreators(CanvasActions, dispatch)
function mapDispatchToProps(dispatch) {
  return {
    
  };
}



export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App);
