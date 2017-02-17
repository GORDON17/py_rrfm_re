import React, { PropTypes } from 'react';
import { ComposedChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Category = ({ data }) => (
  <ResponsiveContainer height={450}>
    <ComposedChart data={data}
            margin={{top: 20, right: 50, left: 10, bottom: 5}}>
      <XAxis dataKey="price" label="Price"/>
      <YAxis/>
      <Tooltip/>
      <CartesianGrid stroke='#f5f5f5' vertical={false} y={10}/>
      <Line type='monotone' name="Rate of Attendance" dataKey="rate_of_attendence" stroke="#311B92" />
      <Legend />
    </ComposedChart>
  </ResponsiveContainer>
);

Category.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    type: PropTypes.number.isRequired,
    category: PropTypes.number.isRequired,
    price: PropTypes.number.isRequired,
    rsvp_count: PropTypes.number.isRequired,
    event_count: PropTypes.number.isRequired,
    rate_of_attendence: PropTypes.number.isRequired
  })).isRequired
};

export default Category;