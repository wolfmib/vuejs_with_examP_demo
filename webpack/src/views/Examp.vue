<template>
  <div> 
    <h1>This is an Exam{{my_message}} page 🦜... </h1>	
    <p> Just Type the examp/1, examp/2 for each questions ...✍️<p>
    <!--
    <p> Original ID {{ $route.params.id}} </p>
    <p> Data:       {{ my_message }} </p>
    <p> CurrentID   {{ current_id }} -->
    <hr>
    <div>
    <b-container fluid class="p-4 bg-dark">
      <b-row>
        <b-col>
 <b-img alt="left image" fluid-grow :src="require(`../assets/examp_${my_message}.jpg`)"></b-img>
        </b-col>
      </b-row>  
      <b-row>
        <hr>
      </b-row>
      <b-row>
        <b-col>
             <b-img alt="left image" fluid-grow :src="require(`../assets/result_${my_message}.jpg`)"></b-img>
        </b-col>
      </b-row>  
    </b-container>
    </div>

  </div>
</template>
<script>





export default {
  data: function(){
    return {
      current_id: 0,
      image_path: "../assets/examp.jpg",
      pics: [
        {message: "examp" },
        {message: "examp_01"}
      ]
    }
  },

  mounted(){
    console.log("halljfwojfio")

  },

  /*
  methods: {
    getImgUrl(input_name){
      input_name = "examp"
      var images = require.context('../assets/',input_name ,/\.jpg$/)
      console.log("images", images)
      return images
    }
  },
  */

  computed:{
    my_message: function(){
      return this.$route.params.id
    },

    myPath(){
      return "../assets/examp" + this.current_id + ".jpg"
    }
  },
  
  watch: {
    my_message (){
      this.current_id = this.$route.params.id
    }
  }
}
</script>