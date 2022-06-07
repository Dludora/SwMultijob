import Cookie from 'js-cookie'
export default {
    state: {
        menu: []
    },
    mutations: {
        setMenu(state, val) {
            state.menu = val;
            Cookie.set('menu', JSON.stringify(val));
        },
        deleteMenu(state, val) {

        },
        addMenu(state, val) {
            if(!Cookie.get('menu')) {
                return
            }
            const menu = JSON.parse(Cookie.get('menu'))
            state.menu = menu
            const menuArray = []
            menu.forEach(item => {

            })
        }
    }

}