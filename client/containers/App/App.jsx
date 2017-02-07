import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

import SideBar from '../SideBar/SideBar';
import Footer from '../Footer/Footer';
import NavBar from '../NavBar/NavBar';

class App extends Component {
  componentDidMount() {
    /* init data from remote api here, dispatch init actions */
    
  }

  render() {
    return (
      <div className="wrapper">
        <SideBar></SideBar>
        <div className="main-panel">
          <NavBar></NavBar>
          <div id="main-content" className="content">
            {this.props.children}
          </div>
          <Footer></Footer>
        </div>
      </div>
    );
  }
}

/* Pass state to its component here */
function mapStateToProps(state) {
  return {
    
  };
}

// /* Map actions here */
// // canvasActions: bindActionCreators(CanvasActions, dispatch)
// function mapDispatchToProps(dispatch) {
//   return {
    
//   };
// }

App.propTypes = {
  dispatch: PropTypes.func.isRequired
}

export default connect(
  mapStateToProps
  // mapStateToProps,
  // mapDispatchToProps
)(App);
