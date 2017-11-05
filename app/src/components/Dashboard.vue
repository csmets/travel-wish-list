<template>
  <main>
    <div class="container">
      <div class="row">
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
            <select id="city" class="form-control">
              <option v-for="city in cities.items" :value="city.name">{{ city.name }}</option>
            </select>
          </div>
        </div>
        <div class="col-md-2 d-flex align-items-center">
          <button id="submit-travel" class="btn btn-primary">Add</button>
        </div>
      </div>
    </div>
  </main>
</template>

<script src="./Dashboard.js"></script>
