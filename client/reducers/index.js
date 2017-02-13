import { combineReducers } from 'redux';
import jobsReducer from './JobsReducer';
import dashboardReducer from './DashboardReducer';

const reducers = combineReducers({
  jobsReducer,
  dashboardReducer
});

export default reducers;
