import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import * as DashboardActions from '../../actions/DashboardActions';
import Count from '../../components/Dashboard/Count'
import Price from '../../components/Dashboard/Price'

class Dashboard extends Component {
  componentDidMount() {
    /* init data here */
    this.props.DashboardActions.initDashboard();
  }

  render() {
    const {monthCount, ticketPrices, categoryPrices} = this.props;

    return (
      <div className="container-fluid">
        <div className="alert alert-success" style={{'textAlign': 'center', 'fontWeight': 'bold'}}>
            <span>Good strategies will defeat every other opponent. Technologies change everything.</span>
        </div>
        <div className="row">
          <div className="col-md-12">
            <div className="card">
              <div className="content">  
                <div className="row table-outter">
                  <Count data={monthCount}></Count>
                  <div className="notes">
                    <ul>Strategies: 
                      <li>3,4,5,9,10,11 are better to create more events. 6,7,8 are too hot? 12,1,2 are too cold?! come up a strategy to solve the issues.</li> 
                      <li>Push more ADs in 6,12.</li> 
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <div className="card">
              <div className="content">  
                <div className="row table-outter">
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
      </div>
    );
  }
}

Dashboard.propTypes = {
  monthCount: PropTypes.array,
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
