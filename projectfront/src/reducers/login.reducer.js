import { LOGIN } from '../actions/user.actions';

const initialState = {};

export default function(state = initialState, action){
    switch (action.type) {

        case LOGIN:
            return {
                ...state,
                userToken: action.payload
            }
        default:
            return state;
    }
}