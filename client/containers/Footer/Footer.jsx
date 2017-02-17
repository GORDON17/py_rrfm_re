import React, { Component } from 'react';
import { connect } from 'react-redux';

class Footer extends Component {
  componentDidMount() {
    /* init data here */
  }

  render() {
    return (
      <footer className="footer-sm-white">
        <div className="container-fluid">
          <p className="copyright pull-right">
              © 2017 <a href="https://www.ivy.com/" style={{'color': '#FFDF00'}}>IVY</a>
          </p>
        </div>
      </footer>
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
)(Footer);
