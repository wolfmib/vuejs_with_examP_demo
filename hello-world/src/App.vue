<template>
  <div id="app">

    <hr>
    <Header />
    <hr>
    <b-container class="bv-example-row">
      <b-row>
        <b-col  >
          <Problem 
          v-if="problems.length"
            :current_problem="problems[index]"
            :next="next"
          />
        </b-col>
      </b-row>
    </b-container>
    
    <hr>

    <b-container class="bv-example-row">
      <b-row>
        <b-col md="4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique recusandae labore magni nisi dolores assumenda alias vel doloremque modi officia perspiciatis ipsum, facere totam repellat est iste, quas, itaque a.</b-col>
        <b-col md="4" cols="7">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut possimus unde quidem asperiores voluptatem officiis repellat nobis quasi, aliquid quisquam.</b-col>
        <b-col md="4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta similique adipisci nemo. Eveniet id atque ad porro! Sequi architecto molestias, ut autem minus doloribus officiis?</b-col>
      </b-row>
      <hr> 
      <b-row>
        <b-col md="3">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad quae impedit commodi porro eum. Eligendi incidunt, nesciunt velit quae aut accusamus, fugiat ipsam iste ut doloribus odit ad maxime est!</b-col>
        <b-col md="3" offset-md="4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti rerum quae optio, asperiores tempora, labore rem voluptatem quas est voluptatum tenetur, voluptas laudantium voluptates alias fuga nemo doloribus aperiam at?</b-col> 
      </b-row>
    </b-container>

  </div>
</template>
<script>
 
   import Header from './components/Header.vue'
  import Problem from './components/Problems.vue'



  export default{
    name: 'app',
    components:{
      Header,
      Problem
    },

    data(){
      return {
        problems: [],
        index: 0
      }
    },

    methods:{
      next(){
        this.index++
      }
    },

    //[Mary]: Api call mount here
    // and save data to the problems: []
    mounted: function (){
      fetch('https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=multiple',{
        method: 'get'
      })
      .then((response) => {
        return response.json()
      }).then((jsonData) => {
        console.log(jsonData.results)
        this.problems = jsonData.results
      })

    }
  }

</script>




<style>
</style>
