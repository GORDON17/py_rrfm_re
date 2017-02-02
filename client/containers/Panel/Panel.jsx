import React, { Component } from 'react';
import { connect } from 'react-redux';

import Footer from '../Footer/Footer';
import NavBar from '../NavBar/NavBar';
import Content from '../Content/Content';
class Panel extends Component {
  componentDidMount() {
    /* init data here */
  }

  render() {
    return (
      <div className="main-panel">
        <NavBar></NavBar>
        <Content></Content>
        <Footer></Footer>
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
)(Panel);
