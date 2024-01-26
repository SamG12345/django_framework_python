document.addEventListener("DOMContentLoaded", function (){
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
        console.log("ok = ", lekhId);
        const url = "like/" + lekhId.dataset.lekhId;
        fetch(url, {
            method: "GET"
        }).then(response => response.json()).then(data => {
            console.log(data.message);
            var likeCountElement = lekhId.querySelector('.no_of_likes');
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

})