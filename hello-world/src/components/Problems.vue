<template>

	<div class='problem-box-ref'>

  <b-jumbotron>

    <template v-slot:lead>
			{{current_problem.question}}
  
		</template>

    <hr class="my-4">

		<b-list-group>
			<b-list-group-item
				v-for="(answer,index) in answers" 
				:key="index"
				@click="selectAnswer(index)"
				:class="[selectedIndex === index ? 'selected' : '']"
				>
				{{ answer }}
			</b-list-group-item>
		</b-list-group>
 

    <b-button variant="primary" href="#"> Submit  </b-button>
    <b-button @click="next" variant="success" href="#"> Next</b-button>
  </b-jumbotron>
	</div>
    

</template>

<script>

import _ from 'lodash'

export default {
	// In order to do that object.question, object.answers, we need
	//  to annouce the props , to set the variable to Object
	props: {
		current_problem: Object,
		next: Function,
	},

	data: function() {
		return {
			selectedIndex: null,
			shuffledAnswers: []
		}

	}, 
	computed:{
		answers(){
			let answers = [...this.current_problem.incorrect_answers]
			answers.push(this.current_problem.correct_answer)
			return answers
		}
	},

	watch:{
		current_problem() {
			this.selectedIndex = null
			this.shuffleAnswers()
		}
	},

	methods: {
		selectAnswer(index) {
			this.selectedIndex = index
			console.log(index)
		},
		shuffleAnswers(){
			let answers = [...this.current_problem.incorrect_answers]
			this.shuffledAnswers = _.shuffle(answers)

		}
	}, 

	mounted(){
		console.log(this.current_problem)
	}

}
</script>

<style scoped>
	.list-group{
		margin-bottom: 20px;
	}
	.btn {
		margin: 0 5px;
	}

	.list-group-item:hover{
		background: #eee;
		cursor: pointer;
	}


	.selected{
		background-color: blue;
	}

	.correct{
		background-color: green;
	}
	.incorrect{
		background-color: red;
	}




</style>