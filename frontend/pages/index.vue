<template>
  <div class="container-fluid jumbotron-fluid jumbo">
    <!-- Pokud chci předat pouze hodnotu použiji abc="neco" v našem případě string "neco"
    :abc by se použilo pokud bych chtěl poslat nejaký výraz/proměnou. Např. kdyby "neco" byla definována v data
    : je vlastně jen zkratka pro v-bind:
    -->
    <Logo abc="neco"/>
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
