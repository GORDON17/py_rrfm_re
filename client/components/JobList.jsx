import React, { PropTypes } from 'react'
import JobItem from './JobItem'

const JobList = ({ jobs }) => (
  <table id="datatables" className="table table-striped table-no-bordered table-hover dataTable dtr-inline" cellSpacing="0" width="100%" style={{'width': '100%', 'overflowX': 'scroll'}} role="grid">
    <thead>
      <tr role="row">
      <th className="sorting_asc" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '30px'}} aria-sort="ascending">ID</th>
      <th className="sorting" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '200px'}} >Name</th>
      <th className="sorting" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '50px'}} >State</th>
      <th className="sorting" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '100px'}} >Duration</th>
      <th className="sorting" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '250px'}} >Created At</th>
      <th className="sorting" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '250px'}} >Ended At</th>
      <th className="disabled-sorting text-right sorting" tabIndex="0" aria-controls="datatables" rowSpan="1" colSpan="1" style={{'width': '138px'}} >Actions</th>
      </tr>
    </thead>
    {/*<tfoot>
      <tr>
        <th rowSpan="1" colSpan="1">ID</th>
        <th rowSpan="1" colSpan="1">Name</th>
        <th rowSpan="1" colSpan="1">State</th>
        <th rowSpan="1" colSpan="1">Duration</th>
        <th rowSpan="1" colSpan="1">Created At</th>
        <th rowSpan="1" colSpan="1">Ended At</th>
        <th className="text-right" rowSpan="1" colSpan="1">Actions</th>
      </tr>
    </tfoot>*/}
    <tbody> 
      {jobs.map( (job, index) => 
        <JobItem key={index} job={job} index={index} ></JobItem>
      )}
      {/*<tr role="row" class="even">
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
      </tr>*/}
    </tbody>
  </table>
)

JobList.propTypes = {
  jobs: PropTypes.array.isRequired
}

export default JobList