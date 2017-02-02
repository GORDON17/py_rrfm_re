import React, { PropTypes } from 'react';

const JobItem = ({ job, index }) => (
  <tr role="row" key={index} className={ index % 2 == 0 ? "even" : "odd" }>
    <td tabIndex="0" className="sorting_1">{job.id}</td>
    <td>{job.name}</td>
    <td>{job.state}</td>
    <td>{job.duration}</td>
    <td>{job.created_at}</td>
    <td>{job.ended_at}</td>
    <td className="text-right">
      <a href="#" className="btn btn-simple btn-info btn-icon like"><i className="fa fa-heart"></i></a>
      <a href="#" className="btn btn-simple btn-warning btn-icon edit"><i className="fa fa-edit"></i></a>
      <a href="#" className="btn btn-simple btn-danger btn-icon remove"><i className="fa fa-times"></i></a>
    </td>
  </tr>
);

JobItem.propTypes = {
  job: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    state: PropTypes.number.isRequired,
    duration: PropTypes.number.isRequired,
    created_at: PropTypes.string.isRequired,
    ended_at: PropTypes.string.isRequired
  }),
  index: PropTypes.number.isRequired
};

export default JobItem;