import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import * as DashboardActions from '../../actions/DashboardActions';
import Count from '../../components/Dashboard/Count'
import Price from '../../components/Dashboard/Price'
import Category from '../../components/Dashboard/Category'

class Dashboard extends Component {
  componentDidMount() {
    /* init data here */
    this.props.DashboardActions.initDashboard();
  }

  _lastMonth(){
    const len = this.props.monthCount.length;
    const lastMonth = this.props.monthCount[len-2];
    return {
      rsvp: lastMonth ? lastMonth.rsvp_count : 0,
      registration: lastMonth ? lastMonth.month_count : 0
    }
  }

  _categoryFilter(event) {
    if (this.type == null && this.category == null) return true;

    return event != undefined && event.type == this.type && event.category == this.category;
  }

  render() {
    const {monthCount, ticketPrices, categoryPrices} = this.props;
    const lastMonth = this._lastMonth();
    const filterdCategory = categoryPrices.filter(this._categoryFilter, {type: 4, category: 4})

    return (
      <div className="container-fluid">
        <div className="header text-center" style={{'textAlign': 'center', 'fontWeight': 'bold'}}>
            <span>Good strategies will defeat every other opponent. Technologies change everything.</span>
        </div>
        <div className="row">
          <div className="col-md-12">
            <div className="card">
              <div className="card-header" data-background-color="rose">
                <i className="material-icons">insert_chart</i>
                <i className="card-title">Overall Registration and RSVP & Last Month State</i>
              </div>

              <div className="card-content scroll-outter"> 
                <div className="row">
                  <div className="ct-chart scroll-inner">
                    <div className="col-md-10">
                      <Count data={monthCount}></Count>
                    </div>
                    <div className="col-md-2">
                      <div className="row">
                        <div id="last-month" className="col-md-12">
                          <ul className="nav nav-pills nav-pills-icons nav-pills-info nav-stacked">
                            <li className="active">
                              <a href="#dashboard-2">
                                <div className="row">
                                  <h1 className="title">{lastMonth.registration}</h1>
                                  <h4 className="title">Registration</h4> 
                                </div>
                              </a>
                            </li>
                            <li className="active">
                                <a href="#schedule-2">
                                <div className="row">
                                  <h1 className="title">{lastMonth.rsvp}</h1>
                                  <h4 className="title">RSVP</h4> 
                                </div>
                                </a>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="notes">
                    <ul>Strategies: 
                      <li>3,4,5,9,10,11 are better to create more events. 6,7,8 are too hot? 12,1,2 are too cold?! come up a strategy to solve the issues.</li> 
                      <li>Push more ADs in 6,12.</li> 
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-md-12">
            <div className="card">
              <div className="card-header" data-background-color="rose">
                <i className="material-icons">insert_chart</i>
                <i className="card-title">Overall Ticket Prices</i>
              </div>
              {/*<div className="card-content">
                  <h4 className="card-title">Ticket Prices
                      <small> - Overall</small>
                  </h4>
              </div>*/}
              <div className="content scroll-outter">  
                <div className="ct-chart scroll-inner">
                  <Price data={ticketPrices}></Price>
                  <div className="notes">
                    <ul>Strategies: 
                      <li>Optimize the price strategy.</li> 
                      <li>Avoid the bad prices such as 55,65 because 60 is better.</li> 
                      <li>The rate of attendence is better when it is higher. Need more analysis based on the costs and profit.</li> 
                      <li>The price of social talk events are better at 80 rather than 75.</li> 
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="row">
          <div className="col-md-12">
            <div className="card">
              <div className="card-header" data-background-color="rose">
                <i className="material-icons">insert_chart</i>
                <i className="card-title">Category Prices</i>
              </div>
              {/*<div className="card-content">
                  <h4 className="card-title">Ticket Prices
                      <small> - Overall</small>
                  </h4>
              </div>*/}
              <div className="content scroll-outter">  
                <div className="ct-chart scroll-inner">
                  <Category data={filterdCategory}></Category>
                  <div className="notes">
                    <ul>Strategies: 
                      <li>probably 80 is the best price choice.</li> 
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

Dashboard.propTypes = {
  monthCount: PropTypes.arrayOf(PropTypes.shape({
    date: PropTypes.string.isRequired,
    month_count: PropTypes.number.isRequired,
    rsvp_count: PropTypes.number.isRequired
  })).isRequired,
  ticketPrices: PropTypes.array,
  categoryPrices: PropTypes.array
}

/* Pass state to its component here */
function mapStateToProps(state) {
  return {
    monthCount: state.dashboardReducer.monthCount,
    ticketPrices: state.dashboardReducer.ticketPrices,
    categoryPrices: state.dashboardReducer.categoryPrices
  };
}

/* Map actions here */
// canvasActions: bindActionCreators(CanvasActions, dispatch)
function mapDispatchToProps(dispatch) {
  return {
    DashboardActions: bindActionCreators(DashboardActions, dispatch)
  };
}



export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Dashboard);
