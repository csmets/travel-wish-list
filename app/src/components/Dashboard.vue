<template>
  <main>
    <topbar></topbar>

    <div v-if="cookieExists()">

      <div class="container">
        <div class="row">
          <div class="col-md-12 text-right">
            <p>Hello, <strong>{{ user.name }}!</strong> <a href="#" @click="logout()">Logout</a></p>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h2>Make Travel Request</h2>
          </div>
          <div class="col-md-5">
            <div class="form-group">
              <label for="country">Country</label>
              <select id="country" class="form-control" v-model="countrySelect" @change="getCities(countrySelect)">
                <option v-for="country in countries.items" :value="country.name">{{ country.name }}</option>
              </select>
            </div>
          </div>
          <div class="col-md-5">
            <div class="form-group">
              <label for="city">City</label>
              <select id="city" class="form-control" v-model="citySelect">
                <option v-for="city in cities.items" :value="city.name">{{ city.name }}</option>
              </select>
            </div>
          </div>
          <div class="col-md-2 d-flex align-items-center">
            <button class="btn btn-primary" @click="addTravel(countrySelect, citySelect)">Add</button>
          </div>
        </div>
      </div>

      <div class="container mt-5">
        <h2>Travel Requests</h2>

        <table class="table table-hover">
          <thead>
            <tr>
              <th>City</th>
              <th>Country</th>
              <th>User</th>
              <th>Votes</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="travel in travels.items">
              <td>{{ travel.city }}</td>
              <td>{{ travel.country }}</td>
              <td>{{ travel.user }}</td>
              <td>{{ travel.votes }}</td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
    <div v-else>
      <login-screen></login-screen>
    </div>
  </main>
</template>

<script src="./Dashboard.js"></script>
