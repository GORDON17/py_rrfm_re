import actions from './ActionConsts';
import constants from '../utils/constants';

export function initDashboard() {
	console.log('init dashboard data ... ')
	return dispatch => {
		dispatch(getCountData());
		dispatch(getTicketPriceData());
		dispatch(getCategoryPriceData());
	};
}

export function receiveCount(monthCount) {
	return {
		type: actions.RECEIVE_COUNT,
		monthCount
	};
}

function getCountData() {
	return dispatch => 
		fetch(constants.API_URI + 'api/v4/re/month-count', {
			method: 'get',
			headers: {
				'HTTP_X_IVY_SESSION_TOKEN': constants.RAILS_TOKEN
			}
		})
			.then(response => response.json())
			.then(json => dispatch(receiveCount(json)))
}

export function receiveTicketPrice(ticketPrices) {
	return {
		type: actions.RECEIVE_PRICE,
		ticketPrices
	};
}

function getTicketPriceData() {
	return dispatch => 
		fetch(constants.API_URI + 'api/v4/re/ticket-prices', {
			method: 'get',
			headers: {
				'HTTP_X_IVY_SESSION_TOKEN': constants.RAILS_TOKEN
			}
		})
			.then(response => response.json())
			.then(json => dispatch(receiveTicketPrice(json)))
}

export function receiveCategoryPrice(categoryPrices) {
	return {
		type: actions.RECEIVE_CATEGORY,
		categoryPrices
	};
}

function getCategoryPriceData() {
	return dispatch => 
		fetch(constants.API_URI + 'api/v4/re/category-prices', {
			method: 'get',
			headers: {
				'HTTP_X_IVY_SESSION_TOKEN': constants.RAILS_TOKEN
			}
		})
			.then(response => response.json())
			.then(json => dispatch(receiveCategoryPrice(json)))
}