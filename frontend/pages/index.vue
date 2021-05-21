<template>
  <div class="container-fluid jumbotron-fluid jumbo">
    <Logo />
    <div class="row">
        <div class="col-3 gx-2">
            <h1>miniSaurus</h1>
            <p>nebuď mini, buď Saurus!</p>
        </div>
        <div class="col-9 gx-2">
            <img src="~/static/img/minisaurus.jpg" class="img-fluid"/>
        </div>
    </div>
    <div class="row">
      <div class="col-9 gx-2">
            <p> {{ a }} </p>
            <p> {{ rendering }} </p>
            <ul>
              <li> <NuxtLink to="/">Home page</NuxtLink> </li>
              <li> <NuxtLink to="/marek">Marek</NuxtLink> </li>
            </ul>
        </div>
    </div>
  </div>
</template>


<script>
export default {
  head() {
    return {
      title: "miniSaurus"
    };
  },

  data() {
    return {
        a :'ahoj'
    }
  },

  asyncData() {
    return {
      rendering: process.server ? 'server' : 'client'
    }
  },

};



</script>


<style>
.jumbo {
    background-color: lightgray;    
}

</style>
