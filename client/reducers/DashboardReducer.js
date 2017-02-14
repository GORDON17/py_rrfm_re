import actions from '../actions/ActionConsts';

const initState = {
	monthCount: [],
	ticketPrices: [],
	categoryPrices: []
}

export default function dashboardReducer(state=initState, action) {
	switch(action.type) {
		case actions.RECEIVE_COUNT:
			return Object.assign({}, state, {
				monthCount: action.monthCount
			});
		case actions.RECEIVE_PRICE:
			return Object.assign({}, state, {
				ticketPrices: action.ticketPrices
			});
		case actions.RECEIVE_CATEGORY:
			return Object.assign({}, state, {
				categoryPrices: action.categoryPrices
			});
		default:
			return state;
	}
}