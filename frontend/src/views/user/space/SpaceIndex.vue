<script setup>
import {useRoute, useRouter} from "vue-router";

const route=useRoute()           //取当前url相关信息
const router=useRouter()         //操作打开一个界面或后退，例子如下
//
// router.push({
//   name:'homepage-index'
// })                             实现功能：打开用户信息界面自动跳转首页
</script>

<template>
个人空间:{{ route.params.user_id }}
</template>

<style scoped>

</style>