import actions from './ActionConsts';
import constants from '../utils/constants';

export function initJobs() {
	console.log('init jobs')
  return dispatch => {
    return dispatch(getJobs());
  }
}

function getJobs() {
	return dispatch => 
		fetch("api/job/list", {
			method: 'get',
			headers: {
				'Token': constants.RAILS_TOKEN
			}
		})
			.then(response =>	response.json() )
			.then(json => {
				if (json.status === 200) {
					dispatch(receiveJobs(json.data));
				} else {
					console.log('ERROR:', json.message);
				}
			})
}

export function receiveJobs(jobs) {
	console.log('receiving jobs ...');
	return {
		type: actions.RECEIVE_JOBS,
		jobs
	};
}