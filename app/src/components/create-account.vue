<template>
  <div class="container">
    <form class="form-horizontal" role="form">
      <div class="row">
        <div class="col-md-3"></div>
        <div class="col-md-6">
          <h2>Create Account</h2>
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
      <div class="row" style="padding-top: 1rem">
        <div class="col-md-3"></div>
        <div class="col-md-6">
          <button class="btn btn-success" @click="create_account(username, password)" @keyup.enter="create_account(username, password)"><i class="fa fa-sign-in"></i> Create</button>
          <a href="/">Back to login</a>
        </div>
      </div>
    </form>
  </div>
</template>

<script src="./create-account.js"></script>
