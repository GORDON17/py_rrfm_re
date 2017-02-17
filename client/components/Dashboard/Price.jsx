import React, { PropTypes } from 'react';
import { ComposedChart, Bar, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Price = ({ data }) => (
  <ResponsiveContainer height={450}>
    <ComposedChart data={data}
            margin={{top: 20, right: 50, left: 10, bottom: 5}}>
      <XAxis dataKey="ticket_price" label="Price" type="category"/>
      <YAxis/>
      <Tooltip/>
      <CartesianGrid stroke='#f5f5f5' vertical={false} y={10}/>
      <Bar dataKey="ticket_price" name="Ticket Price" stackId="a" fill="#009688" />
      <Bar dataKey="rsvp_count" name="RSVP Count" stackId="a" fill="#FF9800" />
      <Line type='monotone' name="Rate of Attendance" dataKey="rate_of_attendence" stroke="#C51162" />
      <Legend />
    </ComposedChart>
  </ResponsiveContainer>
);

Price.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    ticket_price: PropTypes.number.isRequired,
    rsvp_count: PropTypes.number.isRequired,
    event_count: PropTypes.number.isRequired,
    rate_of_attendence: PropTypes.number.isRequired
  })).isRequired
};

export default Price;