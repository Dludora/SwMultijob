import Cookie from 'js-cookie'
export default {
    state: {
        token: '',
        avatar: '',
    },
    mutations: {
        setToken(state, val) {
            state.token = val
            Cookie.set('token', val)
        },
        clearToken(state) {
            state.token = ''
            Cookie.remove('token')
        },
        getToken(state) {
            state.token = state.token || Cookie.get('token')
        },
        setAvatar(state, val) {
            state.avatar = val
            // Cookie.set('token', val)
        }
    }
}