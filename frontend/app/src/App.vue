<template>
  
  <div>
    <p v-if="error">Something went wrong...</p>
  <p v-if="loading">Loading...</p>
  <p v-else v-for="person in result.allNames" :key="person.id">
    {{ person.id }}
    {{ person.name }}
    {{ person.age }}
  </p>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'

const PEOPLE_QUERY = gql`
  query People {
    allNames {
      name,
      age,
      id
    }
  }
`

export default {
  name: 'App',
  setup () {
    const { result, loading, error } = useQuery(PEOPLE_QUERY);
    return {
      result,
      loading, 
      error
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>