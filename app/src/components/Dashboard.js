import Login from '@/components/Login.vue';
import topbar from '@/components/topbar';
import cookie from '@/utils/cookie';


const countries = {
  values: {
    items: [],
  },

  fetch() {
    fetch('http://localhost:8000/countries').then((resp) => {
      const contentType = resp.headers.get('content-type');

      if (contentType && contentType.includes('application/json')) {
        return resp.json();
      }
      throw new TypeError('Expected JSON');
    })
    .then((json) => {
      this.values.items = json;
    })
    .catch((error) => { console.log(error); });
  },
};


const cities = {
  values: {
    items: [],
  },

  fetch(country) {
    fetch(`http://localhost:8000/country/${country}/city/all`).then((resp) => {
      const contentType = resp.headers.get('content-type');

      if (contentType && contentType.includes('application/json')) {
        return resp.json();
      }
      throw new TypeError('Expected JSON');
    })
    .then((json) => {
      this.values.items = json;
    })
    .catch((error) => { console.log(error); });
  },
};


const user = {
  values: {
    name: '',
  },
};


const travels = {
  values: {
    items: [],
  },

  fetch() {
    fetch('http://localhost:8000/travels').then((resp) => {
      const contentType = resp.headers.get('content-type');

      if (contentType && contentType.includes('application/json')) {
        return resp.json();
      }
      throw new TypeError('Expected JSON');
    })
    .then((json) => {
      this.values.items = json;
    })
    .catch((error) => { console.log(error); });
  },
};


export default {
  name: 'Dashboard',

  components: {
    'login-screen': Login,
    topbar,
  },

  data() {
    return {
      countries: countries.values,
      cities: cities.values,
      countrySelect: '',
      citySelect: '',
      user: user.values,
      travels: travels.values,
    };
  },

  created() {
    countries.fetch();
    travels.fetch();
  },

  methods: {

    getCities: (country) => {
      cities.fetch(country);
    },

    cookieExists: () => {
      if (cookie.getCookie('username') !== '') {
        user.values.name = cookie.getCookie('username');
        return true;
      }

      return false;
    },

    addTravel: (country, city) => {
      const username = cookie.getCookie('username');

      const post = {
        country,
        city,
        username,
      };

      const init = {
        method: 'POST',
        body: JSON.stringify(post),
      };

      fetch('http://localhost:8000/travel', init).then((resp) => {
        const status = resp.status;

        if (status === 200) {
          travels.fetch();
        }
      })
      .catch((error) => { console.log(error); });
    },

    logout: () => {
      document.cookie = document.cookie + ';expires=Thu, 01 Jan 1970 00:00:01 GMT';
      window.location.href = '/';
    },
  },
};
