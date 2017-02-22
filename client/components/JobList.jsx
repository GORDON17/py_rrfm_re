import React, { PropTypes } from 'react'
import JobItem from './JobItem'

const JobList = ({ jobs }) => (
  <table id="datatables" className="table table-striped table-no-bordered table-hover dataTable dtr-inline scroll-inner" cellSpacing="0" width="100%" style={{'width': '100%'}}>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>State</th>
        <th>Duration</th>
        <th>Created At</th>
        <th>Ended At</th>
        <th className="disabled-sorting text-right">Actions</th>
      </tr>
    </thead>
    {/*<tfoot>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>State</th>
        <th>Duration</th>
        <th>Created At</th>
        <th>Ended At</th>
        <th className="text-right">Actions</th>
      </tr>
    </tfoot>*/}
    <tbody> 
      {jobs.map( (job, index) =>
          <JobItem key={index} job={job} index={index} ></JobItem>
      )}
      <tr role="row" class="even">
        <td tabIndex="0" class="sorting_1">Colleen Hurst</td>
        <td>Javascript Developer</td>
        <td>San Francisco</td>
        <td>39</td>
        <td>2009/09/15</td>
        <td class="text-right">
          <a href="#" class="btn btn-simple btn-info btn-icon like"><i class="fa fa-heart"></i></a>
          <a href="#" class="btn btn-simple btn-warning btn-icon edit"><i class="fa fa-edit"></i></a>
          <a href="#" class="btn btn-simple btn-danger btn-icon remove"><i class="fa fa-times"></i></a>
        </td>
      </tr>
    </tbody>
  </table>
)

JobList.propTypes = {
  jobs: PropTypes.array.isRequired
}

export default JobList