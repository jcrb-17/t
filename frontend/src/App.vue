<template>
    <div id="search">
        <input id="searchInput" type="text" placeholder="search">
        <button type="submit" class="btn" @click="search">Send</button>    
    </div>
    <div id="nav">

    </div>

    <div class="c">
        <item class="w-full"
        v-for="item in m.hits.hits" 
        :key="item._id"
        :from="item._source.from"
        :to="item._source.to"
        :date="item._source.date"
        :subject="item._source.subject"
        :message="item._source.message"
        :val="v1"
        >
        </item>
    </div>

</template>

<script>
import axios from "axios";
import format from "./format";
import format2 from "./format2";
localStorage.setItem("pag",0);

export default {
    data(){
        return {
            v1:"",
            total:0,
            m:
            {
                hits:{hits:""}
            },
            c:0
        }
    },
    methods:{
        search(){
            let v = document.getElementById("searchInput").value;
            this.v1 = v;
            this.c += 1;
            axios.get(`http://localhost:3000/search/${v}/${localStorage.getItem("pag")}`)
            .then( (response) =>{
                // handle success
                let x = JSON.parse(response.data)
                console.log(x);
                this.m = x;
                this.total = this.m.hits.total.value;
                this.addBtns();
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                //format the word
                format(v);
            });
        },
        addBtns(){
            let nav = document.getElementById("nav");
            let t = Math.ceil(this.total/10);//para paginacion
            nav.innerHTML = "";
            for(let i = 0;i<t;i++){
                let b = document.createElement("button");
                b.textContent = i+1;
                b.className = "btn btnNav";
                nav.appendChild(b);
            }
            let btns = document.getElementsByClassName("btnNav");
            let cl = "black";
            btns[((parseInt(localStorage.getItem("pag"))+10)/10)-1].style.background = cl;
            btns[((parseInt(localStorage.getItem("pag"))+10)/10)-1].style.color = "white";            for (let i = 0; i < btns.length; i++) {

            btns[i].addEventListener("click",function(e){
                let k = format2(parseInt(e.target.textContent));
                localStorage.setItem("pag",k);
                btns[i].style.background = cl;
                btns[i].style.color = "white";
                formatOther(i);
            });
            }

            function formatOther(j){
                let btns = document.getElementsByClassName("btnNav");
                for (let i = 0; i < btns.length; i++) {
                    if(j==i){
                        continue;
                    }else{
                        btns[i].style.background = "white";
                        btns[i].style.color = "black";
                    }
                }

            }

        }
        
    }
}
</script>
<style>
    h3{
        background:rgb(218, 218, 218);
    }
    #app{
        margin: 10px auto;
    }
    #search{
        text-align: center;
        background: white;
        margin-bottom: 20px;
    }
    #search input{
        border-radius: 10px;
        border:1px solid rgb(214, 214, 214);
        padding:5px;
        margin-right:10px;
        background-color: rgba(241, 241, 241, 0.557);

    }
    #search input:active{
        border:1px solid black;
    }
    f{
        border-bottom:2px solid blue;
    }
    .c{
        width:1000px;
        margin: 0 auto;
    }
    #nav{
        margin: 0 auto;
        text-align: center;
    }
    #nav button{
        margin: 3px;
        transition: all ease .7s;
    }
</style>