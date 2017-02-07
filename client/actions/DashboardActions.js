import actions from './ActionConsts';

export function initDashboard() {
	return dispatch => {
		dispatch(getMonthCountData());
	};
}

function getMonthCountData() {
	return dispatch => 
		fetch()
			.then()
			.then()
}