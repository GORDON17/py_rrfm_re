import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router';

import sidebarBGI from '../../../assets/img/full-screen-image-3.jpg';
import ivyLogo from '../../../assets/img/ivy-logo.png';

class SideBar extends Component {
  componentDidMount() {
    /* init data here */

    $(".nav a").on("click", function(){
      $(".nav").find(".active").removeClass("active");
      $(this).parent().addClass("active");
    });
  }

  render() {
    return (
      <div className="sidebar" data-color="black">
        {/*<div className="logo">
          <img className="logo-image" src={ivyLogo} alt="Logo"/>
          <a href="http://www.ivy.com" className="logo-text" style={{'textAlign': 'left'}}>
              IVY
          </a>
        </div>
        <div className="logo logo-mini">
          <a href="http://www.ivy.com" className="logo-text">
              <img className="logo-image" src={ivyLogo} alt="Logo" style={{'float':'none'}}/>
          </a>
        </div>*/}
        <div className="sidebar-wrapper">
          <div className="user">
                <div className="photo">
                    <img src={ivyLogo}/>
                </div>
                <div className="info">
                    <a data-toggle="collapse" href="http://www.ivy.com" className="collapsed">
                        <span style={{'fontSize': '1.5em'}}>IVY</span>
                    </a>
                </div>
            </div>
          <ul className="nav">
            <li className="active">
              <Link to="/">
                <i className="pe-7s-graph"></i>
                <p>Dashboard</p>
              </Link>
            </li>

            <li>
              <Link to="/jobs">
                <i className="pe-7s-alarm"></i>
                <p>Jobs</p>
              </Link>
            </li>

            <li>
              <Link to="/">
                <i className="pe-7s-graph1"></i>
                <p>Charts</p>
              </Link>
            </li>

          </ul>
        </div>
        <div className="sidebar-background" style={{'backgroundImage': 'url(' + sidebarBGI+ ')'}}></div>
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
)(SideBar);
