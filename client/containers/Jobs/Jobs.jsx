import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import JobList from '../../components/JobList';
import * as JobActions from '../../actions/JobListActions';

class Jobs extends Component {
  componentDidMount() {
    /* init data here */
    this.props.JobActions.initJobs();
  }

  render() {
    const jobs = this.props.jobs;

    return (
      <div className="container-fluid">
        <div className="row">
          <div className="col-md-12">
            <div id="job-table" className="card">
              <div className="card-header card-header-icon" data-background-color="purple">
                  <i className="material-icons">assignment</i>
              </div>


              <div className="card-content">
                <div className="card-action-title">
                <h4 className="card-title">Jobs Manager</h4>
                <button className="btn btn-success btn-sm" data-toggle="modal" data-target="#jobCreateModel">
                  <i className="fa fa-plus-square-o"></i>
                </button>
                </div>
                <div className="material-datatables">
                  <div id="datatables_wrapper" className="dataTables_wrapper form-inline dt-bootstrap">
                    <div className="row">
                      <div className="col-sm-12 scroll-outter">
                        <JobList jobs={jobs}></JobList>
                      </div>
                    </div>
                  {/*<div class="row">
                  <div class="col-sm-5">
                  <div class="dataTables_info" id="datatables_info" role="status" aria-live="polite">Showing 1 to 10 of 40 entries</div>
                  </div>
                  <div class="col-sm-7">
                  <div class="dataTables_paginate paging_full_numbers" id="datatables_paginate">
                  <ul class="pagination">
                  <li class="paginate_button first disabled" id="datatables_first">
                  <a href="#" aria-controls="datatables" data-dt-idx="0" tabindex="0">First</a>
                  </li>
                  <li class="paginate_button previous disabled" id="datatables_previous">
                  <a href="#" aria-controls="datatables" data-dt-idx="1" tabindex="0">Previous</a>
                  </li>
                  <li class="paginate_button active">
                  <a href="#" aria-controls="datatables" data-dt-idx="2" tabindex="0">1</a></li><li class="paginate_button "><a href="#" aria-controls="datatables" data-dt-idx="3" tabindex="0">2</a></li><li class="paginate_button "><a href="#" aria-controls="datatables" data-dt-idx="4" tabindex="0">3</a></li><li class="paginate_button "><a href="#" aria-controls="datatables" data-dt-idx="5" tabindex="0">4</a></li><li class="paginate_button next" id="datatables_next"><a href="#" aria-controls="datatables" data-dt-idx="6" tabindex="0">Next</a></li><li class="paginate_button last" id="datatables_last"><a href="#" aria-controls="datatables" data-dt-idx="7" tabindex="0">Last</a></li></ul>
                  </div>
                  </div>
                  </div>*/}
                  </div>
                </div>
              </div>

              <div className="modal fade" id="jobCreateModel" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style={{'display': 'none'}}>
                <div className="modal-dialog">
                  <div className="modal-content">
                    <div className="modal-header">
                      <button type="button" className="close" data-dismiss="modal" aria-hidden="true">
                        <i className="material-icons">clear</i>
                      </button>
                      <h4 className="modal-title">Modal title</h4>
                    </div>
                    <div className="modal-body">
                      <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.
                      </p>
                    </div>
                    <div className="modal-footer">
                      <button type="button" className="btn btn-simple">Nice Button<div className="ripple-container"></div></button>
                      <button type="button" className="btn btn-danger btn-simple" data-dismiss="modal">Close<div className="ripple-container"><div className="ripple ripple-on ripple-out" style={{'left': '29.0781px', 'top': '20px', 'backgroundColor': 'rgb(244, 67, 54)', 'transform': 'scale(8.5)'}}></div><div className="ripple ripple-on ripple-out" style={{'left': '33.0781px', 'top': '29px', 'backgroundColor': 'rgb(244, 67, 54)', 'transform': 'scale(8.5)'}}></div></div></button>
                    </div>
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

Jobs.propTypes = {
  jobs: PropTypes.array,
  JobActions: PropTypes.object.isRequired
}

/* Pass state to its component here */
function mapStateToProps(state) {
  return {
    jobs: state.jobsReducer.jobs
  };
}

/* Map actions here */
// canvasActions: bindActionCreators(CanvasActions, dispatch)
function mapDispatchToProps(dispatch) {
  return {
    JobActions: bindActionCreators(JobActions, dispatch)
  };
}



export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Jobs);
