<template>
  <div>
    <p>This is an Exam{{ my_message }} page 🦜...</p>
    <p></p>
    <p>Just Type the examp/1, examp/2 for each questions ...✍️</p>
    <p>
      <!--
    <p> Original ID {{ $route.params.id}} </p>
    <p> Data:       {{ my_message }} </p>
      <p> CurrentID   {{ current_id }}-->
    </p>
    <hr />
    <div>
      <!-- Main Photos  Here -->
      <b-container class="center">
        <b-row>
          <b-col sm="auto"></b-col>
          <b-col>
            <b-card
              overlay
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Card Image"
              text-variant="black"
              title="JA Examp Collections"
            ></b-card>
          </b-col>
          <b-col sm="auto"></b-col>
        </b-row>
        <b-row>
          <b-col></b-col>
          <b-col>
            <b-button
              href="https://github.com/wolfmib/vuejs_with_examP_demo"
              variant="primary"
              >Source Code on Github</b-button
            >
          </b-col>
          <b-col></b-col>
        </b-row>
      </b-container>
      <hr />

      <!-- Voice   Some other time...
      <b-container fluid class="p-4 bg-dark">
        <vue-audio
          :file="https://drive.google.com/file/d/1rNmREAvCjthEFosYDMTI00QNiwnQ8rib/view?usp=sharing"
        />
      </b-container>
      -->

      <!-- Main Content Questions and Draft here-->
      <b-container fluid class="p-4 bg-dark">
        <b-row>
          <b-col sm="auto"></b-col>
          <b-col>
            <b-tabs content-class="mt-3">
              <b-tab title="Questions" active>
                <b-img
                  alt="left image"
                  fluid-grow
                  :src="require(`../assets/examp_${my_message}.jpg`)"
                ></b-img>
              </b-tab>
              <b-tab title="Draft Solution">
                <b-img
                  alt="left image"
                  fluid-grow
                  :src="require(`../assets/result_${my_message}.jpg`)"
                ></b-img>
              </b-tab>
              <b-tab title="Disabled" disabled>
                <p>I'm a disabled tab!</p>
              </b-tab>
            </b-tabs>
          </b-col>
          <b-col sm="auto"></b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      current_id: 0,
      image_path: "../assets/examp.jpg",
      pics: [{ message: "examp" }, { message: "examp_01" }]
    };
  },

  mounted() {
    console.log("halljfwojfio");
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

  computed: {
    my_message: function() {
      return this.$route.params.id;
    },

    myPath() {
      return "../assets/examp" + this.current_id + ".jpg";
    }
  },

  watch: {
    my_message() {
      this.current_id = this.$route.params.id;
    }
  }
};
</script>

<style></style>
