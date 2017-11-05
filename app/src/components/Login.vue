<template>
  <div v-if="showCreateForm">
    <create-account></create-account>
  </div>
  <div v-else>
    <div class="container">
      <form class="form-horizontal" role="form">
        <div class="row">
          <div class="col-md-3"></div>
          <div class="col-md-6">
            <h2>Login to Travel Wish List</h2>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-md-3"></div>
          <div class="col-md-6">
            <div class="form-group">
              <label class="sr-only" for="username">Username</label>
              <div class="input-group mb-2 mr-sm-2 mb-sm-0">
                <div class="input-group-addon" style="width: 2.6rem"><i class="fa fa-user" aria-hidden="true"></i></div>
                <input type="text" v-model="username" class="form-control" id="username" placeholder="username" required autofocus>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="form-control-feedback invisible">
              <span class="text-danger align-middle">
                <i class="fa fa-close"></i> Username required
              </span>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-3"></div>
          <div class="col-md-6">
            <div class="form-group">
              <label class="sr-only" for="password">Password</label>
              <div class="input-group mb-2 mr-sm-2 mb-sm-0">
                <div class="input-group-addon" style="width: 2.6rem"><i class="fa fa-key" aria-hidden="true"></i></div>
                <input type="password" v-model="password" class="form-control" id="password" placeholder="Password" required>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="form-control-feedback invisible">
              <span class="text-danger align-middle">
                <i class="fa fa-close"></i> Password required
              </span>
            </div>
          </div>
        </div>
        <div v-if="showError.value" class="row">
          <div class="col-md-3"></div>
          <div class="col-md-6">
            <div class="alert alert-danger">Invalid login details</div>
          </div>
          <div class="col-md-3"></div>
        </div>
        <div class="row" style="padding-top: 1rem">
          <div class="col-md-3"></div>
          <div class="col-md-6">
            <button class="btn btn-success" @click="login(username, password)" @keyup.enter="login(username, password)"><i class="fa fa-sign-in"></i> Login</button>
            <a href="#" @click="showCreateForm=true">Create account</a>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script src="./Login.js"></script>
