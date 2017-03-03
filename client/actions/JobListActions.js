import actions from './ActionConsts';

export function initJobs() {
	console.log('init jobs')
  return dispatch => {
    return dispatch(getJobs());
  }
}

function getJobs() {
	return dispatch => 
		fetch("api/job/list")
			.then(response =>	response.json() )
			.then(json => dispatch(receiveJobs(json)) )
}

export function receiveJobs(jobs) {
	console.log('receiving jobs ...');
	return {
		type: actions.RECEIVE_JOBS,
		jobs
	};
}