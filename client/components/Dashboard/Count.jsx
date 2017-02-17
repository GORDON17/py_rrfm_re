import React, { PropTypes } from 'react';
import { ComposedChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Count = ({ data }) => (
  <ResponsiveContainer height={450}>
    <ComposedChart data={data}
                    margin={{top: 20, right: 50, bottom: 25, left: 10}}>
      <XAxis dataKey="date" label="Date"/>
      <YAxis />
      <Tooltip/>
      <CartesianGrid stroke='#f5f5f5'/>
      <Bar dataKey='month_count' fill='#00BCD4' name="Total Reg"/>
      <Bar dataKey='rsvp_count' fill='#E91E63' name="Total RSVP"/>
      <Legend/>
    </ComposedChart>
  </ResponsiveContainer>
);

Count.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    date: PropTypes.string.isRequired,
    month_count: PropTypes.number.isRequired,
    rsvp_count: PropTypes.number.isRequired
  })).isRequired
};

export default Count;