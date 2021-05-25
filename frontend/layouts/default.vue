<template>
  <div>
    <div class="container-fluid jumbotron-fluid jumbo">
      <div class="row">
        <div class="col-md-3 gx-2">
          <h1>miniSaurus</h1>
          <p>nebuď mini, buď Saurus!</p>
          <p>a{{ start }}</p>
          <b-navbar class="gx-2" type="dark" variant="primary">
            <b-navbar-nav>
              <b-nav tabs>
                <b-nav-item to="/" exact-active-class="active">Home</b-nav-item>
                <b-nav-item to="/marek" exact-active-class="active">Marek</b-nav-item>
                <b-nav-item to="/lalala" exact-active-class="active">Lalala</b-nav-item>
              </b-nav>
            </b-navbar-nav>
          </b-navbar>
        </div>
        <div class="col-md-9 gx-2">
            <img src="~/static/img/minisaurus.jpg" class="img-fluid"/>
        </div>
      </div>
      <div class="row">
      </div>
    </div>
    <Nuxt />
  </div>
</template>

<style lang="scss">
.nuxt-link-active {
  font-weight: bold;
}
/* exact link will show the primary color for only the exact matching link */
a.nuxt-link-exact-active {
  color: #00c58e;
}


html {
  font-family:
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}
</style>

<script>
import axios from 'axios'
export default {

  data() {
    return {
      start: 'ahoj',
    }
  },

  async fetch() {
    const start = await this.$axios.$get('/api/start.json')
    this.start = start.data;
  },

};
  
</script>

