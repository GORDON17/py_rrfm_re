import actions from '../actions/ActionConsts';

const initialState = {
  jobs: []
};

export default function jobsReducer(state = initialState, action) {
	switch (action.type) {
		case actions.RECEIVE_JOBS:
			return Object.assign({}, state, {
        jobs: action.jobs
      });
    default:
    	return state;
	}
}