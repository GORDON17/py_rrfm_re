import actions from './ActionConsts';

export function initDashboard() {
	console.log('init dashboard data ... ')
	return dispatch => {
		dispatch(getCountData());
		dispatch(getTicketPriceData());
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
		fetch('http://0.0.0.0:3000/api/v4/re/month-count')//('api/dashboard/month-count')
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
		fetch('http://local.ivy.com:3000/api/v4/re/ticket-prices')
			.then(response => response.json())
			.then(json => dispatch(receiveTicketPrice(json)))
}
