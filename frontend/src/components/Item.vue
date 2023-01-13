<template>
    <div class="item">
        <h6 class="text-2xl font-bold itemContent">{{ subject }}</h6>
        <p><b>From</b></p><p class="itemContent">{{ from }}</p>
        <p><b>To</b></p><p class="itemContent">{{ to }}</p>
        <p><b>Date</b></p><p class="itemContent">{{ date }}</p>
        <button :class="visible? 'btn btnShow h' : 'btn btnShow'" 
        @click="toggle">
        {{ visible ? 'Hide' : 'Show' }}
        </button>

        <div :class="visible? 'r' : 'b' ">
            <p class="msg itemContent">{{ message }}</p>
        </div>
    </div>
</template>

<script>

export default {
    props:[
        "subject",
        "from",
        "to",
        "message",
        "date",
        "val"
    ],
    data() {
        return{
            visible:true,
        }
    },
    methods:{
        toggle(){
            this.visible = !this.visible;
        }
    }
}
</script>

<style>

    .msg{
        max-height: 300px;
        overflow: auto;
        font-family: monospace;
        padding:5px;
        border:1px solid rgb(216, 216, 216);
        margin-top: 10px;
        animation:fade .6s ease 1;
        border-radius: 10px;
        font-size:16px;
        transition: all ease .6s;
    }
    .msg:hover{
        border:1px solid blue;
    }

    .item{
        border:1px solid rgb(216, 216, 216);
        padding:10px;
        margin:10px;
        border-radius: 10px;
        transition:all ease .7s;
        animation:fade .7s ease 1;
        background-color: white;
        overflow: hidden;
        position: relative;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.234);
        transition: all ease .6s;

    }
    .item:hover{
        border:1px solid rgb(59, 155, 220);
    }
    .btn{
        border:1px solid black;
        padding:4px;
        border-radius: 10px;

    }
    @keyframes fade {
        from {opacity:0;}
        to {opacity:1;}
    }
    @keyframes height {
        from {height:auto;}
        to {height:0;}
    }
    .btnShow{
        position: absolute;
        right:30px;
        top:20px;
        width:60px;
        height: 40px;
        transition: all ease .5s;
    }
    .r{
        visibility: visible;
        animation: fade .6s 1 ease;
        transition: all ease .6s;
        max-height: 300px;
    }

    .b{
        visibility: hidden;
        height: 0px;
        transition: all ease .6s;
    }

    .item h6{
        /* background: linear-gradient(150deg,rgb(58, 194, 240), rgb(49, 231, 128)); */
        /* background-clip: text; */
        /* color:transparent; */
        color: black;
    }
</style>