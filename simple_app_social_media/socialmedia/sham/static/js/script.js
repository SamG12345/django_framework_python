document.addEventListener("DOMContentLoaded", function (){
    // Like action
    var likeButtons = document.querySelectorAll(".like-button");
    if (likeButtons) {
        likeButtons.forEach(element => {
            element.addEventListener("click", function(e) {
                var lekhId = e.currentTarget.closest('.lekh');
                likeHandler(e, lekhId);
            });
        });
    }

    function likeHandler(e, lekhId) {
        const url = "/like/" + lekhId.dataset.lekhId;
        fetch(url, {
            method: "GET"
        }).then(response => response.json()).then(data => {
            console.log(data.message);
            var likeCountElement = lekhId.querySelector('#no_of_likes');
            var likebuttonelement = lekhId.querySelector('.like-button');
            var value = likeCountElement.innerText;
            var split = value.split(" ");
            
            
            if(data.message == "Liked"){
                split[0] = Number(split[0])+1;
                likeCountElement.innerText = split.join(" ");
                likebuttonelement.innerText = "Unlike";
                
            }
            else if(data.message == "Unliked"){
                split[0] = Number(split[0])-1;
                likeCountElement.innerText = split.join(" ");
                likebuttonelement.innerText = "Like";
            }
        });
    }

    // like icon action
    var fa = document.querySelectorAll(".fa");
    if (fa){
        fa.forEach(element => {
            if (element.id == "like"){
                like_button_initi(element, false);
            }
            else{
                like_button_initi(element, true);
            }
            element.addEventListener("click", (e)=>{
                var lekhId = e.currentTarget.closest('.lekh');
                likeHandler(e, lekhId);
                var c = element.style.color;
                if (c=="crimson"){
                    element.style.color = "#888";
                }
                else{
                    element.style.color="crimson";
                }
            });
        });
        
    }
    // like icon css
    function like_button_initi(x, b){
        if (b){
            x.style.color="crimson";
        }
        else{
            x.style.color = "#888";
        }
    }

    // lekh remove confr
    var l_rm_c = document.querySelectorAll("#l_rm");
    if (l_rm_c){
        l_rm_c.forEach(element => {
            element.addEventListener("click", ()=>{
                console.log("ok");
                var ol = document.querySelector(".overlay");
                ol.style.display = "block";
                console.log(ol);
                var oll = ol.getElementsByTagName("button");
                oll[0].addEventListener("click", ()=>{
                    console.log("ok");
                    ol.style.display = "none";
                });
                oll[1].addEventListener("click", ()=>{
                    console.log("ok");
                    ol.style.display = "none";
                });
                
            })
        })
    }
    // lekh del
    function l_rm (lekhid){
        const url = "delete/" + lekhid;
        fetch(url, {
            method: "GET"
        }).then(response => response.json()).then(data => {
            if (data.message == "deleted"){
                console.log("ok");
            }
            else {
                console.log("no");
            }
        })
    }


})

