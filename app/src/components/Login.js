import CreateAccount from '@/components/create-account.vue';

const showErrorMessage = {
  value: false,
};

export default {
  name: 'Login',
  components: {
    'create-account': CreateAccount,
  },
  data() {
    return {
      username: '',
      password: '',
      showCreateForm: false,
      showError: showErrorMessage,
    };
  },
  methods: {
    login: (user, pass) => {
      const post = {
        username: user,
        password: pass,
      };

      const init = {
        method: 'POST',
        body: JSON.stringify(post),
      };

      fetch('http://localhost:8000/login', init).then((resp) => {
        const status = resp.status;

        if (status === 200) {
          document.cookie = `username=${user}`;
          window.location.href = '/';
          showErrorMessage.value = false;
        } else {
          showErrorMessage.value = true;
        }
      })
      .catch((error) => { console.log(error); });
    },
  },
};
