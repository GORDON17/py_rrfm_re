import React, { PropTypes } from 'react';
import { ComposedChart, Line, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const Map = ({ data }) => (
  <ComposedChart width={600} 
                  height={400} 
                  data={data}
                  margin={{top: 20, right: 20, bottom: 20, left: 20}}>
    <XAxis dataKey="month"/>
    <YAxis />
    <Tooltip/>
    <Legend/>
    <CartesianGrid stroke='#f5f5f5'/>
    <Bar dataKey='count' barSize={20} fill='#413ea0' name="Total Reg"/>
    <Line type='monotone' dataKey='uv' stroke='#ff7300'/>
  </ComposedChart>
);

Map.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    month: PropTypes.string.isRequired,
    count: PropTypes.number.isRequired
  })).isRequired
};

export default Map;