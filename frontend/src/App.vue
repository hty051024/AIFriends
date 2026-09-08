<script setup>

import NavBar from "@/components/navbar/NavBar.vue";
</script>

<template>
  <NavBar>
    <RouterView />
<!--                                //RouterView作用：自动根据后面的url去index.js里找这个url对应的component，并把其渲染到RouterView这个位置-->
  </NavBar>


</template>

<style scoped>

</style>
