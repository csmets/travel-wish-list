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

export default {
  name: 'Dashboard',
  data() {
    return {
      countries: countries.values,
      cities: cities.values,
      countrySelect: '',
    };
  },
  created() {
    countries.fetch();
  },
  methods: {
    getCities: (country) => {
      cities.fetch(country);
    },
  },
};
