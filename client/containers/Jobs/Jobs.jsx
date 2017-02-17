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
            <div className="card">
              <div className="card-header card-header-icon" data-background-color="purple">
                  <i className="material-icons">assignment</i>
              </div>


              <div className="card-content">
                <h4 className="card-title">Jobs Manager</h4>
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
