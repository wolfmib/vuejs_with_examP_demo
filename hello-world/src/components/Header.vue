<template>
    
  <div>
        <!-- Previos logo-pic
             img-src="https://picsum.photos/600/300/?image=25" 
             Note: after create your entry point in vue js like this
              /my_image/?image=1 to load first photo in the header-->

  <b-card
    title="JA ExampP Problems Collection and Draft Solutions"
    img-src= "https://picsum.photos/600/300/?image=25"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 40rem;"
    class="mb-2"
  >
  <b-card-text>
		<b-nav tabs >
      <b-nav-item disabled> <b> Problem Content</b></b-nav-item>
      <b-nav-item disabled>Your Answer !!</b-nav-item>
    </b-nav>  
  </b-card-text>	
  </b-card>
</div>

</template>


<style scoped>
/* Used to central the card class 
.card {
        margin: 0 auto;
        float: none;
        margin-bottom: 10px;
}
*/

</style>