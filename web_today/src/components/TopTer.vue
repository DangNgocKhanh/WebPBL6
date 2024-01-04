<template>
    <div class="flex flex-col fixed z-30   max-w-[1000px] w-full  items-center  bg-sky-400">
        <div  class="flex  w-full -md px-3 py-2 bg-sky-400 justify-between items-center border-sky-600 border-b-[1px]">
            <div class="flex gap-2 items-center text-[25px] font-bold">
                <router-link to='/'><img src="@/assets/2.png" class="w-[50px] h-[50px]"/></router-link>
                <router-link to='/' >Cao_Minh_Duc</router-link>
                <!-- <div v-if="counter.Table_Lg_Rg==2" class="flex  bg-gray-200 h-[40px] gap-3 items-center w-[364px] rounded-full px-3">
                    <router-link to="/Search-Friends" v-on:click="counter.Search_friend();">
                        <button><svg   role="img" height="24" width="24" aria-hidden="true" class="fill-gray-900 Svg-sc-ytk21e-0 uPxdw mOLTJ2mxkzHJj6Y9_na cursor-pointer_" viewBox="0 0 24 24" data-encore-id="icon"><path d="M10.533 1.279c-5.18 0-9.407 4.14-9.407 9.279s4.226 9.279 9.407 9.279c2.234 0 4.29-.77 5.907-2.058l4.353 4.353a1 1 0 1 0 1.414-1.414l-4.344-4.344a9.157 9.157 0 0 0 2.077-5.816c0-5.14-4.226-9.28-9.407-9.28zm-7.407 9.279c0-4.006 3.302-7.28 7.407-7.28s7.407 3.274 7.407 7.28-3.302 7.279-7.407 7.279-7.407-3.273-7.407-7.28z"></path></svg></button>
                    </router-link>
                    <input placeholder="Search..."  class="w-full text-gray-600  text-[16px] font-normal bg-gray-200 outline-none" v-model="counter.search_friend"/>
                </div> -->
            </div>
            <div v-if="counter.Table_Lg_Rg == 1">
                <button v-if="counter.Form_Lg_R==false" v-on:click="counter.Form_Lg_R=!counter.Form_Lg_R" class="drop-shadow-md w-[100px] py-2 text-[16px] text-semibold bg-black rounded text-white">Đăng nhập</button>
                <button v-if="counter.Form_Lg_R==true" v-on:click="counter.Form_Lg_R=!counter.Form_Lg_R" class="drop-shadow-md w-[100px] py-2 text-[16px] text-semibold bg-black rounded text-white">Đăng kí</button>
            </div>
            <div v-if="counter.Table_Lg_Rg == 2" class="flex gap-1 text-[18px] font-semibold text-gray-900 justify-center items-center bg-orange-400 px-2 py-1 rounded">
                <div class="flex gap-1 justify-center items-center">
                    <font-awesome-icon icon="fa-solid fa-circle-user" class="text-[22px]"/>
                    <h1 class="">{{ counter.openthongtincanhan.username }}</h1>
                    <div class="h-[20px] w-[1px] bg-gray-800"></div>
                </div>
                <router-link to="/" v-on:click="counter.dangxuattaikhoan(); counter. Show_DD_image=!counter. Show_DD_image" >Đăng xuất</router-link>
            </div>
        </div>
        <div v-if="counter.Table_Lg_Rg == 2" class="flex justify-center items-center w-full text-[20px] font-bold h-full py-2 px-3 border-sky-600 border-b-[1px]">
            <router-link to="/" v-on:click="counter.list_select=[]" :class="{'border-b-[2px] border-orange-700 text-orange-700':counter.Path_Route.path=='/'}" class="flex justify-center items-center px-2  cursor-pointer h-full">Trang chủ</router-link>
            <router-link :to="i.url" v-for="i in counter.model_list_all" v-on:click="counter.F_reset_if_SV(); counter.F_Device_list_select(i.url);" :class="{'border-b-[2px] border-orange-700 text-orange-700':counter.Path_Route.path=='/' + i.url}" class="flex justify-center items-center px-2 h-full  cursor-pointer">{{ i.Name }}</router-link >
        </div>
    </div>
</template>


<script >

    import { useCounterStore } from '@/stores/counter';
    import axios from 'axios';
    import VueCookies from 'vue-cookies'


    export default {

    setup() {
        const counter = useCounterStore();
        return {counter}
    },
    }
</script>


