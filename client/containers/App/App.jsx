import React, { Component } from 'react';
import SideBar from '../SideBar/SideBar';
import Panel from '../Panel/Panel';

import { connect } from 'react-redux';

class App extends Component {
  componentDidMount() {
    /* init data here */
  }

  render() {
    return (
      <div className="wrapper">
        <SideBar></SideBar>
        <Panel></Panel>
        
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
