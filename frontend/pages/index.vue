<template>
<div class="container-fluid">

<h1>Home</h1>

<p>Toto je obsah</p>
<p>Toto je obsah</p>
<p>Toto je obsah</p>
<p>Toto je obsah</p>

<p>Toto je  obsah </p>
  
</div>
</template>

<style>
</style>

<script>
/*import axios from "axios";*/

export default {
  head() {
    return {
      title: "miniSaurus",
    };
  },

  data() {
    return {
        a :'ahoj',
        pozdrav: '',
    }
  },
  methods: {

    async fetchStart() {
        const data = await this.$axios.$get('/api/start.json')
        console.log(data);
        this.pozdrav = data.data;
    },

  },

  mounted() {
    /*axios.get('/api/start.json')*/
    /*    .then(function (response) {*/
    /*      // handle success*/
    /*      console.log('ahoj');*/
    /*      console.log(response);*/
    /*    });*/
  }, 


};



</script>


