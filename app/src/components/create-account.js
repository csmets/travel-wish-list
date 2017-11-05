export default {
  name: 'createAccount',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    create_account: (user, pass) => {
      const post = {
        username: user,
        password: pass,
      };

      const init = {
        method: 'POST',
        body: JSON.stringify(post),
      };

      fetch('http://localhost:8000/users/add', init).then((resp) => {
        const status = resp.status;

        if (status === 200) {
          window.location.href = '/';
        }
      })
      .catch((error) => { console.log(error); });
    },
  },
};
